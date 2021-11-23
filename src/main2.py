from threading import Thread

def get_all_combinations(parent): # Finds all possible combinations of alleles a parent can pass on to their offspring, assuming independen assortment.
    if len(parent) == 1:
        return [parent[0][0], parent[0][1]]
    else:
        genlist = []
        
        for x in get_all_combinations(parent[1:]):
            genlist.append(parent[0][0] + x)
            genlist.append(parent[0][1] + x)

        return genlist

def make_row(genotype, allele):
	row = []
	for a in genotype:
		row.append(a + allele)
	return row

def make_table(parent1, parent2):
	table = []
	for a in parent1:
		table.append(make_row(parent2, a))
	return table

def print_table(table, c1, c2): # formats and prints Punnett square
	latextable = []
	divlength = (len(c1[0])*2+4)*2**(len(c1[0]))
	print('')
	print('', end=' ')
	for a in c2:
		print(' '*(len(c1[0])+3) + a + '', end=' ')
		latextable.append('& ' + a + ' ')
	print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
	latextable.append('\\\ \n\\hline\n')
	
	for i, row in enumerate(table):
		print(c1[table.index(row)], end=' ')
		latextable.append(c1[table.index(row)] + ' & ')
		print('|', end=' ')
		for j, cell in enumerate(row):
			print(cell + ' | ', end=' ')
			if j != len(row)-1:
				latextable.append(cell + ' & ')
			else:
				latextable.append(cell + ' ')
		print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
		if i != len(table)-1:
			latextable.append('\\\ \n')	
	return latextable		
	
def print_genotype_frequencies(table): # calculates frequencies for each genotype present in table
	freqtable = []
	freqtable.append('\n')
	calculated = []
	genotypes = [a for b in table for a in b]
	for k, x in enumerate(genotypes):
		count = 0
		for y in genotypes:
			if sorted(x) == sorted(y):
				count += 1
		if sorted(x) not in calculated:
			print("The frequency of the " + x + " genotype is " + str(float(count)/float((len(genotypes)))*100) + "%.")
			freqtable.append(x + ' & ' + str(float(count)/float((len(genotypes)))*100) + '\\% \\\ \\hline \n')	
		calculated.append(sorted(x))
	return freqtable	

print('') 
print('==========   Punnett square maker & Latex table export  ==============')
print('') 
print('Hello, and welcome to the Punnett square maker! To get started, enter the genotypes of each parent. There should be two alleles for each gene, and each should be represented by one letter.')
print('The genes should be separated by spaces. For example, a valid genotype would be "Xx Yy zz", while "XxYyZz" or "Xx Yy zz " would not.')
print('') 
print('=====================================================================')
print('')

while True:
	p1 = input("Please enter the genotype of the first parent: ").split(' ')
	p2 = input("Please enter the gentype of the second parent: ").split(' ')
	c1 = get_all_combinations(p1)
	c2 = get_all_combinations(p2)
	a = make_table(c1, c2)
	latextable = print_table(a, c1, c2)
	freqtable = print_genotype_frequencies(a)
	print('')

	action = input("Enter (A) to make another or any key to quit!\n")
	if action == "A":
		print('')
		print("Again!\n")
	else:	
		quit()