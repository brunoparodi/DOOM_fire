echo "# DOOM_fire" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/brunoparodi/DOOM_fire.git
git push -u origin master

from random import randrange
from time import sleep
from os import system

class Fogo():

    def __init__(self, comprimento, altura, intensidade):
        self.comprimento = comprimento
        self.altura = altura
        self.intensidade = intensidade
        self.calor = 36 #define o valor de calor maximo

    def createFire(self):
        fire = []
        for alt in range(self.altura - 1):
            line = []
            fire.append(line)
            for comp in range(self.comprimento):
                line.append(0)
        fire.append([self.calor]*self.comprimento) #insere o calor maximo na base da matrix
        return fire

    def createFlame(self):
        fire = self.createFire()
        altura = (self.altura) * -1
        comprimento = (self.comprimento) * -1
        for alt in range(-2,altura-1,-1):
            for comp in range(0,comprimento,-1):
                if (fire[alt+1][comp+1])-1 < 0: #não deixa o indice ser negativo
                    pass
                else:
                    fire[alt][comp] = (fire[alt+1][comp+1]) - randrange(0,3) #enfraquece a chama conforme for subindo
                #print(alt,comp,fire[alt][comp])
        return fire

    def printFire(self):
        for x in self.createFlame():
            for y in x:
                print(str(y).rjust(3),end="")
            print("\n")


fogo = Fogo(20, 20, 1)
while True:
    system('cls')
    fogo.printFire()
    sleep(1)
#fogo.createFlame()