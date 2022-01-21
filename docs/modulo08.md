# Modulo 08 - Hyper-parameter Fine Tuning

## What are hyper-parameters?

Hyper-parameters are parameters of an algorithm that determine the performance of that model. The process of tuning these parameters in order to get the most optimal parameters is known as hyper-parameter tuning. The best parameters are the parameters that result in the best accuracy and or the least error.

## How hyper-parameter tuning works?

Given a set of parameters, hyper-parameter tuning works by identifying  the set of parameters that result in the highest accuracy and or least error. This is done by running multiple trials with various  combinations of hyper-parameters. In this process the results are tracked so that the parameters which result in the best performance are settled on.

## Methodologies of Hyper-parameter Tuning

### Grid Search

In Grid search, parameters are defined ad searched exhaustively. Since a model is built for all possible combinations of parameters, this process can be computationally expensive and time consuming. In scikit-learn this can be implemented using the `GridSearchCV` module. 

### Random Search

In this method, a randomized search is performed over the parameters. In this case each configuration is sampled from a distribution over possible parameter values. Unlike `GridSearchCV`, not all the specified parameters will be tried. Compared to exhaustive search, this method is advantageous because you can choose the maximum number of trials wanted for this search. The parameters to be sampled are specified using a dictionary.