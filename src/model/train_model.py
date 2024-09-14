import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Caminhos dos arquivos
PROCESSED_DATA_PATH = os.path.join('data', 'processed', 'processed_data.csv')
MODEL_PATH = os.path.join('data', 'models', 'model.joblib')

def load_data():
    """Carrega os dados processados."""
    return pd.read_csv(PROCESSED_DATA_PATH)

def train_model(df):
    """Treina o modelo de machine learning."""
    X = df.drop(columns=['label_avg_price_per_room'])
    y = df['label_avg_price_per_room']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Avaliação do modelo (opcional)
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy}")
    
    return model

def save_model(model):
    """Salva o modelo treinado."""
    joblib.dump(model, MODEL_PATH)

if __name__ == "__main__":
    # Carrega os dados processados
    data = load_data()
    
    # Treina o modelo
    model = train_model(data)
    
    # Salva o modelo treinado
    save_model(model)
