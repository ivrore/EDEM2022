# Apache Kafka
<ins>*¿Qué es Kafka?*</ins>

Es una plataforma de transmisión de eventos o mensajes de extremo a extremo.

<ins>*¿Para que se puede utilizar?*</ins>

1. Publicar (publish) y leer (subscribe) flujos de eventos.
2. Almacenar secuencias de eventos de forma duradera y fiable.
3. Procesar flujos de eventos.

<ins>*¿Cómo funciona?*</ins>

Está basado en **servidores** normalmente agregados en un clúster y algunos de ellos forman la capa de almacenamiento. A estos últimos se les denomina brokers. Este sistema de conexión en clúster permite gran escalabilidad y evita fallos, ya que si uno de los servidores falla el resto continuará sin pérdida de datos.

Por otra parte, están los **clientes** que permiten leer, escribrir y procesar grandes conjuntos de eventos en paralelo evitando problemas de red o de equipo. 

Estos eventos normalmente tienen una **clave**, **valor**, **tiempo** y otros metadatos opcionales.

<ins>*¿Por cuanto tiempo se almacenan los eventos?*</ins>
Se puede configurar su almacenamiento hasta que sean borrados en función de:

- Tiempo
- Tamaño
- Compactación (Guarda el último evento para cada clave)

## Principales conceptos

- **Producers**: Son los clientes que escriben eventos en Kafka
- **Consumers**: Son los clientes que leen y procesan los eventos en Kafka
- **Topics**: Los eventos se organizan y almacenan en topics
- **Partitions**: Los topics se dividen entre los diferentes brokers.
- **Replication factor**: Cada topic se puede replicar en uno o más brokers.

