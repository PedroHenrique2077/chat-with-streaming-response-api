from fastapi import FastAPI
from chat.controller import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() # cria a instância

#  Define a lista de origens (origins) que são permitidas acessar o aplicativo
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui o roteador router no aplicativo app. 
app.include_router(router)