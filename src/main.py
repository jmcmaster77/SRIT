from flask import Flask
from routes.Auth import auth
from routes.consulta import consulta
app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(consulta)

if __name__ == '__main__':
    app.run()
