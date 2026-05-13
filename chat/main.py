from flask import Flask, session
from view import view

app = Flask(__name__)
app.register_blueprint(view)
app.secret_key = "chave"

if __name__ == "__main__":
    app.run()
    