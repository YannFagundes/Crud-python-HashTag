import mysql.connector

# IMPORTANDO MY SQL 

conection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345', #Altere conforme seu acesso
    database='bdhashtag'
) # ABRINDO CONECÇÃO EM LOCAL HOST

controler = conection.cursor() # Controler ele que irá realizar as ações com o banco de dados


#  REALIZANDO CRUD


# PARA TESTAR, RETIRE DE DENTRO DA FUNÇÃO E APLIQUE OS DADOS OU USE COMO FUNÇÃO MESMO.


# CREATE
def create_fluxo (nome_transação, valor_transação, categoria, destinatario, parcelas):
    # RECEBE ESSES DADOS nome_transação, valor_transação, categoria, destinatario, parcelas
    # command = é onde faz o insert no banco de dados
    # controler executa o comando
    # USAR O COMMIT PARA COMANDOS QUE ESTÃO EDITANDO


    nome_transação = nome_transação
    valor_transação = valor_transação
    categoria = categoria
    destinatario = destinatario
    parcelas = parcelas
    command = f'INSERT INTO fluxodecaixa (nome_transação, valor_transação, categoria, destinatario, parcelas) VALUES ("{nome_transação}",{valor_transação},"{categoria}","{destinatario}",{parcelas}) '
    controler.execute(command)
    conection.commit()

def read_fluxo():
    # READ
    # LISTAR TODA LISTA DE FLUXO
    # command = é onde faz o SELECT no banco de dados
    # controler = executa o comando
    # RESULTADO = ELE USA FETCHALL PARA EXTRAIR OS DADOS (JOGANDO DENTRO DA FUNÇÃO)
    command = f'SELECT * FROM bdhashtag.fluxodecaixa'
    controler.execute(command)
    resultado = controler.fetchall()
    print(resultado)

# UPDATE
def update ():
  # ALTERANDO ALGO DADO OU DADOS
  # command = é onde faz o SELECT no banco de dados
  # controler = executa o comando
  # conection.commit() aplica no banco de dados a alteração
  valor = 10
  nome_transação = "Corte Cabelo"
  comand = f'UPDATE fluxodecaixa SET valor_transação = {valor} WHERE nome_transação = "{nome_transação}"'
  controler.execute(comand)
  conection.commit()
# DELETAR
def delete ():
    # Deletando os dados conforme aplicado
    # command = é onde faz o SELECT no banco de dados
    # controler = executa o comando
    # conection.commit() aplica no banco de dados a alteração
    nome_transação = "Corte Cabelo"
    comand = f'DELETE FROM fluxodecaixa WHERE nome_transação = "{nome_transação}"'
    controler.execute(comand)
    conection.commit()








# saindo da conecção
controler.close()
conection.close()