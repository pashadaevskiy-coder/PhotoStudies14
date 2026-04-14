import sys
import os

# Добавляем путь к вашему приложению
sys.path.append('/home/ваш_логин/photostudio')

# Устанавливаем переменную окружения
os.environ['FLASK_APP'] = 'app.py'

from app import app as application

# Если нужно, можно добавить настройку для production
# application.config['ENV'] = 'production'