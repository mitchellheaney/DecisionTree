import numpy as np
from os import path
from Helper import splitTrainTest
import sys

def main():

    # gather user information
    response = input("\nEnter the file name, target varaible and number of predictive features respecively: ")
    filename, targetVar, givenFeatNum = response.split(' ')
    
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
    target = np.squeeze(rawData[:,targetIdx])                 # NOTE: data is now 2d array, target is single array all same length
        
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
    
    
    

if __name__ == "__main__":
    main()