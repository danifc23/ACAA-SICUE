# ACPEM-SICUE (Análisis y Comparación de Planes de Estudio de Movilidad SICUE)

## Problema

### Contexto

Los estudiantes del programa SICUE (Sistema de Intercambio entre Centros
Universitarios de España) tienen que elaborar un acuerdo académico con las
asignaturas que cursarán en la universidad de destino, y este proceso les causa
problemas de forma habitual.

### Descripción del proceso actual

Seleccionar, en la universidad de destino, asignaturas equivalentes a las del
plan de estudios de la universidad de origen es un proceso agotador. El
estudiante tiene que:

1. Leer y analizar las guías docentes de todas las asignaturas que pueda elegir,
   así como las de su titulación en la universidad de origen.
2. Seleccionar aquellas que desee y que considere equivalentes, y recogerlas en
   el **acuerdo académico**, que deben firmar el propio estudiante y los
   coordinadores SICUE de ambos centros.

El acuerdo académico es vinculante: una vez firmado por las tres partes, lo que
el estudiante curse en destino se reconoce automáticamente en origen, y el
acuerdo solo puede modificarse durante el primer mes desde el inicio del
semestre ([Convocatoria SICUE 2026/2027][convocatoria]). Por eso la decisión
clave es la del coordinador de origen al firmar: en ese momento se juzga si las
asignaturas elegidas son equivalentes.

### Criterio de equivalencia

La equivalencia entre asignaturas se evalúa por **competencias, contenidos y
créditos**. El [Real Decreto 822/2021][rd822] (art. 10) regula el
reconocimiento de créditos entre títulos universitarios oficiales y encarga a
cada universidad aprobar su propia normativa. En la UGR, el [Reglamento de
reconocimiento][ncg323] (art. 6) fija como criterio «la adecuación entre las
competencias, los conocimientos y el número de créditos», y la [normativa de
movilidad nacional de la ETSIIT][etsiit] (Anexo I) lo concreta: se comparan los
contenidos y los ECTS, con especial peso del contenido, y una o varias
asignaturas de origen pueden corresponder a una o varias de destino. La
[Convocatoria SICUE 2026/2027][convocatoria] añade dos cosas. El intercambio
debe adecuarse al perfil curricular del estudiante. Además, las optativas de
destino que no existan en el plan de origen pueden incorporarse al expediente
como optativas.

En este proyecto, ese criterio se traduce en las siguientes reglas:

- Una o varias asignaturas de origen quedan **cubiertas** por una o varias
  asignaturas de destino si se cumplen dos condiciones: sus contenidos y
  competencias están recogidos en los de destino, y la suma de los ECTS de
  destino es igual o mayor que la suma de los ECTS de origen.
- Cada asignatura de destino forma parte, como máximo, de una de esas
  correspondencias.
- Una optativa de origen puede cubrirse con una optativa de destino que no esté
  en el plan de origen y tenga ECTS suficientes, ya que esta se incorpora al
  expediente como optativa.
- El plan debe sumar al menos 24 ECTS en una estancia de medio curso o 45 ECTS
  en una de curso completo.
- El **grado de equivalencia** de un plan es el porcentaje de ECTS de origen
  cubiertos. Un plan es equivalente cuando cubre todas las asignaturas
  obligatorias de origen.

### Por qué es un problema

- El proceso es lento y puede tener que repetirse por falta de plazas en las
  asignaturas, conflictos de horarios, entre otras causas. Como el acuerdo solo
  puede modificarse durante el primer mes del semestre, cada contratiempo obliga
  a rehacer el análisis con prisa.
- Las plazas SICUE se ofertan mediante convenios bilaterales entre centros: el
  estudiante elige destino meses antes de conocer la disponibilidad real de
  plazas en cada asignatura y los horarios definitivos.
- Es un problema muy habitual entre los estudiantes de programas de movilidad, y
  supone una pérdida de tiempo y de oportunidades para que el estudiante pueda
  cursar las asignaturas que realmente desea.

### Datos disponibles

Las guías docentes de las asignaturas son públicas, al igual que otros criterios
de equivalencia, como el número de créditos ECTS. Las guías están en español y
todas incluyen competencias, resultados de aprendizaje, contenidos y evaluación,
pero cada universidad las organiza y publica a su manera: la UGR en páginas web
y la UPM en PDF. Por ejemplo, las del [doble grado en Ingeniería Informática y
Matemáticas de la UGR][plan-ugr] y las [guías de aprendizaje de la ETS de
Ingenieros Informáticos de la UPM][guias-upm].

### Escala del problema

Una titulación de grado de 240 ECTS puede tener unas 60 guías docentes. Para
elaborar el acuerdo académico, el estudiante tiene que comparar cada asignatura
de origen que va a sustituir con todas las asignaturas elegibles en destino, y
después escoger una combinación.

