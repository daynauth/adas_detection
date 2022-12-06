"""
@author: Roland Daynauth
@date: 2018-01-31
@version: 1.0
@description: This script is used to generate a distribution of the classes in the dataset.
"""

import os
import pandas as pd


def distribution(path : str):
    return pd.read_csv(path, header=None, delim_whitespace=True)



def main(path: str):
    """
    This function is used to generate a distribution of the classes in the dataset.
    :param path: The path to the dataset.
    :return: None
    """


    # Get the list of files in the dataset.
    files = os.listdir(path)

    # Create a list to store the classes.
    li = []

    # Loop through the files.
    for file in files:
        file_ = os.path.join(path, file)
        li.append(distribution(file_))

    # Concatenate the list of dataframes.
    df = pd.concat(li, axis=0, ignore_index=True)
    
    df.to_csv("distribution.csv", index=False)

    # # Get the distribution of the classes.
    # df[0].value_counts().plot(kind='bar')
    # plt.xlabel('Class')
    # plt.ylabel('Frequency')
    # plt.savefig('distribution.png', bbox_inches="tight")


if __name__ == '__main__':
    path = "../datasets/kitti/training/label_2/"
    main(path)