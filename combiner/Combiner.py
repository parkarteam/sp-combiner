import numpy as np
import click

class Combiner(object):

    def aggregate(self, Xs, features_names=None):
    		"""average out the probabilities from multiple classifier and return that as a result"""			
	   		click.echo('inside aggregator Xs: %s' % Xs)     
    	return np.mean([float(x[0]) for x in Xs])



# if __name__== "__main__":
#     clf1_res = np.array(['0.80', 'Spam'])
#     clf2_res = np.array(['0.9959868467126312e-04', 'Spam'])

#     example = np.array([clf1_res, clf2_res])
#     combine = Combiner()
#     res = combine.aggregate(example, features_names=None)
#     print(res)

