#2
'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary 
representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

#A conversão para binário se dá dividindo o número pela base(2) e analisar o resto das operações, de forma que o código binário será invertido:

inp=int(input('Escreva um número inteiro positivo '))
bina=[]
while inp>2:
  bina.append(inp%2)
  inp= int(inp/2)
bina.append(inp%2)
bina.reverse()
print(str(bina).strip('[]'))
