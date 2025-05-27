<!-- Initialize backend -->

navigate to ./backend
run "python3 manage.py runserver" in terminal

<!-- initialize frontend -->

navigate to ./frontend
run "npm run server" in terminal

<!-- Steps for making migrations -->
<!-- Whenever changes are made to the model.py in the backend file, migrations have to be made to update django. -->

python3 manage.py makemigrations
python3 manage.py migrate
