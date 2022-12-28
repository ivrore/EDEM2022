# Apache Nifi 
<ins>*¿Qué es Nifi?*</ins>

Es una herramienta ETL (extracción, transformación y carga) que permite automatizar estos procesos con gran escalabilidad, monitoreo y trazabilidad de los datos.

<ins>*¿Para que se puede utilizar?*</ins>

1. Ingestar datos en un data lake en la nube.
2. Conectar los datos de una plataforma a otra, por ejemplo, para la visualización.

<ins>*¿Cómo funciona?*</ins>

El interconexionado entre los diferentes elementos permite establecer la automatización del flujo de los datos para recibir y enviar datos a través de la programación de ordenes.


## Principales conceptos

- **FlowFile**: Es un paquete de información sobre el movimiento de cada objeto a través del sistema.
- **FlowFile Processor**: Es el encargados de realizar las tareas de transformación y mediación entre sistemas.
- **Connection**: Proveen las conexionen enter procesadores y actuán como colas de diferentes procesos.
- **Flow Controller**: Actua como intermediario facilitando el intercambio de FlowFiles entre procesadores.
- **Process Group**: Un conjunto de procesos y conexiones que permiten recibir/enviar datos a través de sus puertos.
