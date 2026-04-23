from conexao import conectar

conexao = conectar() #faz a conexão
cursor = conexao.cursor() #permite usar comandos sql

cursor.execute("""
              CREATE TABLE IF NOT EXISTS cliente
              (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                num_cartao INTEGER NOT NULL,
                num_agencia INTEGER NOT NULL,
                valor_fatura REAL NOT NULL,
                limite INTEGER REAL NULL,
                vencimento_fatura TEXT NOT NULL,
                vencimento_cartao TEXT NOT NULL,
                status INTEGER NOT NULL                
              )
""")
conexao.commit()
conexao.close() #fecha o banco