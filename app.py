

from dao import DAO
from pedido import Pedido

# Lista dos pedidos
pedidos = []


# Adicionar pedido da pizza
def adicionarPedido ():
    

    # Entrada de dados
    nomePizza = str (input ("\n  Pizza:  "))
    tamanho = str (input ("\n Tamanho:  "))
    quantidade = int  (input ("\n  Quantidade:  "))

    
    # Lista adicionando cada um item ao pedido.
    pedidos.append(DAO.create(nomePizza, tamanho, quantidade))

# Remover o pedido por id.
def removerPedido():

    DAO.delete(pedidos)

# Pesquisar o pedido por id
def pesquisarPedido():

    DAO.search(pedidos)

    

# Exibir todos os pedidos
def exibirPedidos ():

    if not (len (pedidos).__eq__(0)):

        procurado = True
           
        DAO.listAll(pedidos)
        
    else:

        print (" NÃO HÁ LISTA DOS PEDIDOS!")      


# Retornar o menu principal

retorno = True

while retorno:

    print ("\n   ------------- COLISEU PIZZARIA ----------------- \n \n"
    
     "  --------  ----------  PREÇOS  ---------- ------------ \n"
    
    "\n         | PIZZA (P) COM 4 FATIAS - R$ 15.00 | \n"
    "\n         | PIZZA (M) COM 6 FATIAS - R$ 30.00 | \n"
    "\n         | PIZZA (G) COM 8 FATIAS - R$ 60.00 | \n \n \n"

    "  ---------   -----------  MENU PRINCIPAL  ---------   ------------------ \n \n"

    " 1 - ADICIONAR O PEDIDO \n"
    " 2 - REMOVER O PEDIDO POR CÓDIGO \n"
    " 3 - PESQUISAR O PEDIDO POR CÓDIGO \n"
    " 4 - EXIBIR TODOS OS PEDIDOS \n"
    " 0 - FINALIZAR O PROGRMA \n \n"

    "  ------------ ----------------- ------------------\n")

    opcao = int (input ("\n Digite a opção:  "))


    if (opcao.__eq__(1)):

        adicionarPedido()
        
        while True:

            add = str (input("\n Prazerado (a), digite o ADD (adicionar mais de um pedido) ou F (finalizar o pedido): ")).upper()
        
        
            if (add.__eq__("ADD")):

                adicionarPedido()

                continue

            elif (add.__eq__("F")):

                exibirPedidos()


                print ("\n PEDIDO FINALIZADO COM SUCESSO!")

            break
    
    elif (opcao.__eq__(2)):

        exibirPedidos ()
        removerPedido()
        exibirPedidos()

    elif (opcao.__eq__(3)):

        pesquisarPedido()

        

    elif (opcao.__eq__(4)):

        exibirPedidos ()
        
    
    elif (opcao.__eq__(0)):

        retorno = False

        print ("\n PROGRAMA FINALIZADO! \n \n")
   
    else:

        print ("\n DIGITE A OPÇÃO VÁLIDA NOVAMENTE.... \n \n")
    

input ("")