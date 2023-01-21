from random import randint
import numpy as np

def splitTrainTest(*args, splitSize):
    
    newData = []
    for sets in args:
        train = []
        accessedIdx = []
        limit = int(len(sets) * splitSize)
        
        # train set
        i = 0
        while i < limit:
            idx = randint(0, len(sets) - 1)
            if idx not in accessedIdx:
                train.append(sets[idx])
                accessedIdx.append(idx)
                i += 1
                
        train = np.array(train)
        test =  np.array([sets[idx] for idx in range(0, len(sets)) if idx not in accessedIdx])
        newData.append(train)
        newData.append(test)
    return newData
        
""" 
This function changes the target column into binary or numerical
indicators to represent a target option for calculations in entropy
"""
def __change_numerical__(target):
        
    tar_options = np.unique(target)
    new_target = []
        
    assigned_nums = {}
    i = 0
    for options in tar_options:
        assigned_nums[options] = i
        i += 1
    
    for idx in range(0, len(target)):
        label = target[idx]
        new_target.append(assigned_nums[label])
        
    return np.array(new_target)