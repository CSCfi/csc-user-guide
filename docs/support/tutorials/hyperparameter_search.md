# Hyperparameter search

In machine learning (ML), one key component in model selection is to select a suitable set of configurations for a model for solving a given statistical problem. These model configurations are known as *hyperparameters*.

This is in no way an easy task. Statistical estimation problems assumes that there exists an optimal solution, however in many real-world problems there is no guarantee that such a solution exists. For example, in biological and medical applications the variability of observations makes near impossible to obtain optimal, separable decision boundaries; whereas (the canonical) seabass and salmon sorting does have a more (or less) optimally defined solutions; and in linguistics they maybe statistically optimal solutions, however semantically the results may be incomprehensible to humans. The lack of an optimal solution makes it difficult to give recommendations for setting up hyperparameters in a ML for a given problem. For this reason, this document chooses to use the term **search** instead of **optimization** (as it appears more frequently in ML literature). 

Some key points when attempting hyperparameter searching:

+ the amount of available data
+ choice of loss function ( determines what type of estimator to be used )
+ choice of solver

These points are conditioned of each other. Hyperparameters can be numerical (discrete or continuous) or categorical (type of regularization, activation functions, solvers), and additionally many hyperparameters (may) have both linear and nonlinear effects on each other. Since ML models are applied to statistical problems, there is no substitue for good statistical knowledge of the problem at hand: this helps setting some possible hyperparameter options and their ranges and choosing the right type of estimator. For example, if all patterns, or almost all, are considered important to the problem at hand, parallel learning methods are preferable (such as neural networks); then if only some patterns are considered important then sequential statistical methods should be preferred. Choosing suitable hyperparameters can be done either manually or automatically. This documentation focuses on automated searching.

In order to do hyperparameter search, the data is randomly divided into three separate sets: *training*, *validation* and *test* sets. The search for hyperparameters are done such a way, that a model is trained against a validation set. Once the suitable set of hyperparameters have been found, the model is then evaluated against the test set.

One thing to keep in mind however: since a change in a hyperparameter defines a new model, *all* hyperparameter searches select the best model w.r.t to a given metric (probability of error for example), which is statistically a questionable approach. Training $$n$$ models on the *same* data set induces a dependency, which has to be considered when comparing different models. ANOVA or Bernoulli trials could be considered here when comparing different models on the same data.

## Search strategies

There are five main categories of searching for hyperparameters.

### Grid search

In *Grid search*, the hyperparameters of a model are considered occupying a grid. Each grid point corresponds to a hyperparameter, and then the grid is searched and evaluated w.r.t given metric. This approach is more suitable when the number of hyperparameters and their ranges are few. This is because Grid search does an exhaustive search from the entire search space, which is then time consuming when given a large space. This approach would be more appropriate if you are searching for a small number of hyperparameters, or for suitable categorical hyperparamters, such as type of regularizer and type of solver. Grid search is also easily parallelizable approach.


### Randomized search

*Randomized search* allows searching for hyperparameters from a larger search space. Given a set of hyperparameters and their lower and upper bound ranges, values are randomly selected from the given ranges. In theory, given a large search space, Random search will be able to find more suitable set of hyperparameters. As in with Grid search, Random search is also an easily parallelizable approach. 


### Adaptive search

The previous two approaches do not take into account of previously evaluated hyperparameter candidates. *Adaptive search*, or *Bayesian optimization*, utilizes previously evaluated hyperparameters to direct its search for a new set of hyperparameters. The search is done by training a *surrogate model*, which contains a set of initial hyperparameters. After a surrogate model has been trained, an *acquisition function* is used to direct the search for new hyperparameters. This approach is sequential in nature: the search moves forward only after the set of hyperparamters have been evaluated by the acquisition function, making adaptive search difficult to parallelize.


### Multifidelity search

*Multifidelity search* addresses the problem of searching large hyperparameter spaces, particularly for large neural network models. The search is divided into *low* and *high* fidelity evaluations: low fidelity involves a small subset of training data while high fidelity involves a large subset of training data. The performances of each hyperparameters from low and high fidelity evaluations are recorded and those which performed best are selected to the next evaluation. There are two popular multifidelity approaches: *successive halving* and *hyperband*. In successive halving, each evaluation iteration discards half of the "poorest performing" hyperparameters which have a static budget, and keeps the better half of the hyperparameters. This process in continued until the best set of hyperparameters remain. Hyperband addresses the static nature of successive halving by dynamically allocating the amount budget to hyperparameters during iterations, using successive halving as a subroutine for selecting the suitable hyperparameters.


