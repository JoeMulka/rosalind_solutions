from itertools import permutations
from scipy.stats import binom
from collections import Counter


def single_allele_probs(first_allele, second_allele, mother_genotype):
    allele_offspring = [
        tuple(sorted([x, y]))
        for x in (first_allele + second_allele)
        for y in mother_genotype
    ]
    counter = Counter(allele_offspring)
    probs = {k: v / 4 for k, v in counter.items()}
    return probs


def generate_probabilities():
    """
    Generate a dictionary of probabilities of each offspring type for a given father geno
    The mother geno is always AaBb
    """
    offspring_probs = {}

    possible_father_genos = [
        tuple(sorted([a1, a2]) + sorted([b1, b2]))
        for a1 in "Aa"
        for a2 in "Aa"
        for b1 in "Bb"
        for b2 in "Bb"
    ]

    for father_geno in possible_father_genos:
        # Always mating with an "AaBb" organism
        first_a_allele, second_a_allele, first_b_allele, second_b_allele = father_geno
        a_probs = single_allele_probs(first_a_allele, second_a_allele, "Aa")
        b_probs = single_allele_probs(first_b_allele, second_b_allele, "Bb")
        combined_probs = {
            father_geno: {
                a_key + b_key: a_val * b_val
                for a_key, a_val in a_probs.items()
                for b_key, b_val in b_probs.items()
            }
        }
        offspring_probs.update(combined_probs)

    return offspring_probs


if __name__ == "__main__":
    # Looking for the probability of having at least N organisms with genotype Aa Bb in generation k
    generation_number = 7
    target_geno_min = 37

    # The original parent has genotype Aa Bb
    # All organisms mate with an outside organism with genotype Aa Bb
    # Thus the genotype of any one organism is enough to determine the probabilities of its offspring
    offspring_probs = generate_probabilities()
    # Check that the probabilities sum to 1
    for individual_prob in offspring_probs:
        assert sum(offspring_probs[individual_prob].values()) == 1

    # population is not actually pop counts, but rather the probability of each genotype
    # We can interact with it as if it were a population, though
    population = {("A", "a", "B", "b"): 1}
    for i in range(1, generation_number + 1):
        next_pop = {}
        for extant_genotype in population.keys():
            # Get probability distribution of offspring of this genotype
            genotype_probs = offspring_probs[extant_genotype]
            # multiply the probability of each offspring by the probability this genotype
            genotype_probs = {
                k: v * population[extant_genotype] for k, v in genotype_probs.items()
            }
            for father_geno in genotype_probs.keys():
                if father_geno in next_pop:
                    next_pop[father_geno] += genotype_probs[father_geno]
                else:
                    next_pop[father_geno] = genotype_probs[father_geno]

        population = next_pop
    num_individuals = 2**generation_number
    AaBb_frac = population[("A", "a", "B", "b")]
    print(
        f"fraction of population with genotype Aa Bb at generation {generation_number}: {AaBb_frac}"
    )
    print(f"number of individuals in this generation: {num_individuals}")
    probability = 1 - binom.cdf(target_geno_min - 1, num_individuals, AaBb_frac)
    print(
        f"probability of at least {target_geno_min} individuals with genotype Aa Bb in generation {generation_number}: {probability}"
    )
