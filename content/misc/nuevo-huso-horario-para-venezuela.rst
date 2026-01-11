Nuevo Huso Horario para Venezuela
=================================

:date: 2007-09-18
:slug: nuevo-huso-horario-para-venezuela
:author: Apalala

.. :tags:
.. :category:
.. :summary:


- vo.2 Agregada nota sobre nueva fecha para el cambio de horario.

  ::

    NOTA: El cambio de huso horario será el 9 de diciembre de 2007 a las
    3:00 AM. 

El anunciado cambio de huso horario en Venezuela tiene una aplicación
sencilla en la mayoría de los casos: atrasar el reloj media hora.

En el caso de las computadoras el cambio de hora es un poco más
complejo debido a que redes como la Internet se rigen por el Tiempo
Universal Coordinado
(`UTC <http://es.wikipedia.org/wiki/Tiempo_Universal_Coordinado>`__) ,
el cual se matiene en consistencia con el Tiempo Medio de Greenwhich
(`GMT <http://es.wikipedia.org/wiki/Tiempo_Medio_de_Greenwich>`__), y
compensan las horas indicadas en mensajes y otras comunicaciones de
acuerdo al huso horario indicado en la configuración. Si solo
cambiáramos la hora en la computadora, la misma calcularía la hora GMT
incorrectamente. En vez de calcular que un mensaje que acabamos de
escribir a las 20:00 hora de Venezuela fue escrito a las 00:30 GMT del
día siguiente (20:00 + 4:30 = 24:30), calcularía que el mensaje fue
escrito media hora antes (20:00 + 4:00 = 24:00), y eso seguramente
causará problemas.

Para el caso de los sistemas operativos Windows, Microsoft ha
`publicado <http://support.microsoft.com/kb/914387>`__ instrucciones
detalladas sobre como cambiar o definir nuevas zonas horarias. El método
más sencillo es éste:

#. Descargar
   `tzedit.exe <http://download.microsoft.com/download/5/8/a/58a208b7-7dc7-4bc7-8357-28e29cdac52f/tzedit.exe>`__
   de la página de Microsoft.
#. Ejecutar el programa para descomprimirlo (por defecto a C:\\Program
   Files).
#. Ejecutar C:\\Program Files\\TZEDIT.EXE.
   |image0|
#. Oprimir el botón New (Nueva) y agregar una zona horaria como
   esta:
   |image1|
#. Finalmente, el domingo 9 de diciembre en la mañana, escoger la nueva
   zona horaria y colocar la nueva hora (media hora menos) usando la
   aplicación de Fecha y Hora del Panel de Control (Control Panel).

Los usuarios de Linux pueden usar el programa
`zic <http://manpages.courier-mta.org/htmlman8/zic.8.html>`__ para
compilar una nueva zona horaria. Existen
`instrucciones <https://secure-support.novell.com/KanisaPlatform/Publishing/51/3655154_f.SAL_Public.html>`__
para las distintas distribuciones en la red.

Los usuarios de celulares, agendas electrónicas, y localizadores
geosatelitales probablemente tendrán que esperar a que una actualización
adecuada del software para el dispositivo se haga disponible.

.. |image0| image:: /images/tzedit.png

.. |image1| image:: /images/vet07.png
