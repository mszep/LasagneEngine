"""
"""
class Displayer(object):
    def __init__(self,engine):
        self.engine = engine 

    def __display_stripe__(self):
        print "********************************************************************************"

    def models(self,deep=False):
        """
        """
        self.__display_stripe__()
        print "Mounted models are"
        for key in self.engine.models.keys():
            print str(key) 
            if deep:
                self.engine.models[key].display()
            print "  "
        self.display_stripe__()

    def sessions(self,deep=False):
        self.__display_stripe__()
        print str(len(self.sessions)) + " running sessions are"
        for key in self.engine.sessions(): 
            print "    " + str(key)
            if deep: 
                self.engine.sessions[key].display()
            print "    "
        self.__display_stripe__()

    def running_sessions(self,deep=False):
        self.__display_stripe__()
        print str(len(self.engine.running_sessions)) + " running sessions are"
        for key in self.engine.running_sessions(): 
            print "    " + str(key)
            if deep: 
                self.engine.running_sessions[key].display()
            print "    "
        self.__display_stripe__()
