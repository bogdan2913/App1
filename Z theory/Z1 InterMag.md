# Пошаговый план создания проекта

1. Создали папку с файлами и виртуальное окружение 

   `python -m venv .venv`

2. Активировали окружение, установили джанго

    `venv\Scripts\activate`

    `python -m pip install Django`

### Проверка установки и версии Django

```py
python
import django
print(django.get_version())
exit()
```

#### Включить в VSCode терминал cmd

`"terminal.integrated.defaultProfile.windows": "Command Prompt",`

3. Создаём проект (главное приложение App):

`django-admin start project App` // можно создать по имени домена или просто App

4. Закрываем редеактор, переименовываем папку App (которая рядом с venv) в App1 и открываем её в VsCode

5. Открываем файл manage.py и в правом нижнем углу выбираем интерпретатор из виртуального окружения, нам нужно find->перейти на уровень выше где у нас лежит venv -> в папке venv\Scripts выбрать python.exe

6. Создание launch.json

Создаём файлик launch.json, в ставляем туда этот код:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django: запуск сервера",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver"],
            "django": true,
            "justMyCode": true
        }
    ]
}
```

В результате структура проекта на данный момент должна выглядеть примерно так:

```html
EXPLORER
└── APP1
    ├── vscode
    │   └── launch.json
    ├── App
    │   ├── __pycache
    │   ├── __init__.py
    │   ├── urls.py
    │   └── ...    
    ├── db.sqlite3
    └── manage.py
```

7. Запуск проекта

ctrl + f5 - запускает проект из любого файла

8. Добавление settings.json для более глубокой индексации

Файл settings.json кидаем в папку .vscode и закрываем

9. Включаем все необходимые расширения 

10. Проект готов

























