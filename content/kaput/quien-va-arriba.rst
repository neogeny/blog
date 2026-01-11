Quién va arriba?
================

:date: 2007-07-31
:slug: quien-va-arriba
:author: Apalala

.. :tags:
.. :category:
.. :summary:


Hace unas semanas compré un computador de escritorio con "todos los
hierros" que el presupuesto predeterminado podía lograr: Pentium D a 3.0
GHz, 1 Gb de RAM, 160 Gb en disco, etc., más un monitor de 19" a
1990x1400.

Una de las razones por las cuales compre desktop es porque estoy harto
de las laptops, las cuales se han convertido en artículos desechables al
cabo de año y medio de uso; pero eso es tema para otro post.

Mi otra intención (ya que estoy decidido a mantenerme alejado de
Windows Vista el mayor tiempo posible) era la de correr Windows XP
(todavía necesario) sobre Linux en la nueva compu. Esto es lo que
aprendí:

#. KVM, el sistema de virtualización imbuido en el kernel de Linux solo
   corre en compus cuyo chipset y bios tienen soporte para
   virtualización asistida por hardware. Descubrí tarde que no todos los
   motherboards se prestan para eso.

#. Otras opciones de virtualización sobre Linux, como
   `VirtualBox <http://www.virtualbox.org/>`__, funcionan en forma
   excelente. Con el doble CPU, Windows XP corrió sobre Linux con el
   mismo o mayor rendimiento que en mi laptop con un Centrino de 1.8
   Ghz.

#. Hacer que Linux reconozca el hardware que uno tiene a la mano sigue
   siendo un reto inmenso no tanto de hackeo sino de tiempo disponible
   para investigar, jurungar, y luego documentar el cambio de
   configuración que funcionó. Como no tengo motivación para esas cosas,
   instalé Windows XP, que tiene drivers para todo, para luego
   virtualizar Linux sobre XP (lógico, no?).
#. No he probado VMWare en la nueva compu, pero tanto VirtualBox como
   `VirtualPC <http://www.microsoft.com/windows/products/winfamily/virtualpc/default.mspx>`__
   funcionan bastante bien virtualizando Linux sobre XP, pero con un
   rendimiento considerablemente inferior al de correr XP sobre Linux.

Conclusión
----------

Hay que adquirir harware pre-certificado para Linux (al menos mientras
los fabricantes terminan de montarse en la onda) para evitar el tipo de
regresiones que yo tuve que hacer. Linux es el SO que toma mejor
provecho del hardware base, y es la elección obvia por muchas razones,
incluso cuando es necesario seguir corriendo Windows. Pero hay que
emplear el tiempo de investigación necesario para asegurarse de que el
hardware disponible va a subir en Linux en unas pocas horas de
configuración en vez de en semanas hacking.
