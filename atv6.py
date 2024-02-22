from fastapi import FastAPI, Query, HTTPException
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

@app.get("/data-hora")
def obter_data_hora():
    return {"data_hora": datetime.now().isoformat()}

@app.get("/converter-moeda")
def converter_moeda(valor: float = Query(..., description="Quantidade a ser convertida"),
                    moeda_origem: str = Query(..., description="Moeda de origem"),
                    moeda_destino: str = Query(..., description="Moeda de destino")):
    taxa_conversao = 5 # converção de real para dólar
    valor_convertido = valor * taxa_conversao
    return {"valor_convertido": valor_convertido, "moeda_destino": moeda_destino}

class Usuario(BaseModel):
    nome: str
    email: str
usuarios_db = [] # simula um banco de dados de usuários 

@app.put("/usuarios/{usuario_id}")
def adicionar_usuario(usuario_id: int, usuario: Usuario):
    usuarios_db.append({"usuario_id": usuario_id, "nome": usuario.nome, "email": usuario.email})
    return {"mensagem": f"Usuário {usuario.nome} adicionado com sucesso"}

@app.get("/usuario/{usuario_id}")
def obter_info_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario["usuario_id"] == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado") # caso o usuário não seja encontrado

@app.get("/Oiii")
def saudacao(nome: str = "Visitante"):
    return {"mensagem": f"Olá, {nome}! Bem-vindo à API."}
