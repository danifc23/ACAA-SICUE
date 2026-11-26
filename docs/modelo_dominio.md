# Modelo del dominio

## Análisis de la HU001

El estudiante necesita disponer de la información académica de las asignaturas de origen y destino para determinar sus posibles equivalencias. El problema es que las universidades publican sus guías docentes en diferentes formatos y estructuras, dificultando su comparación.

## Entidad: Asignatura

Se identifica la asignatura como entidad principal del dominio, ya que representa el elemento sobre el que se realizará la comparación académica.

Su identidad viene determinada por el código de la asignatura y la universidad a la que pertenece.

Contiene los siguientes atributos:

- Código.
- Universidad.
- Nombre.
- Créditos ECTS.
- Tipo de asignatura.
- Curso y semestre.
- Requisitos.
- Competencias.
- Resultados de aprendizaje.
- Temario.

Estos atributos permiten representar de manera homogénea las asignaturas de diferentes universidades.

## Objeto valor: GuiaDocente

La guía docente se modela como un objeto valor independiente e inmutable, asociado a una asignatura, universidad y curso académico.

Esta separación permite que la entidad Asignatura sea independiente del formato en el que cada universidad publica sus guías docentes.

Esta decisión se ha tomado a partir de lo discutido en el [issue #10](https://github.com/diego-vigil-sosa/ACAA-SICUE/issues/10).

## TipoAsignatura

Se representa mediante una enumeración que distingue entre asignaturas básicas, obligatorias y optativas.

## Alcance del modelo

En este milestone únicamente se representa el dominio. La extracción de información de las guías y el cálculo de equivalencias entre asignaturas se abordarán posteriormente.