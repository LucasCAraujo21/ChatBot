from CRUD.conexao import conectar

conexao = conectar() #faz a conexão
cursor = conexao.cursor() #permite usar comandos sql

def inserir_cliente(cliente):
    cursor.execute('''
        INSERT INTO cliente 
        (nome, cpf, num_cartao, num_agencia, valor_fatura, limite, vencimento_fatura, vencimento_cartao, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', tuple(cliente.values()))
    conexao.commit()


def selectAll():
    cursor.execute('SELECT * FROM cliente')
    return cursor.fetchall() #traz os dados do banco

"""    for nomes in dados:
        return print(nomes)"""

def buscar_cliente_por_cpf(conexao, cpf):
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, limite, valor_fatura FROM cliente WHERE cpf = ?", (cpf,))
    return cursor.fetchone()


def atualizar_cliente(cpf, novos_dados):
    cursor.execute('''
        UPDATE cliente SET 
        nome = ?, num_cartao = ?, num_agencia = ?, valor_fatura = ?, 
        limite = ?, vencimento_fatura = ?, vencimento_cartao = ?, status = ?
        WHERE cpf = ?
    ''', (
        novos_dados["nome"],
        novos_dados["num_cartao"],
        novos_dados["num_agencia"],
        novos_dados["valor_fatura"],
        novos_dados["limite"],
        novos_dados["vencimento_fatura"],
        novos_dados["vencimento_cartao"],
        novos_dados["status"],
        cpf
    ))
    conexao.commit()

def deletar_cliente(cpf):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM cliente WHERE cpf = ?", (cpf,))
    conexao.commit()

