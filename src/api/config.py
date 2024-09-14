import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
RDS_ENDPOINT = os.getenv("RDS_ENDPOINT")

if not S3_BUCKET_NAME or not RDS_ENDPOINT:
    raise ValueError("Variáveis de ambiente S3_BUCKET_NAME e RDS_ENDPOINT são obrigatórias.")
