# yandex-afisha
 
Проект разработан для создания собственной интерактивной карты, в которой есть возможность добавлять собственные точки на карте с описанием и фотографиями.

Демо-версия сайта: http://semellot.pythonanywhere.com/
Административная панель: https://semellot.pythonanywhere.com/admin/

## Как установить

Для работы проекта вам понадобится Python 3.10:

1. Клонировать репозиторий:

  ```shell
  git clone https://github.com/semellot/yandex-afisha.git
  ```

2. Создать в каталоге с проектом файл `.env` с переменными окружения. Пример содержимого файла:

  ```
  DEBUG=True
  SECRET_KEY='key'
  ALLOWED_HOSTS='127.0.0.1'
  ```

3. Создать виртуальное окружение, затем запустить его:

  ```shell
  python3.10 -m vitualenv venv
  source venv/bin/activate
  ```

4. Установить зависимости:

  ```shell
  pip install -r requirements.txt
  ```

5. Создать базу данных `sqlite3`:

  ```shell
  python manage.py migrate
  ```

6. Запустить сайт локально:

  ```shell
  python manage.py runserver
  ```
  
  Перейти по адресу http://127.0.0.1:8000/
  
## Наполнение данными

Чтобы на карте появились точки, необходимо добавить их через админку в модель `Place` http://127.0.0.1:8000/admin/places/place/:
- Заголовок
- Краткое описание
- Полное описание
- Координаты: долгота и широта
- Изображения

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).