# Plant Server
This is a server-side program that serves information about my plant collection using the Django framework.

## Installation
1. Clone the repository: `git clone https://github.com/darchdekin/plant-server.git`
2. Navigate to the project directory: `cd plant-server`
3. Install dependencies: `pip install -r requirements.txt`


## Deployment
To deploy this project for development run
```bash
  python manage.py runserver
```

To deploy this project for production using a Gunicorn server, run
```bash
  gunicorn myproject.wsgi
```
