# DecisionTree

## About the Project

Decision/Classification trees represent a tree-like structure that uses independent factors of a
dataset to predict outcomes upon one dependent varaible in some dataset. Each node in the tree
has a threshold which asks the decision model whether a certain feature variable is below/above 
this requirement (decision nodes), and depending on the distribution, the tree will continue to 
split feature variables until all thats left in the dataset are leaf nodes withholding target 
variable options.

The input exploratory data must in a CSV format and in the same directory as Main.py. This must
include the target column as well in the same file for predictive samples. 

## Assumptions

1. The decision tree must take in **quantitative** independent data columns.
2. The target, dependent variable is **qualitative**.
3. Datasets are in the form of a CSV file in the same directory.

## Drawbacks/Learning Aspirations

The fitting model is executed without pruning - a process that removes unnecessary complexity 
from the tree's strucutre. The project has allowed me to substantiate skills surrouding ML modelling,
algorithmic data structures (trees) and useful Python modules such as numpy.

### This was done without sklearn module
