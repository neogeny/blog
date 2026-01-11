Huso Horario Venezolano en Ubuntu
=================================

:date: 2007-09-22
:slug: huso-horario-venezolano-en-ubuntu
:author: Apalala

.. :tags:
.. :category:
.. :summary:


-  Actualizado para el cambio de huso horario en 2007/12/09 03:00.


En otro
`post <http://blog.neogeny.org/2007/09/nuevo-huso-horario-para-venezuela.html>`__
expliqué como y por qué lidiar con el cambio de huso horario en
Venezuela. Aquí explico cómo hacerlo sobre Ubuntu Linux.

Para lograrlo en una distribución Ubuntu 7.04 hice lo siguiente:

#. Respaldar el archivo /usr/share/zoneinfo/America/Caracas
#. Crear un directorio de trabajo y cambiarse al mismo (mkdir work; cd
   work)
#. Obtener el archivo ftp://elsie.nci.nih.gov/pub/tzdata2007\*.tar.gz
#. Descomprimir el archivo (tar xvzf tzdata\*)
#. Editar el archivo llamado southamerica, ir al final del archivo,
   donde dice "Venezuela", y cambiar las últimas líneas para que
   aparezcan como las resaltadas:

   ::

       # Venezuela# Zone  NAME            GMTOFF  RULES   FORMAT  [UNTIL]Zone    America/Caracas -4:27:44 -      LMT     1890                        -4:27:40 -      CMT     1912 Feb 12 # Caracas Mean Time?                        -4:30   -       VET     1965         # Venezuela Time     -4:00   -       VET     2007 Dec 9 3:00     -4:30   -       VET

#. Compilar el archivo así:sudo zic southamerica
    
#. Eso es todo.


Para comprobar el resultado se puede ejecutar

    ::

        zdump -v America/Caracas 
