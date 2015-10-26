import timeit
import threading
import cPickle
from multiprocessing import Process, Manager

class LasagneEngine(object):
    def __init__(self):
        """
        """
        #
        self.data_manager = DataManager()
        self.displayer = Displayer(self)
        self.thread_manager = Manager()
        self.free_gpus = []
        self.models = dict()
        self.sessions = {}
        self.running_threads = {}
        self.stop_events = {}

    def __set_gpu_context__(self):
        """
        """
        gpu = self.free_gpus
        self.sessionKey.start(gpu)
        self.free_gpus.append()

        import theano.sandbox.cuda
        theano.sandbox.cuda.use(private_args['gpu'])

        import theano
        import theano.tensor as T
        from theano.tensor.shared_randomstreams import RandomStreams

    def __free_gpu__(self,gpu):
        None

    def set_ngpus(self,ngpus):
        """ Set the numper of accessible gpus
        """
        for i in range(0,ngpus): 
            self.free_gpus.append("gpu" + str(i))



    def register_model(self,modelKey,model):
        """
        """
        self.models[modelKey] = model

    def get_model(self,modelKey):
        return self.models[modelKey]



    def register_session(self,sessionKey,session):
        """
        """
        self.registered_sessions[sessionKey] = session

    def get_session(self,sessionKey):
        """
        """
        return self.sessions[sessionKey]

    def __session_thread__(self,sessionKey):
        """
        """
        gpu = self.__set_gpu_context__()
        session = self[sessionKey] 
        session.start()
        self.__free_gpu__(gpu)

    def start_session(self,sessionKey):
        """
        """
        if sessionKey in self.session.keys():
            if len(self.free_gpus) != 0:
                self.registered_session[sessionKey]
                args = manager.list()
                args.append({})
                #start session in other process
                p = Process(target=self.session_thread(sessionKey),
                        args=(args,sessionKey,))
                self.running_process.append(p)
            else 
                print "NO FREE GPUS, USE STOP AN OTHER SESSION OR WAIT UNTIL ONE IS FINISHED"

    def stop_session(self,sessionKey):
        """
        """
        print "check if key exists"
        self.running_sessions[sessionKey].stop()
        self.stop_events[sessionKey] = threading.Event()



