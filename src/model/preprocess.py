import pandas as pd

def preprocess_data(df):
    """Realiza o pré-processamento dos dados."""
    # Exemplo de pré-processamento
    df['label_avg_price_per_room'] = df['avg_price_per_room'].apply(lambda x: 1 if x <= 85 else (2 if x < 115 else 3))
    df = df.drop(columns=['avg_price_per_room'])
    return df
