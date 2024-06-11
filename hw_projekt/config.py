from pydantic_settings import BaseSettings
from pydantic import EmailStr

class Settings(BaseSettings):
    SECRET_KEY: str = "str"
   
    POSTGRES_DB: str= "postgres"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "7703"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432


    EMAIL_PORT: int = 465
    EMAIL_HOST_USER: str = "alena_mishchenko@meta.ua"
    EMAIL_HOST_PASSWORD : str = "sicret"

    DEFAULT_FROM_EMAIL : str = 'EMAIL_HOST_USER'
    

    # CLOUDINARY_NAME: str
    # CLOUDINARY_API_KEY: int
    # CLOUDINARY_API_SECRET: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Settings()
