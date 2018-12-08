from sklearn.model_selection import train_test_split
#from keras.layers.core import Activation, Dense
#from keras.layers.embeddings import Embedding
#from keras.layers.recurrent import LSTM
# keras.models import Sequential
#from keras.preprocessing import sequence
import pandas as pd
def loadData():
    para = pd.read_excel('2017_parameter.xlsx',header=None)
    quality = pd.read_excel('2017_quality.xlsx',header=None)
    return para,quality
para, quality = loadData()
print(para.shape[2])
Xtrain, Xtest, ytrain, ytest = train_test_split(para, quality, test_size=0.2, random_state=42)

#EMBEDDING_SIZE = 128
#HIDDEN_LAYER_SIZE = 64
#model = Sequential()
#model.add(Embedding(vocab_size, EMBEDDING_SIZE,input_length=MAX_SENTENCE_LENGTH))
#model.add(LSTM(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))
#model.add(Dense(1))
#model.add(Activation("sigmoid"))
#model.compile(loss="binary_crossentropy", optimizer="adam",metrics=["accuracy"])
