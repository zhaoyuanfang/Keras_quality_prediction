# Report
This paper has been published in 《Mechanical Design and Manufacture》.
## Introduction

H company produces engine cylinder block, after production, it needs to carry out quality inspection of the product. Predicting product quality in the production process can discover production problems ahead of time and reduce the cost of product testing. Product quality inspection based on production data is of great significance to all manufacturing companies

## Data Section
- Die Casting Data of Engine Cylinder Block Produced by H Company in 2017  
- The data from H company(This is a real project, so some information is hard to disclose.)

## Methodology

Considering the time characteristics of the production process, a cyclic neural network based on long-short term memory neurons is used to predict the product quality.  


**RNN** can deal with non-linear high-dimensional time series more accurately, but there are some problems as follows: (1) the disappearance of gradient and explosion in weight updating make it difficult for RNN to adapt to the long time series of die casting prediction; (2) the optimal value of delay window length can not be determined in die casting production process. **LSTM** neurons instead of hidden layer neurons in RNN network can acquire long-term memory ability.

## Results

Experimental comparison of LSTM with Holt-winter and multiple linear regression models.  
Here are the results.  

**Model**|**MSE**
---|---
LSTM|0.036
HoltWinter|0.045
MLR|0.035

## Discussion  
The fitting accuracy of LSTM network is better than the other two models, and it also achieves higher prediction accuracy.

## Conclusion  
**LSTM** is used as hidden layer to solve the dynamic model. The results are compared with the other two time series methods. The results show that the quality prediction method based on LSTM has good prediction performance.

This paper presents a new method for quality prediction of die casting and other complex production processes. Considering the time series characteristics of process parameters affecting quality, the accuracy of quality prediction is improved. It is of practical significance for quality prediction of complex production processes. Based on the research contents of this paper, further research work can be carried out in the following areas: solving the over-fitting and other parameter optimization problems of **LSTM** cyclic neural network; carrying out feature engineering based on the prediction results of **LSTM** network to find and optimize the combination of process parameters affecting the quality of die castings; neural network describing the process almost black box, looking for an accurate and clear die casting and other production. Cheng's description is a new challenge.