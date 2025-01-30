class AuthController:
    def __init__(self,user_model):
        self.user_model=user_model
        self.current_user=None




    def signup(self,username:str,password:str,email:str = None)-> dict:
        if not username or not password:
            return {'message':'Invalid username or password'}
        
        if self.user_model.add_user(username,password,email):
            return {'message':'User created successfully'}
        else:
            return {'message':'User already exists'}

    def login(self,username:str,password:str)-> dict:
        if self.user_model.authenticate(username,password):
            self.current_user=self.user_model.get_user(username)
            return {'success': True, 'user': self.current_user}
        return {'success': False, 'error': 'Invalid username or password'}
    
    def logout(self):
        self.current_user=None