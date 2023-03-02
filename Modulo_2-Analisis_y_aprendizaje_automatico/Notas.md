# Clase 02/03/2023
## Análisis y aprendizaje automático
---
**Machine Learning** es una rama de la Inteligencia Artificial cuyo objetivo es construir sistemas que aprendan automáticamente de los datos

Inteligencia artificial > Machine Learning > Deep Learning

El **aprendizaje automático** está basado en reglas o normas de aprendizaje

Ejemplos:

- Netflix: Utiliza el modelo de sistema de recomendación
- Coche autónomo: Mezcla de machine learning para distinguir el color del semáforo (deep learning) e inteligencia artificial con sensores
  
Conocimiento de negocio + Estadística/Matemática + Computación

Estructura de un proyecto:
|Pasos|Descripción|Ejemplo|
|-----|----------|------|
|1.| Plantear un problema o hipótesis| Optimizar el precio de los billetes de avión|
|2. |Recolección de datos |Venta de billetes, hora, etc... Todos los datos que puedan ser útiles aunque luego no se usen|
|3.|Preprocesado de datos | Se debe escoger una buena muestra, limpieza, etc..|
|4.| Modelización | Se hacen muchos modelos para probar y entrenar|
|5.| Evaluación | Se prueba cada modelo con un caso real y el ajuste con la realidad y se va iterando hasta encontrar un buen ajuste|
|6.| Conclusiones | Informes y visualización de los datos extraidos|
|7.| Puesta en producción | Se aplica a la resolución del problema real|
|8.| Mantenimiento | Pueden haber cambios que afecten al modelo por lo que hay que actualizarlo (ej. Covid)|

## Etapas de la modelización
---
1. Train - Selección de modelos ANN, SVM, XGBoost, etc.. con parámetros diferentes
2. Validation - Selección de métricas para medir el error MAE, AUC, F-score, etc.. 
3. Test - El error debe ajustarse al error esperado

## Definiciones
---
- Overfitting - Equivocación por ajustarse mucho al conjunto de train, por ejemplo por la forma concreta del objeto de la imagen.
- Accuracy - Cuando ejemplos se aciertan. (ej. 2/3 imágenes = 63%)
- Data Augmentation - Ejemplos sintéticos para cumplimentar campos vacíos