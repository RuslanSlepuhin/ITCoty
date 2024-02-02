import os

from dotenv import load_dotenv

load_dotenv(".env")

TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

# Настройки базы данных
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


#Токен для оплаты через Stripe
STRIPE_BOT_TOKEN = os.getenv('STRIPE_BOT_TOKEN')