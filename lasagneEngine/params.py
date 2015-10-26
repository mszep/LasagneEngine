#parent : parent set of param, None if first initialization 
#init_value : init value: 
#end_value : end value
#type : 
#
#associated session :
#model : associated model
import timeit
import threading
import cPickle


class Params(object):

    def __init__(self,parent=None):
        """
        """
    	self.parent = parent

    def save(self,filename):
    	None

    def load(self,filename):
    	None