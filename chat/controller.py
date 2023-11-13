from fastapi import APIRouter, Request # Importa as classes APIRouter e Request do FastAPI, que são usadas para criar rotas e lidar com solicitações HTTP.
from chat.service import generate_response
from fastapi.responses import StreamingResponse

router = APIRouter() # Define um roteador chamado router que será usado para agrupar rotas relacionadas.

@router.post("/chat")
async def upload_text(request: Request):
    data = await request.json()
    question = data.get("text", "") # Extrai o valor associado à chave "text" dos dados da solicitação. Se a chave "text" não existir, a variável question recebe uma string vazia.
    return StreamingResponse(generate_response(question), media_type='text/event-stream') # basicamente transmite os dados, pedaço por pedaço usando uma função geradora.