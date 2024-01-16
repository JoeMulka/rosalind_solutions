import os

data_dir = r"C:\Users\msute\OneDrive\Documents\Dev\Rosalind\data"
data_path = os.path.join(data_dir, "11_rosalind_fibd.txt")

# Check if data path file exists
if os.path.exists(data_path):
    with open(data_path, "r") as infile:
        input_data = infile.read()
        input_data = input_data.split()
else:
    sample = [6, 3]
    input_data = sample

all_rabbits = []


# An object representing a pair of rabbits
class RabbitPair:
    # Constructor
    def __init__(self, age=0):
        self.age = 0

    def update(self):
        self.age += 1

    def __str__(self) -> str:
        print(str(self.age))


class RabbitPopulation:
    # Constructor
    def __init__(self, all_pairs=[], ending_gens=6, max_age=3) -> None:
        self.all_pairs = all_pairs
        self.all_pairs.append(0)
        self.ending_gens = ending_gens
        self.max_age = max_age
        # Rosalind seems to like 1 indexed generation number
        self.current_gen = 1
        self.total_pop_history = [1]

    def run_simulation(self):
        while self.current_gen < self.ending_gens:
            self.update_population()
            self.current_gen += 1

    def update_population(self):
        # Update all rabbits
        num_new_pairs = 0
        for index, pair in enumerate(self.all_pairs):
            # Rabbit pair is old enough to reproduce
            if pair >= 1:
                num_new_pairs += 1
            self.all_pairs[index] += 1
        for x in range(0, num_new_pairs):
            self.all_pairs.append(0)

        # Remove old rabbits
        self.all_pairs = [pair for pair in self.all_pairs if pair < self.max_age]
        self.total_pop_history.append(len(self.all_pairs))


class MortalFibbonacci:
    def __init__(self, ending_gens, max_age):
        self.ending_gens = ending_gens
        self.max_age = max_age
        self.sequence = [1, 1]

    def run_simulation(self):
        while len(self.sequence) < self.ending_gens:
            if len(self.sequence) > self.max_age:
                new_value = (
                    self.sequence[-1]
                    + self.sequence[-2]
                    - self.sequence[-(self.max_age + 1)]
                )
            else:
                new_value = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(new_value)
        print(self.sequence)


class RabbitTable:
    # We make a table where each column represents a possible age of a the rabbit
    def __init__(self, ending_gens=6, max_age=3):
        self.ending_gens = ending_gens
        self.max_age = max_age
        self.table = [[0 for x in range(0, max_age)] for y in range(0, ending_gens)]
        self.table[0][0] = 1

    def run_simulation(self):
        for gen in range(1, self.ending_gens):
            for age in range(0, self.max_age):
                if age == 0:
                    self.table[gen][age] = sum(self.table[gen - 1][1:])
                else:
                    self.table[gen][age] = self.table[gen - 1][age - 1]

        # print(self.table)
        print("final_population = {}".format(sum(self.table[-1])))


if __name__ == "__main__":
    # Create a rabbit population
    # rabbit_pop = RabbitPopulation(ending_gens=10, max_age=3)
    # rabbit_pop.run_simulation()
    # print("Max age: " + str(rabbit_pop.max_age))
    # print(rabbit_pop.total_pop_history)

    rabbit_table = RabbitTable(ending_gens=95, max_age=19)
    rabbit_table.run_simulation()
