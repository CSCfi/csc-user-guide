# Hyperparameter search

This guide explains how to do hyperparameter search for machine learning on
CSC's supercomputers. It is part of our [Machine learning guide](ml-guide.md).

## Introduction

In machine learning (ML), one key component in model selection is to select a suitable set of model configurations for solving a given statistical problem. These model configurations are known as *hyperparameters*.

This is in no way an easy task. Statistical estimation problems assumes that there exists an optimal solution, however in many real-world problems there is no guarantee that such a solution exists. For example, in biological and medical applications the variability of observations makes near impossible to obtain optimal, separable decision boundaries; whereas (the canonical) seabass and salmon sorting does have a more (or less) optimally defined solutions; and in linguistics they maybe statistically optimal solutions, however semantically the results may be incomprehensible to humans. The lack of an optimal solution makes it difficult to give recommendations for setting up hyperparameters in a ML for a given problem. For this reason, this document chooses to use the term **search** instead of **optimization** (as optimization appears more frequently in ML literature). 

Some key points when attempting hyperparameter searching:

+ the amount of available data
+ choice of loss function ( determines the type of estimator to be used )
+ choice of solver

These points are conditioned on each other. Hyperparameters can be numerical (discrete or continuous) or categorical (type of regularization, activation functions, solvers), and additionally many hyperparameters (may) have both linear and nonlinear effects on each other. Since ML models are applied to statistical problems, there is no substitute for good statistical knowledge of the problem at hand: this helps setting some possible hyperparameter options and their ranges and choosing the right type of estimator. For example, if all patterns, or almost all, are considered important to the problem at hand, parallel learning methods are preferable (such as neural networks); then if only some patterns are considered important then sequential statistical methods should be preferred. Choosing suitable hyperparameters can be done either manually or automatically. This documentation focuses on automated searching.

In order to do hyperparameter search, the data is randomly divided into three separate sets: *training*, *validation* and *test* sets ( given that there is enough data. Otherwise, the validation set can be omitted ). Hyperparameters are searched using the training data and validated the validation set. Once a suitable set of hyperparameters has been found, the completed model is evaluated against the test set.

One thing to keep in mind however, is that a change in a hyperparameter defines a new model, *all* hyperparameter searches select the best model w.r.t to a given metric (probability of error for example), which is statistically a questionable approach. Training **n** models on the *same* data set induces a dependency, which has to be considered when comparing different models. ANOVA or Bernoulli trials could be considered here when comparing different models on the same data.

## Search strategies

There are five main categories of searching for hyperparameters.

### Grid search

In *Grid search*, the hyperparameters of a model are considered occupying a grid. Each grid point corresponds to a set of hyperparameters, and then the grid is searched and evaluated w.r.t given metric. This approach is more suitable when the number of hyperparameters is low and their ranges is limited. This is because Grid search does an exhaustive search from the entire search space, which can be time consuming with a large search space. So Grid Search would be more appropriate if you are searching for a small number of hyperparameters, or for suitable categorical hyperparameters, such as type of regularizer and type of solver. Grid search approach is easily parallelizable.


### Randomized search

*Randomized search* allows searching for hyperparameters from a larger search space. Given a set of hyperparameters and their lower and upper bounds, values are randomly selected from the given ranges. In theory, given a large search space, Random search will be able to find more suitable set of hyperparameters. Similarly as Grid search, Random search is also easily parallelizable. 


### Adaptive search

Grid and Random search approaches do not take into account the previously evaluated hyperparameter candidates, whereas *adaptive search*, or *Bayesian optimization*, utilizes previously evaluated hyperparameters to direct its search for a new set of hyperparameters. The search is done by training a *surrogate model*, which contains a set of initial hyperparameters. After a surrogate model has been trained, an *acquisition function* is used to direct the search for new hyperparameters. This approach is sequential in nature: the search moves forward only after the set of hyperparameters have been evaluated by the acquisition function, making adaptive search difficult to parallelize.


### Multifidelity search

