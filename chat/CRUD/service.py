from CRUD.crud import *

conexao = conectar() #faz a conexão
cursor = conexao.cursor() #permite usar comandos sql

def validar_cliente(cliente):
    if not cliente["nome"]:
        raise ValueError("Nome obrigatório")
    if len(cliente["cpf"]) != 11:
        raise ValueError("CPF inválido")
    if cliente["limite"] < 0:
        raise ValueError("Limite inválido")


def cadastrar_cliente(cliente):
    validar_cliente(cliente)
    inserir_cliente(cliente)


def listar():
    return selectAll()


def buscar(cpf):
    return buscar_cliente_por_cpf(cpf)


def atualizar(cpf, dados):
    validar_cliente(dados)
    atualizar_cliente(cpf, dados)


def deletar(cpf):
    deletar_cliente(cpf)