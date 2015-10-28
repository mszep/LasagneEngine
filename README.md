# LasagneEngine

Still WIP. Stable version will be pushed soon (~ 12/2015)

##What 

This project is a prototype for a visual framework for Deep Learning. Deep Learning has shown exciting results in several domains of machine learning. Training a deep learning network required a lot of expertise and understanding of the underlying concepts. Awesome libraries as Theano and Lasagne for python has enable people who design those models to spend more time on understanding the models rather than developing it. 
By enabling people to have a framework to manage their models and their training sessions through usefull visualization, this project aims to push trough this direction.

## How
Lasagne developers have made an awesome job to leverage the power of Theano and enable its users to be efficient when defining a new network model. However, when your model is define you still need to manage its training, and its evolution by yourself. As Deep Learning is a lot about looking 
Lasagne engine is about making you efficient to iterate with the following features : 
  - Run several INDEPENDANT models on the same machine when several GPUs are available.
  - Manage theano variables allocation in an easy wayand thus GPUs memory allocation
  - Save and load a models and parameters (weights in the network)
  - Manage live training sessions
  - Track the evolution of training metrics (training loss, validation loss, ..) on a running session
  - Visualize interesting metrics on your parameters

## Current Design 
  - Engine is the main class. It manage your models and your different training sessions 
  - Displayer is a class that aims to contains the visualialisation bit for the different classes. It's the step 0 through a future UI for Deep Learning
  - Model is just a container for a model that will be define using Lasagne 
  - DataManager allow you to associate numpy array in memory with name and take care to load this data in theano variables (aka in GPUs) when needed 
  - Session handles the training of your network 
  - Params define a specific set of parameters for a specific models. Each models can evolve through different Params that you want to keep track of. 
