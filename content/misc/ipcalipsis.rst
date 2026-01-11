¿IPcalipsis?
============

:date: 2011-02-04
:slug: ipcalipsis
:author: Apalala

.. :tags:
.. :category:
.. :summary:


¿Se acabaron las direcciones IP?

Las `direcciones
IP <http://es.wikipedia.org/wiki/Direcci%C3%B3n_IP>`__ son la suerte de
*números telefónicos* que los dispositivos conectados a la Internet usan
para ubicarse y comunicarse unos con otros. Hoy corre bajo el titular
*IPcalipsis* la voz de que `IANA <http://es.wikipedia.org/wiki/Iana>`__,
el organismo encargado de administrar las mas de cuatro mil millones de
direcciones IP, acaba se asignar el último bloque que tenía disponible y
que, por tanto, *se acabaron las direcciones de Internet*.

No es tan sencillo. Para comenzar, desde hace años se viene trabajando
en reemplazar el sistema de direcciones actual
(`IPv4 <http://es.wikipedia.org/wiki/IPv4>`__) por uno
(`IPv6 <http://es.wikipedia.org/wiki/IPv6>`__) con tantas direcciones
como estrellas hay en una galaxia, en un proceso que recuerda el paso de
los números de teléfono de cinco, a seis, a siete, hasta el actual
estándar de hasta catorce o más dígitos para una llamada a un número
telefónico en otro país.

Además:

#. Las direcciones IP no se gastan. Son completamente reciclables, y
   pueden compartirse.
#. Lo que se agotó fue el registro de primer nivel, y **NADIE** sabe
   cuantas direcciones IP están todavía disponibles en el resto de los
   varios niveles antes de llegar a los ususarios finales, ni cuántas
   están siendo subutilizadas. 
#. La mayoría de los equipos conectados a Internet  (como mi router) no
   soportan IPv6, así que de nada serviría que los proveedores  lo
   soportaran.
#. Son muchas las direcciones IP públicas que están sin uso y pueden
   recuperarse. Mi proveedor me entrega dos direcciones IP públicas, de
   las cuales nunca he usado más que una.
#. No todo el que tiene asignada una dirección IP pública (que son las
   que se agotaron) la necesita. La mayoría de los usuarios de Internet
   no la requieren porque no administran sus propias redes sino que sólo
   se "conectan". Esas direcciones también son recuperables.
#. Existen las *direcciones IP privadas*, como las que asignan los
   routers, las cuales no pueden agotarse porque son reutilizables, y
   existen en bloques que van desde 256 hasta más de 4 mil millones de
   direcciones. En mi red  hay ocho dispositivos conectados a la
   Internet, todos usan la misma dirección IP pública, y todo funciona
   perfecto. Cada dispositivo tiene asignada una *dirección IP privada.*
#. De nada le sirve a un proveedor de Internet en particular soportar
   IPv6. Para que IPv6 funcione, **tiene que soportarlo la Internet
   completa**. La Internet una estructura de "tela de araña" pero con
   organización jerárquica, por lo que un cambio tan pervasivo tiene que
   ocurrir de arriba hacia  abajo; **el cambio no puede hacerse de abajo
   hacia arriba**.
#. Existen numerosos *parches y trucos* que los administradores de redes
   pueden usar para extender el uso de las direcciones IPv4 que
   administran. Uno sencillo, pero efectivo de aplicar, es asignar
   direcciones *sólo* a los equipos *conectados y* *encendidos*\ (parece
   obvio, pero no siempre se aplica). Otro *truco* es reducir el tiempo
   de asignación (leasing) de las direcciones IP que se administran para
   que haya mayor rotación de las mismas entre los usuarios.

La situación de las empresas de Internet en el mundo en cuanto a sporte
de IPv6 es muy parecida, pero **no va a ocurrir ninguna crisis.** Lo que
va a ocurrir es una transición lenta, de al menos un par de años, de la
cual los usuarios de Internet  van a enterarse sólo cuando les
suspendan por unas horas el servicio mientras se hacen reconfiguraciones
en los servidores de su proveedor de Internet.

¿Cuánto  tiempo va durar la transición a IPv6? Nadie lo sabe, en parte
porque la transición no estará completa hasta que los usuarios finales
hayan reemplazado todos los dispositivos de red que poseen por unos
compatibles con el nuevo protocolo. 

Mientras tanto las direcciones IPv4 se harán poco a poco más escasas,
haciendo que las fuerzas económicas eleven sus precios, aparezcan las
direcciones que están siendo desperdiciadas, y el *mercado* se equilibre
de manera que las direcciones estén disponibles, tal vez a un precio un
poco más elevado. No debemos preocuparnos mucho por la posibilidad de
acaparamiento o especulación, ya que IANA, el organismo regulador (`a
cargo del Departamento de Comercio de
EEUU <http://en.wikipedia.org/wiki/Internet_Assigned_Numbers_Authority#Oversight>`__),
tiene plena autoridad sobre la asignación de direcciones IP a todo
nivel.

Al final, lo más probable es que pocos se acuerden de cuándo se agotaron
los números telefónicos de seis dígitos, ni de cómo el mundo siguió
andando mientras ocurría la transición a números más largos. La
transición de IPv4 a IPv6 va a ser algo parecido.

Un problema mucho más grave y más difícil de solucionar es que cualquier
dispositivo conectado a cualquier red (no sólo a la Internet) debe
poseer un identificador único conocido como Dirección MAC (`MAC
address <http://en.wikipedia.org/wiki/MAC_address>`__), y **los MAC  no
son compartibles ni reciclables, y se están agotando a un ritmo
acelrado**. Es más complicado porque una solución requiere del concurso
de todos los fabricantes de dispositivos con capacidad de red en el
mundo, pero ya están en curso los planes para una transición a un número
mayor de identificadores, y lo más probable es que pocos nos demos por
enterado de cuando participamos en el cambio.
