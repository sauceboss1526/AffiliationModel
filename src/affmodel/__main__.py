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