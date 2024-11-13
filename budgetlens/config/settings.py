import os
from dotenv import load_dotenv

# Cargar el archivo .env desde la carpeta data
load_dotenv(dotenv_path=os.path.join('..', 'data', '.env'))

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()
