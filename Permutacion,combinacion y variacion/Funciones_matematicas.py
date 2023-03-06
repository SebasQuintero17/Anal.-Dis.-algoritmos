#PERMUTACION ORDINARIA
def Permutacion(numeros):
    if len(numeros) == 0:
        return []
    if len(numeros) == 1:
        return [numeros]
    permutaciones = []
    for i in range(len(numeros)):
        numero_recorrido = numeros[i]
        numeros_restantes = numeros[:i] + numeros[i+1:]
        for permutation in Permutacion(numeros_restantes):
            permutaciones.append([numero_recorrido] + permutation)
    return permutaciones
    
permutaciones = Permutacion([1, 2, 3])
for p in permutaciones:
    print(p)

print(len(permutaciones))

#PERMUTACION CON REPETICION

def Permutacion_con_Repeticion(n, lst):
    if n == 0:
        return [[]]
    result = []
    for item in lst:
        for permutation in Permutacion_con_Repeticion(n-1, lst):
            result.append([item] + permutation)
    return result
n = 3
lst = [1,2,3]
permutations = Permutacion_con_Repeticion(n, lst)
for p in permutations:

    print(p)
print("El numero de combinaciones posibles en este caso son", len(permutations))


#VARIACION CON REPETICION

def variation_with_repetition(m, n):
    count = 0
    result = [0] * n
    def backtrack(i=0):
        nonlocal count
        if i == n:
            count += 1
            print(count, result)
            return
        for j in range(m):
            result[i] = j
            backtrack(i+1)
    backtrack()
    def formula(m,n):
        return m**n
    print("Las variaciones que pueden salir de aqui son", formula(5,3))

variation_with_repetition(5,3)

#VARIACION SIN REPETICION

def variacion_ordenada(n, k):
    count = 0
    result = []
    def backtrack(first=1):
        nonlocal count
        if len(result) == k:
            count += 1
            print(count, result)
            return
        for i in range(first, n+1):
            result.append(i)
            backtrack(i+1)
            result.pop()
    backtrack()
    
    def formula(m, n):
        resultado = 1
        for i in range(m, m-n, -1):
            resultado *= i
        return resultado
    print("Las variaciones en este caso serian ",formula(5,3))


variacion_ordenada(5,3)

#Combinacion Ordinaria 
def combinations(n, k):
    if k > n:
        return
    comb = []
    def backtrack(first=1):
        if len(comb) == k:
            yield comb.copy()
            return
        for i in range(first, n+1):
            comb.append(i)
            yield from backtrack(i+1)
            comb.pop()
    count = 0
    for c in backtrack():
        count += 1
        print(count, c)
    print("Numero de combinaciones ", count) 
