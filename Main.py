import numpy as np
from os import path
from helper import splitTrainTest, __change_numerical__
import sys
from decision_tree import DecisionTree


def main():
    '''
    Facilitates all main user input, decision modelling and accuracy assessment
    
    Arguments:
        N/A
    
    Exceptions:
        AssertionError - Occurs when:
                            - User inputs incorrect data necessary for decision
                              modelling
                            - target variable entered does not exist in chosen
                              csv file
        FileNotFoundError - Occurs when:
                            - file entered is not in same directory
        
    Return Value:
        (void)
    '''
    
    response = input("\nEnter the file name, target varaible, max depth and \
                     number of predictive features respecively: ")
    
    # check correct input structure
    try:
        assert(len(response.split(' ')) == 4)
    except AssertionError:
        print('Ensure all variables are entered with a space in between.')
        sys.exit(0)

    filename, targetVar, maxDepth, givenFeatNum = response.split(' ')
    
    # run checks for filename
    try: 
        open(filename)
    except FileNotFoundError:
        print('\n\t' + filename + " not found. Ensure the file is in directory\
            and the filename matches.")
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
        
    # split data and target into train and test subsets
    dataTrain, dataTest, targetTrain, targetTest = splitTrainTest(data, \
        target, splitSize=0.75)
    
    print(type(splitTrainTest(dataTrain, splitSize=0.5)))
    
    # run checks for number of feature columns in file
    numFeat = min(int(givenFeatNum), len(data[0]))
    
    # execute decision tree fitting model
    clft = DecisionTree(num_feats= numFeat, max_depth= maxDepth)
    root = clft.__fit__(dataTrain, targetTrain)
    
    clft.__print_d_tree__(root)
    
    # run predictive assessment with testing sets
    predictions = clft.predict(dataTest)
    new_t_test = __change_numerical__(targetTest)

    acc = accuracy(new_t_test, predictions)
    print(acc)


def accuracy(y_test, y_pred):
    '''
    Returns the numerical accuracy of a decision model
    
    Arguments:
        y_test (ndarray)        - target column test set
        y_pred (ndarray)        - predicitions made by the decision model
        
    Exceptions:
        N/A
        
    Return Value:
        (float)                 - accuracy rate
    '''
    
    return np.sum(y_test == y_pred) / len(y_test)



if __name__ == "__main__":
    main()