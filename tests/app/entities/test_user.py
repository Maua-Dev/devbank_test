from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated
import pytest

class Test_User:
    
    def test_user(self):
        
        user = User(
            name="Leo",
            agency="1234",
            account="00000-1",
            current_balance=1000.0
        )
        
        assert user.name == "Leo"
        assert user.agency == "1234"
        
    def test_invalid_name(self):
        
        with pytest.raises(ParamNotValidated):
            
            User(
                name="ab",
                agency="1234",
                account="12345-6",
                current_balance=1000.0
            )
            
    def test_invalid_current_balance(self):
        
        with pytest.raises(ParamNotValidated):
            
            User(
                name="leo",
                agency="1234",
                account="12345-6",
                current_balance=-1000
            )
        