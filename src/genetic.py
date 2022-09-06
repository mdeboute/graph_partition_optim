import numpy as np


class GeneticAlgorithm:
    def __init__(
        self,
        init_function,
        population_size,
        crossover_rate,
        mutation_rate,
        max_generations,
        fitness_function,
        verbose=False,
    ):
        self.init_function = init_function
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.fitness_function = fitness_function
        self.verbose = verbose

    def getScores(self, population):
        return [self.fitness_function(guy) for guy in population]

    def selection(self, population, scores, k=5):
        # first random selection
        selection_ix = np.random.randint(len(population))
        for ix in np.random.randint(0, len(population), k - 1):
            # check if better (e.g. perform a tournament)
            if scores[ix] < scores[selection_ix]:
                selection_ix = ix
        return population[selection_ix]

    def crossOver(self, p1, p2):
        # children are copies of parents by default
        c1, c2 = p1.copy(), p2.copy()
        # check for recombination
        if np.random.rand() < self.crossover_rate:
            # c1 is the oposite of p2 and c2 is the oposite of p1
            # like: p1=[0,1,0,1,0,1] and p2=[1,0,1,0,1,0]
            # c1=[1,0,1,0,1,0] and c2=[0,1,0,1,0,1]
            for i in range(len(p1)):
                c1[i] = p2[i]
                c2[i] = p1[i]

        return [c1, c2]

    def mutation(self, bitString):
        for _ in range(len(bitString)):
            # check for a mutation
            if np.random.rand() < self.mutation_rate:
                # flip the bit
                x = np.random.randint(0, len(bitString))
                y = np.random.randint(0, len(bitString))
                if x != y and bitString[x] != bitString[y]:
                    bitString[x], bitString[y] = bitString[y], bitString[x]

    def getNextGen(self, selected):
        # create the next generation
        childrens = list()
        for i in range(0, self.population_size, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i + 1]
            # crossOver and mutation
            for c in self.crossOver(p1, p2):
                # mutation
                self.mutation(c)
                # store for next generation
                childrens.append(c)
        return childrens

    # genetic algorithm
    def run(self):
        # initial population of random bitstring
        pop = [self.init_function() for _ in range(self.population_size)]
        # keep track of best solution
        best, best_eval = pop[0], self.fitness_function(pop[0])
        # enumerate generations
        for gen in range(self.max_generations):
            # evaluate all candidates in the population
            scores = self.getScores(pop)
            # check for new best solution
            for i in range(self.population_size):
                if scores[i] < best_eval:
                    best, best_eval = pop[i], scores[i]
                    if self.verbose:
                        print(">%d, new best f(%s) = %.3f" % (gen, pop[i], scores[i]))
            # select parents
            selected = [
                self.selection(pop, scores) for _ in range(self.population_size)
            ]
            # create the next generation
            pop = self.getNextGen(selected)
        return best, best_eval
