# Cars-CRUD-app


ТЗ для проекта на хакатон “CRUD”

Цель проекта: реализовать CRUD действия для небольшого автосалона на классах

### Дополнительно: - внедрено "django page pagination" в cars_list.html (в главную страницу - "Home")

- cars/view.py                # Добавлено views:

- cars_list.html              # для получения списка записей авто
- cars_form.html              # для создания/обновления записей авто
- cars_confirm_delete.html    # для удаления записей авто
- car_detail.html             # для получения одной записи авто

- base.html                   # создано базовый шаблонизатор

- brand_list.html             # для получения списка записей брендов авто
- brand_form.html             # для создания/обновления записей брендов авто
- brand_confirm_delete        # для удаления записей брендов авто

- cars/models.py              # Создание класс Cars со следующими атрибутами объекта

- cars/urls.py                # Создано urls, чтобы можно было взаимодействовать с основным autos/urls.py 

- db.sqlite3                  # Сохранение данных в бд sqlite

- comment = models.TextField(blank=True)              # добавлено в model Cars комментарии

- i_like = models.CharField(max_length=20,default='like',
                             choices=TLIKE_CHOICES)   # добавлено в model Cars лайки

- код соответствует PEP8

- requirements.txt            # использованные библиотеки, указано в этом файле

- при выполнении кода не возникнет ошибка             # протестировано несколько раз

- проект загружено в github.com/kuba1248/Cars-CRUD-app


Задание:

1. Создайте класс Cars со следующими атрибутами объекта:
● марка (строка)
● модель (строка)
● год выпуска (целое число)
● объем двигателя (decimal, точность 1 знак)
● цвет (строка)
● тип кузова (поле одиночного выбора.
варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап)
● пробег (целое число)
● цена (decimal, точность 2 знака)
2. Добавьте views:
● create для создания записей
● listing для получения списка записей
● retrieve для получения одной записи
● update для обновления записей
● delete для удаления записей


Extra функционал:
● Создайте urls, чтобы можно было взаимодействовать через терминал.
● Сохранение данных в бд (json / sqlite / postgresql)
● Сделайте комментарии
● Сделайте лайки

Требования к проекту:
- код должен соответствовать PEP8
- при использовании каких-либо библиотек, укажите их в файле
requirements.txt
- при выполнении кода не должно возникать ошибок
- свой проект нужно закинуть в GitHub

#### Cледующие цели/планы для развития/расширение проекта "Cars CRUD app" :

- brand_detail.html     # добавить страницу для получения списка авто по отдельным брендам

- на главную страницу добавить окно "поиск", где можно искать по всем характеристикам авто и брендов,
- на главную страницу добавить рисунок лого,

- добавить на главную страницу  логин/выход пользователей,
- добавить CRUD для пользователей
- добавить категорию для пользователей: владелец, продавец, покупатель, менеджер
- добавить карзину для заказа, покупку машины
- добавить онлайн оплату через электронную банковскую карту,
- добавить получение списка заказов на корзине, управление корзиной CRUD
- добавить почтовую сервер smtp для отправки сообщении, уведомлении по заказу, по изменению паролей, и т.д.
- добавить получение списка заказов, лубой список в базе на pdf  формате, или на электронную почту
- добавить акции, скидки, купоны,
- добавить аукцион,
- добавить рисунок авто, брендов, аватар пользователей
