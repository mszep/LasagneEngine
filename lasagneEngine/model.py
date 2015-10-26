
class Model(object):
    def __init__(self,engine,filename=None):
        """
        """
        if filename != None: 
            self.load_model(filename)
        else: 
            None

    def load_model(self,filename):
        None

    def start_session(self,session):
        if len(self.free_gpus) == 0:
            print "No gpus available, use Displayer' sessions method to see current running sessions"
        else:
            print "Session started"

    
    def display_past_sessions(self):
        None