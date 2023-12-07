"""Building clustering analytics models

Returns: 

"""
class Kmean:
    def __init__(self, dfpath):
        """ Read terrorsim datasetwith pandas and creating dataframe object
        Args:
        self(series): original dataframe to be analyzed
        dfpath(str): name of csv file in which dataset is contained
        """
    def preview(self):
        """ Reads first rows of terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            First rows of terrorism data

        """
        self.df = pd.read_csv('terrorismp1.csv')
        return self.df.head()
    
    def catvariables(self):
        """ Creates list of categorical variables
        
        Args:
            self(series): original dataframe to be analyzed
            """
    
    def kmeans(self):