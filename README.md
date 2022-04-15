# Graph partition optimization

From a non oriented graph, possibly weighted in R. The principal objective is to partition the graph into p classes, so that the sum of the weights between vertices not belonging to the same class is minimal. Moreover, it's necessary to ensure that the vertices of the graph are distributed in a (more or less) equitable way in the p classes. And finally establish what is the best method to solve this problem.

## Python script

```text
Usage: python3 src/main.py [filePath] [options]
Options:
  -h, --help: print this help message
  -e, --enum: perform basic enumeration
  -g, --gradient: perform gradient descent
  -m1, --meta1: perform simulated annealing
  -m2, --meta2: perform tabu search
  -t, --time: set the time limit for the algorithm (default: 600)
  -k, --class: set the number of classes to be considered (default: 2)
  -s, --size: set a size for the neighborhood (default: all the neighborhood)
  only for gradient descent or metaheuristics
```

Use:

```shell
python3 -m cProfile -s tottime src/main.py [filePath] [options]
```

for perfomance.

## Shell script for benchmarking (test all the instances)

Before running the script make sure to do: `chmod u+x src/benchmark.sh`

```text
Usage: ./benchmark.sh [dataDir] [solDir] [algo] [timeLimit] [sizeNeighborhood]
where algo can be one of these:
  --enum
  --gradient
  --meta1
  --meta2
timeLimit is the time limit in seconds,
and sizeNeighborhood is the size of the neighborhood
only for the meta-heuristics (default: all the neighborhoods).
```
