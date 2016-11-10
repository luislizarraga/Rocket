Ticket app usando Python3 con virtualenv y bower.

Para instalar en Ubuntu:

```bash
- sudo apt-get install python3-dev python3-venv
- python -m venv "nombre de virtualenv"
- pip install -r requirements.txt
- npm install bower
- bower install
```

y listo!.

Se debe crear un usuario administrador con `python3 manage.py createsuperuser`, y después usar el administrador de Django para crear los demás usuarios.