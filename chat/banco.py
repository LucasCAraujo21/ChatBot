from CRUD.service import *
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))    

def input_cliente():
    return {
        "nome": input("Nome: "),
        "cpf": input("CPF: "),
        "num_cartao": input("Cartão: "),
        "num_agencia": input("Agência: "),
        "valor_fatura": float(input("Fatura: ")),
        "limite": float(input("Limite: ")),
        "vencimento_fatura": input("Vencimento fatura: "),
        "vencimento_cartao": input("Vencimento cartão: "),
        "status": input("Status: ")
    }

def menu():
    #começa o chat
    print("="*40)
    print("CHATBOT - OPERADORA DE CARTÃO")
    print("="*40)

    while True:
        print("\n1 - Inserir")
        print("2 - Listar")
        print("3 - Buscar por CPF")
        print("4 - Atualizar")
        print("5 - Deletar")
        print("0 - Sair")

        opcao = input("Escolha: ")

        try:
            if opcao == "1":
                cliente = input_cliente()
                cadastrar_cliente(cliente)
                print("Inserido com sucesso!")

            elif opcao == "2":
                clientes = listar()
                for c in clientes:
                    print(c)

            elif opcao == "3":
                cpf = input("CPF: ")
                cliente = buscar(conexao, cpf)
                print(cliente or "Não encontrado")

            elif opcao == "4":
                cpf = input("CPF do cliente a atualizar: ")
                dados = input_cliente()
                atualizar(cpf, dados)
                print("Atualizado com sucesso!")

            elif opcao == "5":
                cpf = input("CPF: ")
                deletar(cpf)
                print("Deletado com sucesso!")

            elif opcao == "0":
                break

            else:
                print("Opção inválida")

        except Exception as e:
            print(f"Erro: {e}")

    conexao.close()
    
menu()