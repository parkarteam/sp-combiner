import numpy as np
import click

class Combiner(object):

    def aggregate(self, Xs, features_names=None):
        """average out the probabilities from multiple classifier and return that as a result"""			
           # click.echo('inside aggregator Xs: %s' % Xs)    
        click.echo('Feature names    : %s ' % features_names)   
        click.echo('Mean    : %s ' % np.mean([float(x[0]) for x in Xs]))   
        return np.mean([float(x[0]) for x in Xs])

    
# Function to convert 
def listToString(s): 
    # initialize an empty string 
    str1 = "" 
    # traverse in the string 
    for ele in s: 
        str1 += ele 
    # return string 
    return str1 
        

if __name__== "__main__":
    clf1_res = np.array(['0.80', 'Spam'])
    clf2_res = np.array(['0.9959868467126312e-04', 'Spam'])

    example = np.array([clf1_res, clf2_res])
    combine = Combiner()
    res = combine.aggregate(example, features_names=None)
    print(res)

