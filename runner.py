import os
from app import app
from flask_migrate import Migrate


# эти переменные доступны внутри оболочки без явного импорта


if __name__ == '__main__':
    app.run(host="0.0.0.0")
