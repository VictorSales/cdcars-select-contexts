from Tkinter import *
import tkFileDialog
from tkFileDialog import askopenfilename 
import numpy as np
from numpy import genfromtxt
from sklearn import cross_validation
from skfeature.function.information_theoretical_based import MRMR

def main():
      
    root = Tk()
    #select dataset with file extension *.csv
    root.filename = tkFileDialog.askopenfilename(initialdir = "/",
                                                 title = "Select file",
                                                 filetypes = 
                                                 (("csv files","*.csv"),
                                                  ("all files","*.*")))
    print(root.filename)
    data = genfromtxt(root.filename, delimiter=',')
    data = data[~np.isnan(data).any(axis=1)]
    contexts = data[:, [0,1,2,3,4,5,6]]    # data # label
    class_rating = data[:,7]
    # number of samples and number of features
    n_samples, n_features = contexts.shape 
    # split data into 10 folds
    data_splitted = cross_validation.StratifiedKFold(class_rating, n_folds=10, 
                                                     shuffle=True) 
    num_fea = 7    # number of selected features
    
    for train, test in data_splitted:
        # obtain the index of each feature on the training set
        idx,J_CMI,MIfy = MRMR.mrmr(contexts[train], class_rating[train], 
                                   n_selected_features=num_fea)
        # obtain the dataset on the selected features
        print "Index of Top Selected Features",idx;
        # corresponding objective function value of selected features
        print "J_CMI",J_CMI;
        # corresponding mutual information between selected features
        print "MIfy",MIfy;
                
if __name__ == '__main__':
    main()