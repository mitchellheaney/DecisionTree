from sklearn import datasets
import numpy as np

def main():
    data = datasets.load_diabetes();
    print(type(data))

    npData = np.genfromtxt('diabetes.csv', delimiter=',', dtype=str)
    print()

    print(npData)

if __name__ == "__main__":
    main()