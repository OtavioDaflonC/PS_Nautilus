#4
'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''
soma=0
for i in range(1,1000):
  
  soma = soma + (i**i)
  

res=str(soma)
print(res[-11:-1])
# [-11:-1] representa o index dos últimos 10 números. Sendo -1 o último, -2 o penúltimo, e assim por diante.

# 1911084670 = resposta certa
