Sobre la Revisión por Pares
===========================

:date: 2007-06-06
:slug: sobre-la-revision-por-pares
:author: Apalala

.. :tags:
.. :category:
.. :summary:


Van algunos comentarios en torno al artículo que mi amigo
`Pedro <http://pedrogtit.blogspot.com/>`__\ escribió sobre "peer
reviews".

[versión 0.1]

En el mundo del software una revisión por pares no es solo una
oportunidad para mejorar la calidad del producto (el "código fuente") a
través de la detección temprana de defectos, como errores de
programación, o desviaciones de la especificación, de la arquitectura, o
de las buenas prácticas.

Es también una importante oportunidad de aprendizaje para los
participantes, y en ello una opotrunidad de mejorar el entorno.

Una revisión por pares enfocada solo en encontrar anomalías, o "el
qué", pierde la valiosa oportunidad valiosa de analizar también el
"cómo" y el "por qué":

-  Falta de conocimiento.
-  Herramientas inadecuadas.
-  Tareas repetitivas y proclives a equivocaciones.
-  ...

Y de aplicar mejoras con efectos permanentes como:

-  Entrenamiento.
-  Obtención o creación de mejores herramientas.
-  Automatización.
-  ...

Por ejemplo, la
`automatización <http://en.wikipedia.org/wiki/Static_code_analysis>`__
de las revisiones particularment porque provee a tanto revisores como a
autores de más tiempo para ocuparse de lo verdaderamente importante.

Al final importan el entendimiento de los conceptos y de las buenas
prácticas, y el buen criterio. Frente a una desviación de las normas o
la arquitectura el autor debería ser capaz de argumentar sbore por qué
su decisión fue adecuada y no un capricho o un error. A veces ocurre que
la arquitectura tiene defectos u omisiones, o que una norma no es
aplicable en todas las situaciones.

Durante una revisión por pares buscamos que el código sea "bueno".

Un código que no es de calidad puede pasar una primera inspección ser
todavía vulnerable a la ocurrencia de cientos de defectos en una
siguiente iteración.

Mucho se ha discutido sobre la "estética" en software porque, en
general, la informática se considera una cosa objetiva, mucho más
cercana a las matemáticas que a la música (algo bien
`discutible <http://www.amazon.com/Godel-Escher-Bach-Eternal-Golden/dp/0465026567/>`__).

La verdad es que la calidad estética del software puede determinarse
con criterios bastante objetivos. Criterios que tienen que ver
fundamentalmente con cuan entendible por otros mortales es una pieza de
código. Lo subjetivo está en que quien adquiere experiencia en escribir
buenos programas adquiere también un sentido intuitivo (o "estético") .

-  Modularidad
-  Separación de responsabilidades
-  Alta cohesión
-  Bajo acoplamiento
-  Minimalidad
-  Comprensibilidad
-  ...

Hay toda una tradición en libros por autores famosos sobre estos
temas: `Software
Tools <http://www.amazon.com/Software-Tools-Pascal-Brian-Kernighan/dp/0201103427/>`__,
`Programming
Pearls <http://www.amazon.com/Programming-Pearls-2nd-Jon-Bentley/dp/0201657880/>`__,
`Code
Complete <http://www.amazon.com/Complete-Microsoft-Programming-Steve-McConnell/dp/1556154844/>`__,
`Design
Patterns <http://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional/dp/0201633612/>`__,
`Pragmatic
Programmer <http://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X/>`__,
y
`Refactoring <http://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672/>`__,
entre otros.

Por ser tan importantes el aprendizaje, el entendimiento, y el
criterio, los acercamientos
`ágiles <http://en.wikipedia.org/wiki/Agile_programming>`__ al
desarrollo de software incorporan varias prácticas particularmente
relevantes a este tema:

-  Programación en pares que cambian, con lo cual la práctica de
   revisión por pares se lleva a cabo constantemente.
-  El código es la documentación, con lo cual se afianza el concepto de
   "tener criterio" y se resuelven los conflictos con documentación de
   diseño obsoleta, incompleta, o errónea.
-  Automatización, no solo de las pruebas unitarias, sino de toda tarea
   que sea repetitiva y con ello proclive a errores.

Una revisión por pares no es solo una oportunidad para detectar y
corregir los errores de hoy, sino para aprender, y así poder hacer del
trabajo de manera más fácil y mejor en el futuro.
