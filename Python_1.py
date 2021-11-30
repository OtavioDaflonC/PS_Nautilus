#1
'''
CRIE UMA FUNÇÃO QUE REALIZE TANTO UMA PA  QUANTO UMA PG PARA VALORES INTEIROS
SE A RAZÃO FOR PAR DEVERÁ SER REALIZADA UMA P.A DE TERMO N1 ATÉ UM VALOR X QUE NÃO DEVE SER ULTRAPASSADO
SE O VALOR DA RAZÃO FOR ÍMPAR A FUNÇÃO REALIZARA UMA PG

cada termo tanto da PA quanto da PG devem ser armazenados em uma lista 

exemplo 
n1= 2
nx= 13
razão = 4

output = [2, 6, 10]
'''

n1=int(input('insira o primeio termo '))
nx= int(input('insira o último termo '))
r= int(input('insira a razão '))
#pa : nx=n1 + (n -1)r, logo n= (nx - n1)/(r) + 1 mas não será necessário
#pg : nx= n1*r^(n-1), logo n=(log(nx/n1)-log(r)+1) mas não será necessário

out=[]
if r%2 ==0:
#nesse caso seria par
  n=int(((nx - n1)/r) +1)

  for num in range(n1,nx+1,r):
    
    out.append(num) 
else:
#nesse caso seria ímpar
# é necessário apenas seguir em um range que eu tenha certeza que sempre será maior
# que o numero de valores n necessários, programando em seguida condições para interromper corretamente 
# a formação da lista:
  for n in range(1,nx+1):
    num= n1*r**(n-1)
    out.append(num)
    if num == nx:
      break
    if num > nx:
      out.remove(num)
 
      break 

print(out)
