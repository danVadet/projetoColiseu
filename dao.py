

from pedido import  Pedido

class DAO:

    def  create (nomePizza : str, tamanho : str, quantidade : int):

        return Pedido(nomePizza, tamanho, quantidade)

    
    def delete(pedidos):

        idPedido = int (input ("\n Determine o id do pedido a ser removido: "))
          
        for p in range ( len (pedidos)):

           p =  idPedido 

        pedidos.pop(idPedido)
                  
        print (" PEDIDO REMOVIDO COM SUCESSO!")

    
    def search (pedidos):

        idPedido = int (input (" Determine o id do pedido a ser procurado: "))

        contador = 0

        for pedido in pedidos:

            contador = contador + 1

            if ((contador - 1).__eq__(idPedido)):

        
                print ("\n  ------------ PEDIDO %d ------------ \n \n"
                " PIZZA: %s  \n"
                " TAMANHO: %s \n \n"
                " QUANTIDADE: %d\n"
                "      TOTAL: R$ %.2f \n \n"
                "  ------------------------------------------" % (idPedido, pedido.getPizza(), pedido.getTamanho(), pedido.getQuantidade(), pedido.calcularPrecoTotal ()))
            

    def listAll (pedidos: list):

            contador = 0
         
            for pedido in pedidos:

                contador = contador + 1

    
                print ("\n  ------------ PEDIDO %d ------------ \n \n"
                " PIZZA: %s  \n"
                " TAMANHO: %s \n \n"
                " QUANTIDADE: %d \n"
                "            TOTAL: R$ %.2f \n"
                "  -------------------------------" % ((contador - 1), pedido.getPizza(), pedido.getTamanho(), pedido.getQuantidade (), pedido.calcularPrecoTotal ()))
     