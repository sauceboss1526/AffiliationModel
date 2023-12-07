"""Building clustering analytics models

Returns: 
    catvariables(list): list of categorical variables
    numvariables(list): list of numerical variables"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn import preprocessing as pre
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline 
from sklearn.cluster import KMeans 
from sklearn.model_selection import cross_val_score
import scipy as sp
from scipy.cluster.hierarchy import dendrogram, ward 

class Kmean:
    """K-means clustering model for terrorism dataset
    returns:
    preprocessor: preprocessing of data
    kmeansmanual: Kmeans clustering with sklearn
          fitting of scikit learn kmeans clustering model with preprocessed data """
    def __init__(self, dfpath):
        """ Read terrorsim datasetwith pandas and creating dataframe object
        Args:
        self(series): original dataframe to be analyzed
        dfpath(str): name of csv file in which dataset is contained

        Returns:
            First rows of terrorism data object"""
        self.df = pd.read_csv(dfpath)
        self.df.offenses = self.df.offenses.astype(str)
        self.df.terrorist = self.df.terrorist.astype(str)
        return self.df
    def peprocessor(self):
        """ Preprocessing of data
        
        Args:
            self(series): original dataframe to be analyzed
        
        Returns:
            Preprocessed dataframe"""
        
        categorical_variables = [i for i in self.df.select_dtypes(include = object) if i != 'name' and i != 'incrimination' and i != 'circumstances' and i != 'date' and i != 'where']
        numerical_variables = [i for i in self.df.select_dtypes(exclude = object) if i!= 'name' and i!= 'incrimination' and i!= 'circumstances' and i!= 'date' and i!= 'where']
        dummy_variables = pd.get_dummies(self.f[categorical_variables], drop_first = True, dtype = 'int64')
        scaled_numerical_variables = [i for i in numerical_variables]
        scaled_numerical_variables = [i for i in numerical_variables]
        array = self.df[numerical_variables].values
        datascaler = pre.MinMaxScaler(feature_range = (0,1))
        dfscaled = pd.DataFrame(datascaler.fit_transform(array), columns = scaled_numerical_variables)
        datascaler = pre.MinMaxScaler(feature_range = (0,1))
        self.modeldf = pd.concat([dummy_variables, dfscaled], axis = 1)
        return self.modelf.head()
    
    def kmeanmanual(self):
        """
          Kmeans clustering with sklearn
          fitting of scikit learn kmeans clustering model with preprocessed data 

          Args: 
            self(series): original dataframe to be analyzed
          Returns:
          results of cluster model fitting with preprocessed data """
        k = 8
        model = KMeans(n_clusters = k, random_state = 0)
        model.fit(self.modeldf)
        clusters = model.predict(self.modeldf)
        manualdf = self.df.copy()
        manualdf.clusters = clusters
        return manualdf
class hierararchical_clustering:
    """
    Hierararchical Clustering
    
    returns:
    hierararchical_clustering: fitting of scikit learn kmeans clustering model with preprocessed data via pipeline  """
    def __init__(self, dfpath):
        """ Read terrorsim datasetwith pandas and creating dataframe object
        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            First rows of terrorism data object"""
        self.df = pd.read_csv('dfpath.csv')
        self.df.offenses = self.df.offenses.astype(str)
        self.df.terrorist = self.df.terrorist.astype(str)
        
        return self.df
    def peprocessor(self):
        """ Preprocessing of data
        
        Args:
            self(series): original dataframe to be analyzed
        
        Returns:
            Preprocessed dataframe"""
        
        categorical_variables = [i for i in self.df.select_dtypes(include = object) if i != 'name' and i != 'incrimination' and i != 'circumstances' and i != 'date' and i != 'where']
        numerical_variables = [i for i in self.df.select_dtypes(exclude = object) if i!= 'name' and i!= 'incrimination' and i!= 'circumstances' and i!= 'date' and i!= 'where']
        dummy_variables = pd.get_dummies(self.f[categorical_variables], drop_first = True, dtype = 'int64')
        scaled_numerical_variables = [i for i in numerical_variables]
        scaled_numerical_variables = [i for i in numerical_variables]
        array = self.df[numerical_variables].values
        datascaler = pre.MinMaxScaler(feature_range = (0,1))
        dfscaled = pd.DataFrame(datascaler.fit_transform(array), columns = scaled_numerical_variables)
        datascaler = pre.MinMaxScaler(feature_range = (0,1))
        self.modeldf = pd.concat([dummy_variables, dfscaled], axis = 1)
        return self.modelf.head()
    

    def hierararchical_clustering(self):
        """
          Hierararchical clustering with scipy
          fitting of scikit learn kmeans clustering model with preprocessed data via pipeline

          Args: 
            self(series): original dataframe to be analyzed
          Returns:
          results of hierarchachal cluster model fitting with preprocessed data """
        matrices = ward(self.modeldf.values)
        dendrogram(matrices, orientation = 'right', labels = list(self.df['name']))
        plt.tick_params(axis = 'x', which = 'both', bottom = 'off', top = 'off', labelbottom = 'off')
        showtime = plt.show()
        return showtime

