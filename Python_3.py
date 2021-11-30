#3
'''In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins? '''
#temos uma equação com 5 variáveis: a + b5 +c20 + d50 + e100 =200
#sendo este um problema de análise combinatória, e considerando que é possível 0 moedas de 4 tipos de moedas,
#basta decidir quantas vezes cada moeda equivale em valor a 200p, e multiplicar estes valores:

#vamos supor pelo formato a convvenção de estruturar os dados em listas
form = [1]+[0]*200
for i in [1, 2, 5, 10, 20, 50, 100, 200]:
  
  hrz= len(form)
  for j in range(hrz-i):
    form[j + i]=form[j+i]+form[j]
print(str(form[-1]))
