from inference import app

# Se quiser adicionar outras funcionalidades no futuro, pode colocar aqui
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)