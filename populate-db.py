from db import DB
import pandas as pd
import os

db = DB(host="localhost", port=5432, database="postgres", user="postgres", password="postgres")

# Seu código de processamento
for file in os.listdir("02-silver-validated"):
    df = pd.read_parquet(f"02-silver-validated/{file}")

    db.create_table(
        file.replace(".parquet", ""),
        df.columns.to_list()
    )

    db.insert_data(
        file.replace(".parquet", ""),
        df
    )

# 💡 CORREÇÃO CRÍTICA: Salvar as alterações
db.commit() # Ou o nome do método que sua classe DB usa
# Opcional: fechar a conexão se ela não foi fechada automaticamente
db.close() 

print("Todos os dados foram processados e salvos no PostgreSQL.")