from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import json
import sqlite3
from CRUD.crud import buscar_cliente_por_cpf
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
    
estado_usuario = {
    "aguardando_cpf": False
}

def responder(pergunta):
    global estado_usuario   
    
# 🔹 Se estiver esperando CPF
    if estado_usuario["aguardando_cpf"]:
        cpf = pergunta.strip()

        conexao = sqlite3.connect("cartao.db")
        cliente = buscar_cliente_por_cpf(conexao, cpf)
        conexao.close()

        estado_usuario["aguardando_cpf"] = False

        if cliente:
            nome, limite, fatura = cliente
            return f"{nome}, seu limite é R$ {limite}"
        else:
            return "CPF não encontrado."

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
        return "Não entendi a pergunta."
        
    # 🔥 se precisar de CPF
    if categoria_prevista.lower() == "limite":
        estado_usuario["aguardando_cpf"] = True
        return "Por favor, informe seu CPF."

    #RESPOSTA GENÉRICA
    return respostas.get(categoria_prevista.lower(), "Resposta não encontrada.")