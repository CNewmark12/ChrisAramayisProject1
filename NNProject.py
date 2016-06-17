# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 14:45:18 2016

@author: Dell 15r
"""
import numpy as np

#This file will begin to replicate my neural network project


##############################################################################
#Initializing everything
data_Size = input('Enter how many data points will be used: ')
print("We will have " + data_Size + " data points.")

Num_Of_Inputs = input('Enter the number of inputs: ')
print("Number of inputs is: " + Num_Of_Inputs)

inputs = np.zeros(shape = (int(data_Size),int(Num_Of_Inputs)))
print(inputs)

Num_Of_Hidden_Layers = input('Enter the number of hidden layers (exluding the output layer): ')
print("Number of hidden layers is: " + Num_Of_Hidden_Layers)

HiddenLayerSize = np.zeros(int(Num_Of_Hidden_Layers))
print(HiddenLayerSize)

for i in range(0,int(Num_Of_Hidden_Layers)):
    inputQ = "Neurons in layer " + str(i + 1) + ": "
    HiddenLayerSize[i] = input(inputQ)
    print("Neurons in layer " + str(i + 1) + " is " + str(HiddenLayerSize[i]))

#End Initializing
##############################################################################

##############################################################################
#Creating Matrices   
MatrixList = [inputs]

for i in range(0,int(Num_Of_Hidden_Layers)):
    if i == 0:
        MatrixList.append(np.random.rand(int(Num_Of_Inputs),int(HiddenLayerSize[0])))
    else:
        MatrixList.append(np.random.rand(int(HiddenLayerSize[i-1]),int(HiddenLayerSize[i])))
        
MatrixList.append(np.random.rand(int(HiddenLayerSize[int(Num_Of_Hidden_Layers) -1]),int(data_Size))) 

for i in MatrixList:
    print(i)
#Setting each weight