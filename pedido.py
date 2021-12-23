

class Pedido:

    def __init__(self, pizza : str, tamanho: str, quantidade : int):

        self.pizza = pizza
        self.tamanho = tamanho
        self.quantidade = quantidade

    def getPizza (self):

        return self.pizza
    
    def setPizza (self, pizza : str):

        self.pizza = pizza
    

    def getTamanho (self):

      return self.tamanho

    def setTamanho (self, tamanho : str):

        self.tamanho = tamanho

    def getPreco (self):

        return self.preco
    
    def setPreco (self, preco: float):

        self.preco = preco

    def getQuantidade (self):

       return self.quantidade
    
    def setQuantidade (self, quantidade : int):

        self.quantidade = quantidade

    
    
    def calcularPrecoTotal (self):

        if (self.getTamanho().__eq__("P")) :

                self.setPreco(15.00)
        
        elif (self.getTamanho().__eq__("M")):

               self.setPreco(30.00)
        
        elif (self.getTamanho().__eq__("G")):

              self.setPreco(60.00)
              
        
        return self.getPreco() * self.getQuantidade()

    