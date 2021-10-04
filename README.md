# site_foodboxes

Запуск проекта:

1 . Активируем виртульнок оеружение.

2 . Скачиваем пакеты:

pip install -r requirements.txt

3 . Создаем базу данных:

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py save_data -f

4 . Запускаем сервер:

python3 manage.py runserver