### Metaheuristics

*Metaheuristics* are a set of search methods that can cope with difficult constraints, such as nonconvexity, noncontinuous and nonsmooth functions. In theory, metaheuristics can do better approximations to a global optimum (if a true optimum exists) for large scale models. For hyperparameter search, popular metaheuristic approaches are *evolutionary computation* and *particle swarm* approaches: in evolutionary computation, a set of initial, random hyperparameters are evaluated, then mutated and selected according to a fittness function; particle swarm approaches in a similar manner, but searching for hyperparameters are done in a semi-collective manner: each hyperparamter is individually evaluated and then information is shared between all hyperparameters to direct the search for a new set of hyperparameters. 

## Software for hyperparameter search

This documentation is biased towards the Python programming languages. We present here which have a clearer API and documentation and suitable for using them in CSC's computing infrastructure.

Due to package dependencies, you should load the python-data module with the latest python version:

```bash
module load python-data/3.9-1
```


#### Scikit-learn

When Grid or Random search is a suitable option for hyperparameter search, **Scikit-learn** has implemented both Grid and Random search with cross-validation. Cross-validation is its own model selection process, and is highly dependent on the amount of available data and, for example, the number of folds to use (number of folds and train/test data split are dependent variables). Note that if you are testing a *larger number* of possible models, you will be in risk of getting an overfitted model.

```python
# Scikit-learn 
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
hyperparams = { ... } # list of hyperparameters with their ranges and options

gridsearch   = GridSearchCV( model, hyperparams, ... )

... = # Define data splits

gridsearch.fit( Xtrain, ytrain )
```

#### Optuna

**Optuna** is a model agnostic library for hyperparameter search. Additionally to Grid and Random search, Optuna implements Tree-structured Parzen estimator and CMA-ES sampling methods for searching hyperparameters, and additionally you can implement your own custom sampler methods. To make searching more efficient, multifidelity search can be done with Optuna, with Median and Threshold as an additional pruning option of the search space. 

```python
# Optuna
import optuna
model       = ... # Define model
hyperparams = { ... }

gridsearch = optuna.create_study( sampler = optuna.samplers.GridSampler( params ) )
gridsearch.optimize( model )
```

#### Scikit-optimize

**Scikit-optimize** implements adaptive search strategies and is built right on scikit-learn. This makes it easy to implement right on top of models which are built using scikit-learn.

```python
# Scikit-optimize using Scikit-learn models
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier()  # Define GradientBoosting

from skopt.space import Real, Integer
from skopt.utils import use_name_args

hyperparams = [ Integer( 1, 5, name = 'max_depth' ),
		        Real( 10 ** -5, 10 ** 0, 'log-uniform', name = 'learning_rate' ) 
	          ]

@used_named_args( space )
def objective( **hyperparams ):
	model.set_params( **hyperparams )
	return -( np.mean( cross_val_score( model, X, y, cv = 3, n_jobs = -1, scoring = 'neg_mean_absolute_error' ) )

# Execute Gaussian Process
from skopt import gp_minimize

model_gp = gp_minimize( objective, hyperparams, n_class = 50, random_state = 123 )
```

#### Ray

For the case you would like to enable parallel model selection, *Ray* offers an efficient wrappers for various Python packages. In case you need packages that are not included in the python-data module, use
```python
pip install --user <package-name>
```
If you want to use Ray to parallelize models build with scikit-learn, the easiest way is to use **tune-sklearn** package. With tune-sklearn, you will get better parallelization performance using Ray, instead of using **n_jobs = -1** argument within GridSearchCV or RandomizedSearchCV functions. Here's is an example using **TuneGridSearchCV** with models using scikit-learn:

```python
from ray.tune.sklearn import TuneGridSearchCV

from sklearn.linear_model import SGDClassifier


model               = SGDClassifier()
hyperparameter_grid = { "loss": [ 'hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron' ],
                        "max_iter": [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 ],
                        "n_iter_no_change": [ 5, 10, 15, 25, 40, 60 ] 
                      }

tune_search = TuneGridSearchCV( model, hyperparameter_grid, early_stopping = True, max_iters = 10, 
                                use_gpu = False, n_jobs = -1 )

... # Do your data split into train, validation and test sets
tune_search.fit( Xtrain, ytrain )
print( tune_search.best_params_ )
```
It is recommended to have a lot of hyperparameter options on the grid to exploit Ray's parallelism. If you have a small set of hyperparameters to try out then use the methods what are offered in scikit-learn.