**Asignaturas de la ETSIIT que se pueden escoger por año del grado en el primer
semestre:**

| Curso | Asignaturas en el 1er semestre |
| --- | --- |
| 1º | 5 (todas troncales) |
| 2º | 5 (todas obligatorias) |
| 3º | 5 (comunes; las de especialidad son del 2º semestre) |
| 4º | 28: 15 obligatorias de especialidad (3 por mención) + 13 optativas de especialidad |
| **Total** | **43** |

Si un estudiante de último curso se limita a asignaturas de 3º y 4º, tiene 33
candidatas.

| | Medio curso (ETSIIT, último curso) | Curso completo (estimación) |
| --- | --- | --- |
| Asignaturas de origen a sustituir | 5 (30 ECTS) | 10 (60 ECTS) |
| Asignaturas elegibles en destino | 33 | ~60 |
| Guías docentes que leer | 38 | ~70 |
| Comparaciones asignatura a asignatura | 165 | ~600 |
| Combinaciones posibles de asignaturas de destino | C(33, 5) = 237 336 | C(60, 10) ≈ 7,5 · 10¹⁰ |

Como una asignatura de origen puede quedar cubierta por varias de destino, el
número real de planes posibles es aún mayor. Además, cada falta de plazas o
conflicto de horarios obliga a repetir la búsqueda.

## Lógica de negocio

Para cada asignatura o grupo de asignaturas de origen se calcula qué parte de su
temario está recogida en una o varias asignaturas de destino. Cada tema se
representa con TF-IDF, que da poco peso al vocabulario común a todas las guías,
y se compara con los temas de destino mediante la similitud del coseno. Un tema
queda cubierto si se parece lo suficiente a alguno de destino, y la asignatura
o el grupo, si lo está una proporción suficiente de sus temas y los ECTS de
destino alcanzan los de origen. Las competencias específicas se comparan igual,
pero con menos peso, porque la normativa da especial peso al contenido.

Con esas coberturas se genera el plan que cubre más ECTS de origen cumpliendo
las reglas anteriores, y se indica qué temas quedan sin cubrir, para que el
estudiante sepa antes de la firma qué puede rechazar el coordinador.

## Validación

Los umbrales y pesos se ajustan con correspondencias de acuerdos SICUE ya
firmados, que la solución debe dar como cubiertas, y con correspondencias
rechazadas por el coordinador, como la de Análisis Funcional de la HU1, que
debe dar como no cubiertas. Los casos se obtienen de estudiantes SICUE de
cursos anteriores y de los coordinadores de origen, a los que se pueden pedir
correspondencias aprobadas y rechazadas. Una parte de los casos se reserva para
comprobar los parámetros elegidos.

## Planificación

La planificación parte de la entrevista a un estudiante SICUE y sigue este
orden:

1. [User journey][journey]: el recorrido de un estudiante del doble grado en
   Ingeniería Informática y Matemáticas de la UGR durante su SICUE de curso
   completo en la UPM, con los puntos de dolor y las necesidades de cada etapa.
2. [Personas][personas]: el perfil de usuario que se extrae de ese recorrido.
3. [Historias de usuario][user-stories] ([issues][issues-hu]): la HU1 recoge el
   problema de elaborar un acuerdo académico admisible, la etapa más costosa
   del recorrido.
4. [Milestones][milestones] ([en GitHub][milestones-gh]): el M0 modeliza la
   HU1, y el M1 añade sobre ese modelo la lógica de negocio y sus tests.

## Documentación adicional

- [Configuración de git y GitHub](docs/configuration.md)
- [Fotografía de la tarjeta del juego de rol](docs/img/tarjeta.jpeg)

[convocatoria]: https://www.crue.org/wp-content/uploads/2025/12/00.-Convocatoria_SICUE_2026-2027_vf-1.pdf
[rd822]: https://www.boe.es/buscar/act.php?id=BOE-A-2021-15781
[ncg323]: https://secretariageneral.ugr.es/sites/webugr/secretariageneral/public/inline-files/NCG323.pdf
[etsiit]: https://etsiit.ugr.es/sites/centros/etsiit/public/inline-files/Reglamento_Reconocimiento_Nacional_ETSIIT_2021.pdf
[plan-ugr]: https://grados.ugr.es/ramas/dobles-titulaciones/grado-ingenieria-informatica-matematicas
[guias-upm]: https://www.etsiinf.upm.es/?pagina=3175
[journey]: docs/user-journey.md
[personas]: docs/personas.md
[user-stories]: docs/user-stories.md
[issues-hu]: https://github.com/diego-vigil-sosa/ACPEM-SICUE/issues?q=label%3Auser-stories
[milestones]: docs/milestones.md
[milestones-gh]: https://github.com/diego-vigil-sosa/ACPEM-SICUE/milestones
