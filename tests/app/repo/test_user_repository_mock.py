from src.app.repo.user_repository_mock import UserRepositoryMock

class Test_UserRepoMock:
    
    def test_get_first_user(self):
        
        repo = UserRepositoryMock()
        
        user = repo.get_first_user()
        
        assert user is not None
        
        assert user.name == "Vitor Soller"
        assert user.current_balance == 1000.0