from abc import ABC, abstractmethod

from ..entities.user import User

class IUserRepository(ABC):
    
    @abstractmethod
    def get_first_user(self) -> User:
        """Retorna o primeiro usuário da lista do mock, não recebe parâmetros"""
        pass