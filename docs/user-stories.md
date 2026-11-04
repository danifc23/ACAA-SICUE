# Historias de usuario

## HU1. Ineficacia para llegar a un acuerdo académico admisible ([#2][hu1])

Pablo, estudiante de último curso del doble grado en Ingeniería Informática y
Matemáticas de la UGR, obtuvo una plaza SICUE de curso completo en la UPM y
tenía que elaborar un acuerdo académico admisible: cada asignatura que le
faltaba en la UGR debía quedar cubierta por asignaturas de la UPM.

Para elaborarlo, leyó las guías docentes de las asignaturas que le faltaban en
la UGR y de casi todas las optativas de la UPM en el área de Matemáticas e
Informática, y decidió la equivalencia de cada pareja fijándose sobre todo en el
contenido y, en menor medida, en el nombre.
Le llevó entre 6 y 8 horas, repartidas en 3 o 4 días.
Aun así, el coordinador SICUE de origen rechazó la pareja propuesta para
Análisis Funcional porque «la guía no coincidía del todo con la de la UGR», e
hicieron falta 2 versiones del acuerdo hasta la firma.

Pablo no supo hasta la firma qué asignaturas de origen se quedarían sin cubrir,
ni por qué.
Tampoco sabía cómo se analiza la equivalencia: se fijó en el contenido y el
nombre, sin saber que intervienen los ECTS, el tipo, el curso, el semestre, los
requisitos, las competencias, los resultados de aprendizaje y el temario.
Quería saber qué información de las guías cuenta y tenerla reunida para cada
asignatura que le faltaba y cada candidata de la UPM, sin buscarla guía a guía
en páginas web y PDF con estructuras distintas.
Así habría detectado antes parejas que no coinciden, como la de Análisis
Funcional.
El caso completo está en su [user journey][journey].

### Secciones de las guías docentes que intervienen en la comparación

La UGR publica sus guías docentes en páginas web y la UPM, que las llama «guías
de aprendizaje», en PDF.
Cada una tiene más secciones, pero las que intervienen en la comparación son
estas:

- **Identificación**: código, ECTS, tipo (básica, obligatoria u optativa),
  curso y semestre.
  La UPM llama «carácter» al tipo.
- **Requisitos**: asignaturas o conocimientos previos que se exigen o se
  recomiendan.
  La UPM identifica las asignaturas por su código; la UGR los describe en texto
  libre.
- **Competencias**: lista con código que procede de la memoria de verificación
  del grado.
  Cada universidad usa sus propios códigos (CG, CE y CT en la UGR; C y S en la
  UPM), así que no se pueden comparar por código, y un mismo código se repite
  en asignaturas distintas del mismo grado.
- **Resultados de aprendizaje**: en la UPM tienen código y se enlazan con las
  actividades que los evalúan; en la UGR son listas sin código.
- **Temario**: temas numerados, cada uno con sus subtemas.
  A diferencia de las competencias, lo redacta el profesorado y lo aprueba el
  departamento, así que es lo que más varía entre universidades.
  En la UGR se divide en teórico, organizado en temas, y práctico, cuya
  estructura cambia según la asignatura.

### Reglas del reconocimiento

- El acuerdo académico debe sumar al menos 24 ECTS en una estancia de medio
  curso y 45 en una de curso completo (apartado 2.4 de la
  [Convocatoria SICUE 2026/2027][convocatoria]).
- Una vez firmado por el estudiante y los dos centros, el acuerdo es vinculante
  (apartado 2.4 de la [Convocatoria][convocatoria]), así que la decisión que
  cuenta es la del coordinador de origen al firmar.
- El criterio de reconocimiento es «la adecuación entre las competencias, los
  conocimientos y el número de créditos» (art. 6 del
  [Reglamento de reconocimiento de la UGR][ncg323]), aplicable a la movilidad
  nacional por su art. 11.
- La [normativa de movilidad nacional de la ETSIIT][etsiit] (Anexo I) lo
  concreta:
  - Se comparan los contenidos y los ECTS, con especial peso del contenido.
  - Una asignatura de origen puede corresponder a una o a varias de destino, y
    varias de origen pueden corresponder a una o a varias de destino, siempre
    que el contenido de origen esté recogido en el de destino y los ECTS sean
    similares.
  - El tipo de las asignaturas no es determinante, aunque las básicas y
    obligatorias requieren especial atención.
  - Una asignatura de destino sin equivalente se puede reconocer como
    optatividad genérica.

### Fuentes de datos

- Plan de estudios y guías docentes de origen: [página del doble grado en la
  UGR][plan-ugr].
- Guías docentes de destino: [página de guías de la ETSI de Ingenieros
  Informáticos de la UPM][guias-upm].
- Ejemplos de parejas del curso 2026/2027:
  - Análisis Funcional: [297114D en la UGR][af-ugr] y
    [105000142 en la UPM][af-upm].
  - Inteligencia Artificial: [297113A en la UGR][ia-ugr] y
    [105000133 en la UPM][ia-upm].
- Normativa: [Convocatoria SICUE 2026/2027][convocatoria],
  [Reglamento de reconocimiento de la UGR][ncg323] y
  [normativa de movilidad nacional de la ETSIIT][etsiit].

[hu1]: https://github.com/diego-vigil-sosa/ACAA-SICUE/issues/2
[journey]: user-journey.md
[convocatoria]: https://www.crue.org/wp-content/uploads/2025/12/00.-Convocatoria_SICUE_2026-2027_vf-1.pdf
[ncg323]: https://secretariageneral.ugr.es/sites/webugr/secretariageneral/public/inline-files/NCG323.pdf
[etsiit]: https://etsiit.ugr.es/sites/centros/etsiit/public/inline-files/Reglamento_Reconocimiento_Nacional_ETSIIT_2021.pdf
[plan-ugr]: https://grados.ugr.es/ramas/dobles-titulaciones/grado-ingenieria-informatica-matematicas
[guias-upm]: https://www.etsiinf.upm.es/?pagina=3175
[af-ugr]: https://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica-matematicas/analisis-funcional/guia-docente
[af-upm]: https://www.upm.es/comun_gauss/publico/guias/2026-27/GA_10ML_105000142_ES_2026-27.pdf
[ia-ugr]: https://www.ugr.es/estudiantes/grados/grado-ingenieria-informatica-matematicas/inteligencia-artificial/guia-docente
[ia-upm]: https://www.upm.es/comun_gauss/publico/guias/2026-27/GA_10ML_105000133_ES_2026-27.pdf
