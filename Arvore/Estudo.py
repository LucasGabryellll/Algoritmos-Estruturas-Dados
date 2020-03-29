class No():
    def __init__(self, elemento):
        self.elemento = elemento
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.elemento)

class Arvore():
    def __init__(self):
        self.raiz = None
        self.__quantFolhas = 0

    def add(self, elemento):
        no = No(elemento)
        if self.treeVaria():
            self.raiz = no
        else:
            perc = self.raiz
            while True:
                if no.elemento > perc.elemento:
                    if perc.direita != None:
                        perc = perc.direita
                    else:
                        perc.direita = no
                        break
                elif no.elemento < perc.elemento:
                    if perc.esquerda != None:
                        perc = perc.esquerda
                    else:
                        perc.esquerda = no
                        break
                else:
                    Exception("ELEMENTO JA ADICIONADO")
        self.__quantFolhas +=1

    def treeVaria(self):
        if self.raiz == None:
            return True
        return False

    def imprimirNo(self, no):
        if no != None:
            self.imprimirNo(no.esquerda)
            print(no)
            self.imprimirNo(no.direita)
    def imprimir(self):
        return self.imprimirNo(self.raiz)

    def buscarElemento(self, elemento):
        perc = self.raiz
        if self.treeVaria():
            return ("ÁRVORE VAZIA")
        else:
            while perc != elemento:
                if elemento > perc.elemento:
                    perc = perc.direita
                elif elemento < perc.elemento:
                    perc = perc.esquerda
                else:
                    return perc

    def getMax(self, raiz):
        if self.treeVaria():
            return ValueError("ÁRVORE NÃO TEM ELEMENTOS")
        perc = raiz
        while perc.direita != None:
            perc = perc.direita
        return perc

    def getMin(self, raiz):
        if self.treeVaria():
            return ValueError("ÁRVORE NÃO TEM ELEMENTOS")
        perc = raiz
        while perc.esquerda != None:
            perc = perc.esquerda
        return perc

    def sucessor(self):
        if self.raiz.direita != None:
            return self.getMin(self.raiz.direita)

    def predecessor(self):
        if self.raiz.direita != None:
            return self.getMax(self.raiz.esquerda)

    def remover(self, elemento):
        if self.treeVaria():
            raise ValueError("ÁRVORE VAZIA")
        perc = self.raiz
        pai = self.raiz
        filho_esquerdo = True
        while perc.elemento != elemento:
            pai = perc
            if elemento < perc.elemento:
                perc = perc.esquerda
                filho_esquerdo = True
            else:
                perc = perc.direita
                filho_esquerdo = False
            if perc == None:
                return False
        if perc.esquerda is None and perc.direita is None:
            if perc == self.raiz:
                self.raiz = None
            else:
                if filho_esquerdo:
                    pai.esquerda = None
                else:
                    pai.direita = None
        elif perc.direita == None:
            if perc == self.raiz:
                self.raiz = perc.esquerda
            else:
                if filho_esquerdo:
                    pai.esquerda = perc.esquerda
                else:
                    pai.direita = perc.esquerda
        elif perc.esquerda == None:
            if self.raiz == perc:
                self.raiz = perc.direita
            else:
                if filho_esquerdo:
                    pai.esquerda = perc.direita
                else:
                    pai.direita = perc.direita
        else:
            sucessor = self.sucessor(perc)

            if perc == self.raiz:
                self.raiz = sucessor
            else:
                if filho_esquerdo:
                    pai.esquerda = sucessor
                else:
                    pai.direita = sucessor
            sucessor.esquerda = perc.esquerda
        self.__quantFolhas -= 1
        return True

    def totalElementos(self):
        return self.__quantFolhas

    def somatorio(self, perc):
        if perc == None:
            return 0
        else:
            return self.somatorio(perc.esquerda) + self.somatorio(perc.direita) + perc.elemento
    def soma(self):
        return (self.somatorio(self.raiz))

    def altura(self, perc):
        if self.treeVaria():
            return 0
        if perc == None or perc.esquerda == None and perc.direita == None:
            return 1
        else:
            if self.altura(perc.esquerda) > self.altura(perc.direita):
                return 1 + self.altura(perc.esquerda)
            else:
                return 1 + self.altura(perc.direita)
    def alturaTree(self):
        return self.altura(self.raiz)

    def niveisTree(self):
        if self.raiz == None:
            return ("ARVORE NÃO CONTÉM ELEMENTOS")
        perc = self.raiz
        if self.raiz != None and perc.esquerda == None and perc.direita == None:
            return 0
        elif perc.esquerda != None and perc.direita == None:
            contE = 0
            while perc.esquerda != None:
                perc = perc.esquerda
                contE += 1
            return contE
        elif  perc.esquerda == None and perc.direita != None:
            contD = 0
            while perc.direita != None:
                perc = perc.direita
                contD += 1
            return contD
        else:
            contE, contD = 0, 0
            while perc.esquerda != None:
                perc = perc.esquerda
                contE += 1
                break
            perc = self.raiz
            while perc.direita != None:
                perc = perc.direita
                contD += 1
            if contE > contD:
                return contE
            else:
                return contD

    def elemDoNivel(self, nivel):
        if nivel == 0:
            return self.raiz
        perc = self.raiz
        if nivel == 1 and perc.esquerda != None and perc.direita != None:
            return perc.esquerda.elemento, perc.direita.elemento
        elif nivel == 1 and perc.esquerda != None and perc.direita == None:
            return perc.esquerda.elemento , None
        elif nivel == 1 and perc.esquerda == None and perc.direita != None:
            return None, perc.direita.elemento
        cont = 0
        paiE = self.raiz
        paiD = self.raiz
        if nivel > 1:
            while cont != nivel - 1:
                if perc.esquerda != None and perc.direita != None:
                    paiE = paiE.esquerda
                    paiD = paiD.direita
                    cont += 1

            return paiE.esquerda, paiE.direita, paiD.esquerda, paiD.direita
        #Está incompleto!

    def balanco(self):
        pass