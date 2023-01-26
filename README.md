# Majority Voting

### WORK IN PROGRESS
This project concerns agent-based models and simulations of majority voting. The 
main goal is to investigate under which conditions majority voting succeeds in 
selecting the alternative that is in the best interest of the majority. 

## Setup
1. To run the simulations and generate the data, run the script

```commandline
python main.py
```
which will create a csv file `data/clean.csv`, a collection of communities in the 
folder `data/communities`, and a README file with the parameter settings for the 
simulation in `data/README.csv`.

2. To generate the figures, run the script
```commandline
python figures.py
```
which will create a folder `new_figures` containing all the figures. 

3. To run the statistical analysis, run the script
```commandline
python statistics.py
```
which will create several csv files in the folder `stats` with the results of the 
statistical 
analysis.  

## Organization

### The agent-based model: `Community`
The central class `Community` is defined in `community.py`. A `Community` is an 
*agent-based model* consisting of a network of agents, and it can be used to compute 
the estimated accuracy of a given community. The networks are generated with homophilic 
and preferential attachment. 

### Simulations: `Simulation.run()`
The central class `Simulation` and method `Simulation.run()` is defined in 
`simulation.py`, the method produces the csv file `data/clean.csv`. The method 
`Simulation.run()` runs a simulation consisting of generating `number_of_communities` 
communities and estimating the accuracy of each community by running 
`number_of_voting_simulations` voting simulations.  

### Figures
The script `figures.py` creates a folder `new_figures` containing all the 
figures. The folder `generate_figures` contains the scripts that generate 
figures. Each script in that folder is associated with one of the figures. 

### Statistical analysis
The script `statistics.py` runs the statistical analysis that generates several csv 
files in  the folder `stats`. The folder `stats` contains scripts that generate the 
csv files. Each script in that folder is associated with one of the figures.  

## How to cite
todo
