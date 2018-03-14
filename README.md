# django-todo-rest
django rest server for todo application


### initialize database
python manage.py makemigrations todo
python manage.py migrate

INSERT INTO todo(title, complete) values('buy pants', 0);
INSERT INTO todo(title, complete) values('learn flight', 1);