*Multifidelity search* addresses the problem of searching large hyperparameter spaces, particularly for large neural network models. The search is divided into *low* and *high* fidelity evaluations: low fidelity involves a small subset of the training data while high fidelity involves a large subset of the training data. The performances of each hyperparameter configuration from low and high fidelity evaluations are recorded and those which performed best are selected to the next evaluation. There are two popular multifidelity approaches: *successive halving* and *hyperband*. In successive halving, each evaluation iteration discards half of the "poorest performing" hyperparameter configurations which have a static budget, and keeps the better half of the hyperparameter configurations. This process in continued until the best set of hyperparameters remain. Hyperband addresses the static nature of successive halving by dynamically allocating the amount budget to hyperparameters during iterations, using successive halving as a subroutine for selecting the suitable hyperparameters.


### Metaheuristics

*Metaheuristics* are a set of search methods that can cope with difficult constraints, such as nonconvexity, noncontinuous and nonsmooth functions. In theory, metaheuristics can do better approximations to a global optimum (if a true optimum exists) for large scale models. For hyperparameter search, popular metaheuristic approaches are *evolutionary computation* and *particle swarm* approaches: in evolutionary computation, a set of initial, random hyperparameters are evaluated, then mutated and selected according to a fitness function; particle swarm approaches work in a similar manner, but searching for hyperparameters is done in a semi-collective manner: each hyperparameter is individually evaluated and then information is shared between all hyperparameters to direct the search for a new set of hyperparameters. 

## Software for hyperparameter search

This documentation is biased towards the Python programming languages. We present here software packages which have a clearer API, documentation and are suitable usage in CSC's computing infrastructure.

Due to package dependencies, you should load the python-data module with the latest python version:

```bash
module load python-data/3.9-1
```


#### Scikit-learn

When Grid or Random search is a suitable option for hyperparameter search, **Scikit-learn** has implementations of both Grid and Random search with cross-validation. Cross-validation is its own model selection process, and is highly dependent on the amount of available data and, for example, the number of folds to use (number of folds and train/test data split are dependent variables). Note that if you are testing a *larger number* of possible models, you will be in risk of getting an overfitted model.

```python
# Scikit-learn 
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
hyperparams = { ... } # list of hyperparameters with their ranges and options

gridsearch   = GridSearchCV( model, hyperparams, ... )

... = # Define data splits

gridsearch.fit( Xtrain, ytrain )
```

#### Optuna

**Optuna** is a model agnostic library for hyperparameter search. In addition to Grid and Random search, Optuna implements Tree-structured Parzen estimator and CMA-ES sampling methods for searching hyperparameters, and additionally you can implement your own custom sampler methods. To make searching more efficient, multifidelity search can be done with Optuna, with Median or Threshold as an additional pruning option of the search space. 

```python
# Optuna
import optuna
model       = ... # Define model
hyperparams = { ... }

gridsearch = optuna.create_study( sampler = optuna.samplers.GridSampler( params ) )
gridsearch.optimize( model )
```

#### Scikit-optimize

**Scikit-optimize** implements adaptive search strategies and is built on top f scikit-learn. This makes it easy to implement right on top of models built using scikit-learn.

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
It is recommended to have a lot of hyperparameter options on the grid to exploit Ray's parallelism. If you have only a small set of hyperparameters to try out then use the methods what are offered in scikit-learn.

**TuneSearchCV** function enables the use of Randomized and Adaptive Search. To switch to adaptive search, change the **search_optimization** argument. By default TuneSearchCV uses Randomized search. Instead of fixed set of hyperparameters, use suitable ranges using Numpy or Scipy functions. Note that different *search_optimization* arguments may have packages dependencies which you have to install if they are missing.

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

Here are case examples of doing model selection using Puhti and Mahti. Be sure to assign the number of CPUs **explicitly** in Puhti. In Mahti when you reserve a node, you automatically reserve the max number of CPUs. Also check the documentation for the partition names to use in both Puhti and Mahti.


```batch
# example-slurm.sh
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

### More examples

More examples can be found from <https://github.com/bilbrait/ml-guide-examples>.
