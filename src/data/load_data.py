import pandas as pd
import os

# Caminhos dos arquivos
RAW_DATA_PATH = os.path.join('data', 'raw', 'Hotel_Reservations.csv')
PROCESSED_DATA_PATH = os.path.join('data', 'processed', 'processed_data.csv')

def load_raw_data():
    """Carrega os dados brutos do arquivo CSV."""
    return pd.read_csv(RAW_DATA_PATH)

def preprocess_data(df):
    """Realiza o pré-processamento dos dados."""
    # Exemplo de pré-processamento
    df['label_avg_price_per_room'] = df['avg_price_per_room'].apply(lambda x: 1 if x <= 85 else (2 if x < 115 else 3))
    df = df.drop(columns=['avg_price_per_room'])
    return df

def save_processed_data(df):
    """Salva os dados processados em um arquivo CSV."""
    df.to_csv(PROCESSED_DATA_PATH, index=False)

if __name__ == "__main__":
    # Carrega os dados brutos
    raw_data = load_raw_data()
    
    # Processa os dados
    processed_data = preprocess_data(raw_data)
    
    # Salva os dados processados
    save_processed_data(processed_data)