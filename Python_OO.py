#OO
class Competidor:
  def __init__(self,nome,pont,idade,nacio,rating,tit,sex):
    self.nome=nome
    self.pont=pont
    self.idade=idade
    self.nacio=nacio
    self.rating=rating
    self.titulo=tit
    self.sexo=sex
  def __gt__(self,outro):
    return self.pont>outro.pont
  def __lt__(self,outro):
    return self.pont<outro.pont
  def __eq__(self,outro):
    return self.pont==outro.pont
  def __ne__ (self,outro):
    return self.pont!=outro.pont
  def __add__(self,outro):
    return self.pont+outro.pont
  def __sub__(self,outro):
    if self.pont<=outro.pont:
      d=outro.pont - self.pont
    else: 
      d= self.pont - outro.pont
    return d
  def __repr__(self):
    if self.sexo== 'feminino':
      r=' Nome: {} \n Pontuação: {} \n Jogadora de {} anos de idade. \n Representando o país {}. \n Com rating de {}, tendo o título de {}. \n '.format(self.nome,self.pont,self.idade,self.nacio,self.rating,self.titulo)
    elif self.sexo== 'masculino':
      r= ' Nome: {} \n Pontuação: {} \n Jogador de {} anos de idade. \n Representando o país {}. \n Com rating de {}, tendo o título de {}. \n '.format(self.nome,self.pont,self.idade,self.nacio,self.rating,self.titulo) 
    else:
      r= ' Nome: {} \n Pontuação: {} \n Jogador não binário de {} anos de idade. \n Representando o país {}. \n Com rating de {}, tendo o título de {}. \n '.format(self.nome,self.pont,self.idade,self.nacio,self.rating,self.titulo)
    return r
#-------------------------------------------------------------------
C1 = Competidor('Julia Martins',5,22,'Australia',1755,'Amador','feminino')
C2 = Competidor('Otávio Daflon',8,22,'Brasil',1810,'Amador','masculino')
C3 = Competidor('Knel Agny',8,30,'Àustria',2000,'Mestre Internacional','não binário')
C4 = Competidor('Beth Harmon',20,23,'Inglaterra',2900,'Grande Mestre','feminino')
C5 = Competidor('Tuco Salamanca',0,39,'Mexico',1504,'Amador','masculino')

listagem=[C1,C2,C3,C4,C5]
listagem.sort()
listagem.reverse()
#vai do menor ao maior, logo é preciso inverter a lista

#------------------------------------------------------------------

#Exemplos:
print(listagem)
print(C2)
print(C3-C4)
print(C1+C2)


#São assim atendidos todos os critérios dos entregáveis.
