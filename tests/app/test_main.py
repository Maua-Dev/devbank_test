from fastapi.exceptions import HTTPException
import pytest
import src.app.main as main_module
from src.app.main import execute_get_pra_barra
from src.app.repo.item_repository_mock import ItemRepositoryMock


class Test_Main:

    def setup_method(self):
        # Reset do repositorio global usado em src.app.main a cada teste
        main_module.repo = ItemRepositoryMock()
        
    def test_rota_barra(self):
        
        repo = ItemRepositoryMock()
        response = execute_get_pra_barra()
        assert response.get("name", None) == "Vitor Soller"

   