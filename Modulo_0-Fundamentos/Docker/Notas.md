### Clase 12/01/2022
---
Comandos para utilizar en docker:

- Docker ps -> Listar contendores activos
- Docker ps -a -> Listar todos los contenedores
- Docker start/stop -> Solo se usa cuando está creado el contenedor para arrarncar o parar
- Docker run -it  -> Crea una imagen de ubuntu (importante poner -it porque sino se crea y muere, con el -it entra dentro del contenedor
- Docker run -it –name “Nombre” ubuntu
- docker rm 26 ->26 Es el inicio del container ID, no hace falta ponerlo entero para eliminarlo
- docker system prune -> Borrar todos los contenedores (dangling images son las que no tienen nombre)
- docker image ls -> Listar todas las imágenes
- docker rmi (ID)-> Borrar todas las imágenes
- docker inspect (ID) -> Te da un JSON con los datos 
- docker run -d -> Cuando es un servidor que se ejecuta continuamente tipo zeppelin o nginx para que 
