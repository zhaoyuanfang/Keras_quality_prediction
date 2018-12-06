from pandas import  DataFrame,concat
from pandas import read_csv
from sklearn.preprocessing import *
def series_to_supervised(data,n_in=1,n_out=1,dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    for i in range(n_in,0,-1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)'%(j+1,i)) for j in range(n_vars)]
    for i in range(0,n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)'%(j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)'%(j+1,i)) for j in range(n_vars)]
    agg = concat(cols,axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace = True)
    return agg

dataset = read_csv("pollution.csv",header=0,index_col=0)
values = dataset.values
encoder = LabelEncoder()
values[:,4] = encoder.fit_transform(values[:,4])
values=values.astype('float32')
scaler=MinMaxScaler(feature_range=(0,1))
scaled = scaler.fit_transform(values)
reframed=series_to_supervised(scaled,1,1)
reframed.drop(reframed.columns[[9,10,11,12,13,14,15]],axis = 1,inplace = True)
print(reframed.head)