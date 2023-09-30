### Para correr el proyecto
1. Cree su máquina virtual
2. pip install -r requirements.txt
### En una terminal corra el microservicio usuarios
1. cd usuarios
2. flask run -p 5000

### En otro terminal corra el microservicio autenticador
1. cd autenticador
2. flask run -p 8000 

### En otro terminal corra el microservicio candidatos
1. cd candidatos 
2. flask run -p 9000

### En otra terminal Active el redis server
1. redis-server 

### En otra terminar active el servicio de mensajería
1. celery -A autenticador.tareas.tareas worker --loglevel=info -P eventlet

### Para correr la prueba en otra terminal ejecute
1. cd prueba
2. flask run -p 10000