**TuneSearchCV** function enables to do Randomized and Adaptive Search. To switch to an adaptive search, change the **search_optimization** argument. By default TuneSearchCV uses Randomized search. Instead of fixed set of hyperparameters, use suitable ranges using Numpy or Scipy functions. Note that different *search_optimization* arguments may have packages dependencies which you have to install if they are missing.

```python
from ray.tune.sklearn import TuneSearchCV 
hyperparameter_grid = { ... } # Set hyperparameter ranges

# Randomized search
tune_randomized = TuneSearchCV( model, hyperparameter_grid, early_stopping = True, 
                                    search_optimization = 'random',
                                    max_iters = 10, use_gpu = False, n_jobs = -1 )

tune_bayes      = TuneSearchCV( model, hyperparameter_grid, early_stopping = True, 
                                    search_optimization = 'bayesian',
                                    max_iters = 10, use_gpu = False, n_jobs = -1 )
```

### Example using CSC's supercomputers

Here are case examples of doing model selection using Puhti and Mahti. Be sure to assign the number of cpus **explicitly** in Puhti. In Mahti when you reserve a node, you automatically reserve the max number of cpus. Also check the documentation for the partition names to use in both Puhti and Mahti.


```batch
# example-slurhm.sh
#!/bin/bash
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --time=10:00:00
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --cpus-per-task=40
#SBATCH --account=projectname

module load python-data/3.9-1

set -xv
python3 $*
```

```python
# hyperparameter_example.py
from ray.tune.sklearn import TuneGridSearchCV
from sklearn.linear_model import SGDClassifier


model               = SGDClassifier()
hyperparameter_grid = { "loss": [ 'hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron' ],
                        "max_iter": [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 ],
                        "n_iter_no_change": [ 5, 10, 15, 25, 40, 60 ] 
                      }

tune_search = TuneGridSearchCV( model, hyperparameter_grid, early_stopping = True, max_iters = 10, 
                                use_gpu = False, n_jobs = -1 )

X, y = load_digits(n_class=10, return_X_y=True)

Xtrain, Xtest, ytrain, ytest = train_test_split( X, y, train_size = 0.90, test_size = .1, random_state = 0 ) # Split chosen arbitrarily

tune_search.fit( Xtrain, ytrain )
print( tune_search.best_params_ )
print( tune_search.best_score_ )
print( tune_search.score( Xtest, ytest ) )
```

```batch
sbatch example-slurm.sh hyperparameter_example.py 
```

### Large-scale model building

For searching large number of hyperparameters or large scale models, such as neural networks, Ray offers a convenient way to do parallel and distributed searching. Below are examples of how to use Ray with Tensorflow and PyTorch packages.

#### Ray pt.1

Here are some examples using paralllel, distributed hyperparameter search for neural networks.

