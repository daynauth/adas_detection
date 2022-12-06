"""
@author: Roland Daynauth
@date: 2018-01-31
@version: 1.0
@description: This script is used to plot the distribution of the classes in the dataset.
"""
import matplotlib.pyplot as plt
import pandas as pd

def main(path: str):
    """
    This function is used to generate a distribution of the classes in the dataset.
    :param path: The path to the dataset.
    :return: None
    """
    df = pd.read_csv(path, header=None)

    # Get the distribution of the classes.
    df  = df[0].value_counts()
    df = df.drop('0', axis = 0)
    df = df/df.sum()*100
    df.plot(kind='bar')



    plt.xlabel('Class')
    plt.ylabel('Frequency (%)')
    plt.savefig('distribution.png', bbox_inches="tight")

if __name__ == '__main__':
    path = 'distribution.csv'
    main(path)