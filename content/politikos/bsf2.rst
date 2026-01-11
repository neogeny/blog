BsF2
====

:date: 2007-09-22
:slug: bsf2
:author: Apalala

.. :tags:
.. :category:
.. :summary:


En una `nota <http://blog.neogeny.org/2007/09/bsf.html>`__ anterior
expliqué las razones por las cuales es conveniente considerar una
reconversión monetaria como la introducción de una nueva moneda, y
adaptar los sistemas informáticos para el manejo de múltiples monedas.

¿Cómo se hace eso?

En un sistema que maneja múltiples monedas, un monto aislado carece de
significado mientras no se sepa en qué moneda está expresado. Por eso
los montos deben pasar de ser solo cifras a pares ordenados:

    [monto, moneda]

Con eso las capas superiores de una aplicación pueden solicitar
valores en una moneda en particular, delegando en librerías
especializadas el llevar cuenta de los tipos de cambio, su conversión,
su aritmética, y su presentación.

Usando orientación a objetos la interfaz para dichas librerías resulta
bastante simple. Las librerías para manejo de `fechas localizadas en
Java <http://java.sun.com/j2se/1.5.0/docs/api/java/util/Calendar.html>`__
son un buen ejemplo de como lograr ese tipo de abstracción. Uno de los
primeros tutoriales para la librería de pruebas
`JUnit <http://www.junit.org/>`__ trata precisamente sobre un programa
que `maneja múltiples
monedas <http://junit.sourceforge.net/doc/testinfected/testing.htm>`__.
Otra ventaja es que una librería de manejo de múltiples monedas puede
escribirse una vez, y se reutilizada indefinidamente, más si la misma es
expuesta como servicio Web.

Manejando los montos como pares, las bases de datos antiguas y de
solo-lectura pueden quedarse como están, ya que la transformación a
pares puede llevarse a cabo solo en las interfases que lo requieran. Así
muchas de las interfases entre sistemas "legacy" pueden permanecer
inalteradas.

Para bases de datos activas es necesario agregar una columna paralela
que indique la moneda para cada columna que contenga un monto; una tarea
fácil, rápida, e inocua si es realizada antes de la fecha de la
reconversión, y la cual evita los riesgos de discrepancia con
contrapartes en físico (en papel) y las inconsistencias con sistemas que
no deben ser modificados. Para los sistemas sujetos a actualización, las
consultas a bases de datos específicas en las capas de persistencia de
una aplicación deben extraer el par completo (ambos valores), y dejar lo
demás a las librerías correspondientes.

Manejar los montos en las transacciones como pares [monto, moneda] es
suficiente para atender los requerimientos de la introducción del
Bolívar Fuerte inmediatos y para siempre, ya que la tasa de conversión
de Bs. 1000/Bs.F. jamás va a cambiar.

Para hacer que un sistema maneje múltiples monedas internacionales
hace falta agregar una dimensión temporal a los montos debido a que las
tasas de cambio varían constantemente. Ese será el tema de otro
artículo.
