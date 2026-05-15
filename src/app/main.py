from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.item import Item


app = FastAPI()

user_repo = Environments.get_user_repo()()

# a baixo estão as rotas da api
# elas interagem com os métodos de repositório. por exemplo a rota create item chama, não exclusivamente,
# o método repo.create_item() para criar o item no nosso repositório

@app.get("/")
def execute_get_pra_barra():
    
    return user_repo.get_first_user().__dict__
    
handler = Mangum(app, lifespan="off")
