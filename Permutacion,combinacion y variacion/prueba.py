#PERMUTACION CON REPETICION

def permutation_with_repetition(n, lst):
    if n == 0:
        return [[]]
    result = []
    for item in lst:
        for permutation in permutation_with_repetition(n-1, lst):
            result.append([item] + permutation)
    return result
n = 3
lst = [1,2,3]
permutations = permutation_with_repetition(n, lst)
for p in permutations:

    print(p)
print("El numero de combinaciones posibles en este caso son", len(permutations))