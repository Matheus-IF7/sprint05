# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY src/api /app

# Expor a porta 8000
EXPOSE 8000

# Comando para iniciar a API
CMD ["uvicorn", "main:main", "--host", "0.0.0.0", "--port", "8000"]
