import itertools
from textwrap import wrap

begin = 'y'

def combos(list_of_lists):
    results = []
    for i in itertools.product(*list_of_lists):
        results.append(''.join(i))
    return results

def sperm_gen(dad_genotype, traits):
    alleles = []
    #splits up dad_genotype into each individual allele, in sublists based on trait the allele controls for
    alleles = wrap(dad_genotype, 2)
    alleles = [list(i) for i in alleles]
    #generates possible sperm combinations using combo()
    sperm = combos(alleles)
    #removes duplicate possibilities
    sperm = list(set(sperm))
    return sperm

def egg_gen(mom_genotype, traits):
    alleles = []
    #splits up mom_genotype into each individual allele, in sublists based on trait the allele controls for
    alleles = wrap(mom_genotype, 2)
    alleles = [list(i) for i in alleles]
    #generates possible egg combinations using combo()
    egg = combos(alleles)
    egg = list(set(egg))
    return egg

def genotype_gen(sperm, egg):
    genotypes = []
    for i in sperm:
        for k in egg:
            genotypes.append(i+k)
    return genotypes

def chisqr(expected_list):
    #chi squared stuff
    actual = input('actual values in same order as printed expected, separated by comma: ')
    actual = actual.split(',')
    actual = [int(x) for x in actual]
    chisqrvals = []
    counter = 0
    for i in actual:
        expected = expected_list[counter]
        chisqrvals.append(((i-expected)**2)/expected)
        counter+=1
    chisqrval = sum(chisqrvals)
    print('chi squared value: ',chisqrval)
    return chisqrval

def conclusion(chisqrval):
    variables = int(input('input number of variables: '))
    degrees_of_freedom = variables-1
    p_val = float(input('p value: '))
    table_result = float(input('input table value: '))
    if chisqrval <= table_result:
        print('p value is valid')

def prob_calcs():
    ratios = input('ratios, separated by colons (e.g., 9:3:3:1): ')
    ratios = ratios.split(':')
    ratios = [int(x) for x in ratios]
    denominator = sum(ratios)
    population = int(input('population size: '))
    population_ratios = []
    for i in ratios:
        population_ratios.append(i/denominator*population)
    print(population_ratios)
    chsqrval = chisqr(population_ratios)
    conclusion(chsqrval)

def setup(traits, dad_genotype, mom_genotype):
    sperm = sperm_gen(dad_genotype, traits)
    egg = egg_gen(mom_genotype, traits)

    genotypes = genotype_gen(sperm, egg)
    print('genotypes: '+', '.join(genotypes))

while begin == 'y':
    traits = int(input('number of traits: '))
    dad_genotype = input("Dad genotype: ")
    mom_genotype = input("Mom genotype: ")
    setup(traits, dad_genotype, mom_genotype)
    prob_calcs()
    begin = input("Would you like to do another? y or n: ")