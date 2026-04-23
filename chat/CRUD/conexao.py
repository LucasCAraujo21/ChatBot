import sqlite3

def conectar():
  conexao = sqlite3.connect('cartao.db') #faz a conexão
  return conexao
