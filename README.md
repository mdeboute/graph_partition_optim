# graph_partition_optim

Usage:

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
