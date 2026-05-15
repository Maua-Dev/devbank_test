
from ast import Param
from locale import currency
from ..errors.entity_errors import ParamNotValidated

from abc import abstractmethod


class User:
    
    name: str
    agency: str
    account: str
    current_balance: float
    
    def __init__(
        self,
        name: str,
        agency: str,
        account: str,
        current_balance: float
    ): 
        
        self.validate_name(
            name=name
        )
        self.name = name
        
        self.agency = agency
        self.account = account
        
        self.validate_current_balance(
            current_balance=current_balance
        )
        self.current_balance = current_balance
        
    @abstractmethod
    def validate_name(
        self,
        name: str
    ) -> None:
        
        if type(name) != str:
            
            raise ParamNotValidated(
                param="name",
                message="Nome precisa ser uma string"
            )
        
        if len(name) < 3 or len(name) > 40:
            
            raise ParamNotValidated(
                param="name",
                message="Nome não pode ser menor que 3 nem maior que 40 caracteres"
            )
            
    @abstractmethod
    def validate_current_balance(
        self,
        current_balance
    ): 
        
        if type(current_balance) != float:
            
            raise ParamNotValidated(
                param="current_balance",
                message="current_balance precisa ser do tipo float"
            )
        
        if current_balance < 0:
            
            raise ParamNotValidated(
                param="current_balance",
                message="Saldo não pode ser negativo!"
            )
            
    