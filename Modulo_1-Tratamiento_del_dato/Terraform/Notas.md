# DevOps
## ¿Qué es DevOps?
Suma muchas disciplinas:
- Conocer el código
- Comunicativo
- Integración continua
- Despliegue de infraestructura

## Qué es DevSecOps?

IAC - Infraestructura como código

Se utiliza sobretodo para setear en la nube todo.

Service account:
Es un fichero que tiene determinados permisos de acceso de Google.

Ejemplo gcp:
1. Creamos un proyecto en Google cloud.
2. Definimos los roles:
- Cloud Run Admin - Permite la creación, actualización y borrado de servicios en Cloud Run
- Service Account User - Necesario para desplegar cloud roun como service account
- Storage Admin - Permite subir al contenedor de registro de Google

Para ello:
1. IAM & Admin >> Service accounts 
2. Create service account
3. Define roles
4. Actions >> Manage keys >> Add key > Create JSON 

status.cloud.google >> Se puede ver si algún servicio está caído si no carga


Para guardar los secretos de las credenciales de Google
Github >> Settings >> Secrets and variables >> Actions >> New repository secret 