#### Tensorflow - Hyperparameter search with Adaptive search
```python
# Define model training
def train_nn( config ):
    # Import stuff from Tensorflow

    from tensorflow.keras.datasets import mnist
    data, num_classes = mnist.load_data(), 10
        
    Xtrain, ytrain, Xtest, ytest = data
    img_shape = Xtrain.shape[ 1: ]
    
    Xtrain  = Xtrain.astype( 'float32' )
    Xtest   = Xtest.astype( 'float32' )
    Xtrain /= 255.0
    Xtest  /= 255.0
    
    ytrain = to_categorically( ytrain, num_classes )
    yest   = to_categorically( ytest , num_classes )
    
    # Define neural network
    inputs = keras.Input( shape = img_shape )
    x      = layers.Flatter()( inputs )
    
    hid1 = int( config[ 'hidden1' ] )
    hid2 = int( config[ 'hidden2' ] )
    dout = config[ 'dropout' ]
    
    x = layers.Dense( units = hid1, activation = 'relu' )( x )
    
    if dout != 0: x = layers.Dropout( rate = dout )( x )
    
    if hid2 > 0 :
        x = layers.Dense( units = hid2, activation = 'relu' )( x )
        if dout != 0: x layers.Dropout( rate = dout )( x )
            
    outputs = layers.Dense( units = num_classes, activation = 'softmax' )( x )
    model   = keras.Model( inputs = inputs, outputs = outputs, name = 'mlp' )
    opt     = keras.Optimizer.Adam( learning_rate = config[ 'lr' ] )
    
    model.compile( loss      = 'categorical_crossentropy',
                   optimizer = opt,
                   metrics   = [ 'accuracy' ]
                 )
    
    # from ray.tune.integration.keras import TuneReportCallback
    callbacks = [ TuneReportCallback( { 'train_accuracy': 'accuracy',
                                        'train_loss'    : 'loss',
                                        'val_accuracy'  : 'val_accuracy',
                                        'val_loss'      : 'val_loss'
                                      }
                                    )
                ]
    
    history = model.fit( Xtrain, ytrain,
                         epochs           = config[ 'epochs' ],
                         batch_size       = 32,
                         callbacks        = callbacks,
                         validation_split = 0.2,
                         verbose          = 0
                       )
# end of train_nn

import ray
from ray.tune.suggest.bayesopt import BayesOptSearch

ray.init()
analysis = ray.run( train_nn,
                    name                = 'mlp',
                    scheduler           = ASHAScheduler( time_attr = 'train_iteration' )
                    metric              = metric,
                    mode                = 'max',
                    search_alg          = BayesOptSearch(),
                    num_samples         = 10,
                    resources_per_trial = { 'cpu': 20,
                                            'gpu': 1
                                          },
                   config               = { 'dataset': ,
                                            'epochs' : 10,
                                            'dropout' : tune.choice( [ 0.0, 0.1, 0.2, 0.25, 0.4, 0.5 ] ),
                                            'lr'      : tune.choice( [ 0.001, 0.01, 0.002, 0.0015 ] ),
                                            'hidden1' : tune.uniform( 32, 512 ),
                                            'hidden2' : tune.uniform( 0, 128 )
                                          }
                  )
print( 'Hyperparameters found: ', analysis.best_config )
print( 'Best value for ', metric, ': ', analysis.best_result[ metric ] )

ray.shutdown() # Always add this to the end. Terminates workers spawned by Ray
```

