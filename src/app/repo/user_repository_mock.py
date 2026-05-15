

from src.app.entities.user import User
from .user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    
    def __init__(self) -> None:
        
        """Lista que simula o banco de dados"""
        
        self._users: list[User] = [
            User(
                name = "Vitor Soller",
                agency="3333",
                account="00000-1",
                current_balance=1000.0
            ),
            User(
                name = "Leo Lorio",
                agency="3333",
                account="00000-2",
                current_balance=500.0
            )
        ]
        
    def get_first_user(self) -> User:
        
        return self._users[0]