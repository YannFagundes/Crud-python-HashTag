# APLICANDO CRUD CONFORME ORIENTAÇÃO CURSO DA HASHTAG

Com essa database foi realizado um controle de fluxo de caixa para executar um simples C.R.U.D.

# CREATE - READ - UPDATE - DELETE 

*CREATE* Apliquei direto no banco uma transação de um gasto, que está descrito com a função *CREATE_TRANSAÇÃO* recebendo os seguintes parametros: nome_transação, valor_transação, categoria, destinatario, parcelas. 

*READ* Aplicado apenas um SELECT ALL mas pode ser facilmente modificado conforme a necessidade

*UPDATE* Aplicado a busca no banco de dados uma transação que tenha o nome CORTE CABELO que fará a ALTERAÇÃO no valor de todas com esse nome.

*DELETE* Aplicado a busca no banco de dados uma transação que tenha o nome CORTE CABELO que deletará todos com esse nome


# Durante a criação de uma tabelo caso for fazer uma modificação ou leitura de um dado.

*LEMBRE-SE* 

USAR O COMMIT PARA COMANDOS QUE ESTÃO EDITANDO 

USAR FETCHALL PARA LEITURA DE UM DADO 


Dentro do arquivo database tem comentarios importantes para melhor compreensão.