#### PyTorch - Parallel model selection ( from docs.ray.io )
```python
import os
import numpy as np
from filelock import FileLock

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

import ray

ray.init()

# The number of sets of random hyperparameters to try.
num_evaluations = 10


# A function for generating random hyperparameters.
def generate_hyperparameters():
    return {
            "learning_rate": 10**np.random.uniform(-5, 1),
            "batch_size"   : np.random.randint(1, 100),
            "momentum"     : np.random.uniform(0, 1)
           }
# end of generate_hyperparameters

def get_data_loaders( batch_size ):
    
    mnist_transforms = transforms.Compose(
                                           [ transforms.ToTensor(),
                                             transforms.Normalize( ( 0.1307, ), ( 0.3081, ) ) 
                                           ]
                                         )

    # We add FileLock here because multiple workers will want to
    # download data, and this may cause overwrites since
    # DataLoader is not threadsafe.
    with FileLock( os.path.expanduser( "~/data.lock" ) ):
        train_loader = torch.utils.data.DataLoader(
                                                    datasets.MNIST( "~/data",
                                                                    train     = True,
                                                                    download  = True,
                                                                    transform = mnist_transforms
                                                                  ),
                                                    batch_size = batch_size,
                                                    shuffle    = True
                                                  )
    
    test_loader = torch.utils.data.DataLoader(
                                               datasets.MNIST( "~/data", train = False, 
                                                               transform = mnist_transforms ),
                                               batch_size = batch_size,
                                               shuffle    = True 
                                             )
    return train_loader, test_loader
# enf of get_data_loaders

class ConvNet(nn.Module):
    """Simple two layer Convolutional Neural Network."""

    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 3, kernel_size=3)
        self.fc = nn.Linear(192, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 3))
        x = x.view(-1, 192)
        x = self.fc(x)
        return F.log_softmax(x, dim=1)
# enf of class ConvNet

def train(model, optimizer, train_loader, device=torch.device("cpu")):
    """Optimize the model with one pass over the data.

    Cuts off at 1024 samples to simplify training.
    """
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        if batch_idx * len(data) > 1024:
            return
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
# end of train

def test(model, test_loader, device=torch.device("cpu")):
    """Checks the validation accuracy of the model.

    Cuts off at 512 samples for simplicity.
    """
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(test_loader):
            if batch_idx * len(data) > 512:
                break
            data, target = data.to(device), target.to(device)
            outputs = model(data)
            _, predicted = torch.max(outputs.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()

    return correct / total
# end of test

@ray.remote
def evaluate_hyperparameters(config):
    model = ConvNet()
    train_loader, test_loader = get_data_loaders(config["batch_size"])
    optimizer = optim.SGD(
        model.parameters(),
        lr=config["learning_rate"],
        momentum=config["momentum"])
    train(model, optimizer, train_loader)
    return test(model, test_loader)
# end of evaluate_hyperparameters

# Evaluate hyperparameters in a synchronous parallel manner
# Keep track of the best hyperparameters and the best accuracy.
best_hyperparameters = None
best_accuracy = 0
# A list holding the object refs for all of the experiments that we have
# launched but have not yet been processed.
remaining_ids = []
# A dictionary mapping an experiment's object ref to its hyperparameters.
# hyerparameters used for that experiment.
hyperparameters_mapping = {}

# Randomly generate sets of hyperparameters and launch a task to evaluate it.
for i in range(num_evaluations):
    hyperparameters = generate_hyperparameters()
    accuracy_id = evaluate_hyperparameters.remote(hyperparameters)
    remaining_ids.append(accuracy_id)
    hyperparameters_mapping[accuracy_id] = hyperparameters

# Fetch and print the results of the tasks in the order that they complete.
while remaining_ids:
    # Use ray.wait to get the object ref of the first task that completes.
    done_ids, remaining_ids = ray.wait(remaining_ids)
    # There is only one return result by default.
    result_id = done_ids[0]

    hyperparameters = hyperparameters_mapping[result_id]
    accuracy = ray.get(result_id)
    print("""We achieve accuracy {:.3}% with
        learning_rate: {:.2}
        batch_size: {}
        momentum: {:.2}
      """.format(100 * accuracy, hyperparameters["learning_rate"],
                 hyperparameters["batch_size"], hyperparameters["momentum"]))
    if accuracy > best_accuracy:
        best_hyperparameters = hyperparameters
        best_accuracy = accuracy

# Record the best performing set of hyperparameters.
print("""Best accuracy over {} trials was {:.3} with
      learning_rate: {:.2}
      batch_size: {}
      momentum: {:.2}
      """.format(num_evaluations, 100 * best_accuracy,
                 best_hyperparameters["learning_rate"],
                 best_hyperparameters["batch_size"],
                 best_hyperparameters["momentum"]))
		 
ray.shutdown()
```
### A Bayesian approach to model comparison after hyperparameter search

Here is an example of using **Bayesian analysis** for statistically comparing models from each other using hyperparameter search. The MNIST dataset will be used as an example.

```python
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
import warnings
warnings.simplefilter("ignore", UserWarning)

# Load MNIST data
X, y = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False)

train_samples = 5000
test_samples  = 10000

# Comparing three models: Logistic regression, Support vector machine and multi-layer perceptron. 
# Default hyperparameters from scikit-learn library will be used, except some will be fine tuned.

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

import scipy.stats as stats

svc = SVC()
## Hyperparameters to search for SVM
# Grid Search
hp_svc_gs = [ { 'kernel': [ 'linear' ], 'C': [ 0.4, 0.8, 1.0 ], 'shrinking': [ True, False ] },
              { 'kernel': [ 'poly' ]  , 'degree': [ 2, 3, 4, 5 ], 
                'C': [ 0.4, 0.8, 1.0 ], 'shrinking': [ True, False ] }  
            ]

# Randomized and adaptive search
hp_svc_rs = [ { 'kernel': [ 'linear' ], 'C': stats.uniform( 0, 1 ), 'shrinking': [ True, False ] },
              { 'kernel': [ 'poly' ]  , 'degree': np.random.randint( 2, 10 ), 
                'C': stats.uniform( 0, 1 ), 'shrinking': [ True, False ] }  
            ]


#lgr = LogisticRegression()
## Hyperparameters to search for Logistic regression


#mlp = MLPClassifier()
## Hyperparameters to search for MLP

```
