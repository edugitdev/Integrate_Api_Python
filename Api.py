import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-Q3JLRD9\SQLSERVER2023;"
    "Database=GrammysDB;"
)

conexao = pyodbc.connect(dados_conexao)
print('conexão realizada com sucesso')

cursor = conexao.cursor()

comando = """ SELECT*  FROM Person.Person """;


cursor.execute('''
  SELECT artist, MAX(sales) AS ARTISTA_MAIOR_FATURAMENTO
FROM [money-makers-bb]
GROUP BY artist
ORDER BY ARTISTA_MAIOR_FATURAMENTO DESC
''')

# Recuperar os resultados
resultados = cursor.fetchall()

# Imprimir os resultados
for item, visualizacoes in resultados:
    print(f'Item: {item}, Maior_Faturamento: {visualizacoes}')

# Fechar a conexão com o banco de dados
conexao.close()
