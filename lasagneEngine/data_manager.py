import timeit
import threading
import cPickle


class DataManager(object):

    def __init__(self,gpus_keys):
        """
        """
        #dictionnary of numpy variables to store data in memory
        self.numpy_data = dict()
        #dictionnary of dictionnary of shared variables : {"gpu1" : {"var1" : theano.tensor...}, ..}
        self.shared_variables = dict()
        # dictionnary of list = shared variables currently used by sessions
        self.in_used_shared = dict()
        for key in gpu_keys: 
            self.in_used_shared[key] = []

    def set_numpy_data(self,dataKey,data):
        self.numpy_data[dataKey] = data

    def set_shared_variables(self,variableKey,variable):
        print "check variables"
        self.shared_variables[variableKey] = variable

    def set_in_memory(self,gpuKey,variableKey): 
        print "to do set variable in memory"
        #set value in the right gpu for variableKey
        self.in_used_shared[gpuKey] = variableKey

