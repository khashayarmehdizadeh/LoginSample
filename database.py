import sqlite3
import hashlib
from typing  import Optional, Tuple
class UserModel:
    def __init__(self, db_name='users.db'):
        self.db_name=db_name
        self.__init__db()


    def __init__(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor =conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           username TEXT PRIMARY KEY,
                           password TEXT NOT NULL,
                           email TEXT NOT NULL,
                           create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                           )''')
    def add_user(self,username:str,password:str,email:str=None) -> bool:
        hashed_pw=self.__hash__password(password)
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor =conn.cursor()
                cursor.execute('''(
                            INSERT INTO users (username, password, email) VALUES (?, ?, ?)
                                           
                            ''' ,(username, hashed_pw, email))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
        
    def authenticate(self, username:str,password:str) -> bool:
        hashed_pw=self.__hash__password(password)
        with sqlite3.connect(self.db_name) as conn:
            cursor =conn.cursor()
            cursor.execute('''(
                           SELECT username FROM users
                           WHERE username =? AND password =?
                           ''',(username,hashed_pw))
            return cursor.fetchall() is not None




    def get_user(self , username:str) -> Optional[Tuple]:
        with sqlite3.connect(self.db_name)as conn:
            cursor =conn.cursor()
            cursor.execute('''(
                           SELECT * FROM users
                           WHERE username =?
                           ''',(username,))
            return cursor.fetchone()
        
        @staticmethod
        def __hash__password(password: str) -> str:
            return hashlib.sha256(password.encode()).hexdigest()
                                              
