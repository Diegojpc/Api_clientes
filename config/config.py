import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:Diego_jose123@localhost/gamma_clientes')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
