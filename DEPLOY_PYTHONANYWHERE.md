# Инструкция по деплою на PythonAnywhere

## 1. Регистрация
1. Зайдите на https://www.pythonanywhere.com/
2. Зарегистрируйтесь бесплатно (Free account)
3. Подтвердите email

## 2. Создание веб-приложения
1. После входа перейдите в Web tab
2. Нажмите "Add a new web app"
3. Выберите:
   - Domain name: выберите свободный домен
   - Web framework: Flask
   - Python version: 3.10 или выше

## 3. Загрузка файлов
1. Перейдите в Files tab
2. Зайдите в папку вашего веб-приложения (обычно /home/ваш_логин/yourdomain.com)
3. Загрузите все файлы проекта:
   - app.py
   - init_db.py
   - requirements.txt
   - templates/ (папка со всеми шаблонами)
   - static/ (папка со статическими файлами)

## 4. Настройка WSGI
1. Перейдите в Web tab
2. Нажмите "Configuration"
3. В разделе "WSGI configuration file" нажмите "Enter path"
4. Укажите путь: /home/ваш_логин/yourdomain.com/photostudio.wsgi

## 5. Установка зависимостей
1. Откройте Bash консоль в PythonAnywhere
2. Выполните:
```bash
pip install -r requirements.txt
```

## 6. Инициализация базы данных
1. В Bash консоли выполните:
```bash
cd /home/ваш_логин/yourdomain.com
python init_db.py
```

## 7. Перезапуск приложения
1. В Web tab нажмите "Reload your web app"

## 8. Проверка
1. Откройте ваш сайт в браузере
2. Проверьте работу всех функций

## Важно!
- PythonAnywhere бесплатный аккаунт имеет ограничения
- База данных SQLite будет храниться в файле
- Для работы формы записи нужно настроить переменные окружения