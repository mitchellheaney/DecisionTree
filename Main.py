import numpy as np
from os import path
from helper import splitTrainTest
import sys
from decision_tree import DecisionTree

def main():

    # gather user information
    response = input("\nEnter the file name, target varaible, max depth and number of predictive features respecively: ")
    
    # check correct input structure
    try:
        assert(len(response.split(' ')) == 4)
    except AssertionError:
        print('Ensure all variables are entered with a space in between.')
        sys.exit(0)

    filename, targetVar, max_depth, givenFeatNum = response.split(' ')
    
    # run checks for filename
    try: 
        open(filename)
    except FileNotFoundError:
        print('\n\t' + filename + " not found. Ensure the file is in directory and the filename matches.")
        sys.exit(0)
        
    # split data from file into respective feature data and target data
    fileData = np.genfromtxt(filename, delimiter=',', dtype=str)
    targetIdx = np.where(fileData[0] == targetVar)
    rawData = fileData[1:, :]
    data = np.delete(rawData, targetIdx, 1)
    target = np.squeeze(rawData[:,targetIdx])
        
    # run checks for target variable existence
    try: 
        targetCheck = np.where(fileData[0] == targetVar)
        assert(len(targetCheck[0]) == 1)
    except AssertionError:
        print("\n\t Entered target variable not found.")
        sys.exit(0)
        
    # split data and targetData into train and test subsets
    dataTrain, dataTest, targetTrain, targetTest = splitTrainTest(data, target, splitSize=0.75)
    
    # run checks for number of feature columns in file
    numFeat = min(int(givenFeatNum), len(data[0]))
    
    clft = DecisionTree(numFeat, max_depth=max_depth)
    clft.__fit__(dataTrain, targetTrain)
    

if __name__ == "__main__":
    main()