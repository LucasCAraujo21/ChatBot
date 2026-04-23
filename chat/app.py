from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import json
from CRUD.service import *
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

#Contvectorizer é uma classe da biblioteca sklearn que tranforma textos do vocabulario em vetores numéricos
#MultinomialNB classifica os textos com base na frequencia das palavras. Aprende com a contagem das palavras vetorizadas e as probabilidades aprendidas

#Dados de treinamento
perguntas = pd.read_csv("perguntas.csv")

categorias = perguntas['categoria'].astype(str).tolist()
frases = perguntas['frase'].astype(str).tolist()

#vetorização e treinamento
vetorizador = CountVectorizer()
X = vetorizador.fit_transform(frases)
#vetorizador vai guardar um objeto que será usado para transformar texto em numeros
#X guarda o resultado da transformação das frases em vetores numericos
#fit_transform é um metodo da classe CountVectorizer que aprende o vocabulario das frases e trans1forma em vetor

modelo = MultinomialNB()
modelo.fit(X,categorias)
#modelo vai guardar o modelo criado
#modelo.fit é um algoritimo que treina os exemplos das frases que passamos para ele

#RESPOSTAS

with open("respostas.json", "r", encoding="utf-8") as arquivo:
    respostas = json.load(arquivo)
    
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
                cliente = buscar(cpf)
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


"""while True:
  pergunta = input("\nVocê: ")
  if pergunta.lower() == 'sair':
    print("Encerrando atendimento.")
    break

  pergunta_vetorizada = vetorizador.transform([pergunta])
  #pergunta_vetorizada - transforma a pergunta digitada em uma forma numerica que o modelo consiga entender
  #vetorizador é o objeto CountVetorizer(), que foi treinado antes com as frases do dataset

  categoria_prevista = modelo.predict(pergunta_vetorizada)[0]
  #modelo.predict(): analiza o vetor da pergunta e decide a qual categoria ela pertence(começa desde o inicio)

  probabilidades = modelo.predict_proba(pergunta_vetorizada)[0]
  #modelo.predict_proba(): calcula as probabilidades de pertencimento a cada categoria

  maior_probabilidade = max(probabilidades)
  #guarda a maior probabilidade de resposta escolhida pelo modelo

  if maior_probabilidade < 0.40: #menor que 40%
    print("Não entendi a pergunta.")
  else:
    print("Categoria identificada:", categoria_prevista)
    print("Probabilidade:", round(maior_probabilidade*100,2),"%")
    print("chatbot:", respostas[categoria_prevista.lower()])"""