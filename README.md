# LasagneEngine

Still WIP. Bugs to correct and changing API. Stable version will be pushed soon (~ 12/2015)

##What 

Prototype for a visual framework for Deep Learning. Deep Learning has shown exciting results in several domains of machine learning. Training a deep learning network requires a lot of expertise and understanding of the underlying concepts. For python, some libraries such as Theano and Lasagne have enabled people who design those models to spend more time on understanding what they do rather than developing their models. 
By enabling people to have a framework to manage models and training sessions through useful visualization, this project aims to push in this direction.

## How
Lasagne (https://github.com/Lasagne/Lasagne) developers have done an awesome job to leverage the power of Theano. We can now be efficient when defining a new network model. However, when your models are defined, you still need to manage their training, and their evolution by yourself.
LasagneEngine is about making you efficient to iterate when you build new models, providing the following features : 
  - Run several INDEPENDENT models on the same machine when several GPUs are available.
  - Manage allocation of theano variables (and therefore GPU memory) in an easy way.
  - Save and load models and parameters (weights in the network)
  - Manage live training sessions
  - Track the evolution of training metrics (training loss, validation loss, ..) on a running session
  - Visualize interesting metrics on your parameters

## Current Design 
  - Engine is the main class. It manages your models and your different training sessions.
  - Displayer is a class that contains the visualisation bits for the different classes. It's the first step towards a future UI for Deep Learning
  - Model is just a container for a model that you define using Lasagne 
  - DataManager allows you to associate numpy arrays in memory with names and take care to load this data in theano variables (ie in GPUs) when needed by your sessions
  - Session handles the training of your network 
  - Params define a specific set of parameters for a specific models. Each model can evolve through different Params that you want to keep track of.
