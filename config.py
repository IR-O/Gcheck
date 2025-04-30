import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    APP_NAME = os.getenv('APP_NAME', 'malty-bot')
    ENV = os.getenv('ENV', 'DEVELOPMENT')
    PORT = int(os.getenv('PORT', 8443))
