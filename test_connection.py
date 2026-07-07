import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

def testar_conexao():
    try:
        # Tenta conectar usando as variáveis de ambiente
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        print("✅ Sucesso! Conexão estabelecida com o banco de dados.")
        conn.close()
    except Exception as e:
        print("❌ Falha na conexão. Erro:")
        print(e)

if __name__ == "__main__":
    testar_conexao()
    