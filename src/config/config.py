from dotenv import load_dotenv
import os

load_dotenv()

host = os.environ["host"]
database = os.environ["database"]
userdb = os.environ["user"]
passworddb = os.environ["password"]
portdb = os.environ["port"]
ks = os.environ["ks"]
prueba = "test"