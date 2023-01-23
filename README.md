# DecisionTree

## About the Project

Decision Trees/Classification Trees represent a machine learning classifier that accepts exploratory 
input data, trains it into its model and produces predictive data back to the user. It executes this
through a tree data structure through splitting all the input data into decision nodes until it reaches
leaf nodes. The leaf nodes classify an outcome in the dependent variable we wish to predict by using
information gain and entropy to find correlations (not causations) with independent variables. Each 
decision node withholds a threshold which splits input data into respective branches to aid probabilities.

Note: This decision tree model prints out the tree in pre order and calculates the accuracy rate with
testing subsets.

The input exploratory data must in a CSV format and in the same directory as Main.py. This must
include the target column as well in the same file for predictive samples. Examples are included 
such as 'breast_cancer.csv' and 'diabetes.csv'.

## To Run

1. Install into directory along with CSV file you wish to parse into the model.
2. Run > python Main.py.
3. Input all data the program requires.

## Assumptions

1. The decision tree must take in **quantitative** independent data columns.
2. The target, dependent variable is **qualitative**.
3. Datasets are in the form of a CSV file in the same directory.

## Drawbacks/Learning Aspirations

The fitting model is executed without pruning - a process that removes unnecessary complexity 
from the tree's strucutre. The project has allowed me to substantiate skills surrouding ML modelling,
algorithmic data structures (trees) and useful Python modules such as numpy. I wish to further this
model with random forest algorithms along with a pruning process, ensuring the user obtains
optimal accuracy and simplicity whilst using this model.

### This was done without sklearn module
