Off XP and into Ubuntu
======================

:date: 2009-10-11
:slug: off-xp-and-into-ubuntu
:author: Apalala

.. :tags:
.. :category:
.. :summary:


This weekend I managed to take care of the
problems that
have kept me from transitioning my main workstation from XP to Ubuntu.

The details follow.

OS Version
----------

I downgraded to the 32-bit version of Ubuntu 9.04 (Jaunty). I found no
advantages in running at 64bit, and plenty of hoops to jump through to
to get some stuff to run. My opinion is that 64bit Linux is not yet
mature enough for a desktop.

Work
----

I still have projects that require Windows, and WinXP virtualized with
`VirtualBox <http://www.virtualbox.org/>`__ runs great,
indistinguishable from native (of course, the virtualized XP is
pristine, and doesn't have all the crap of the original, three-year-old
installation). VirtualBox complains that I assigned too much memory to
XP, but Ubuntu keeps running well when the virtual machine is up, which
only happens when I need to be in Windows mode. I used the "bridged"
network connection mode for the virtualized XP, so I can access it
remotely using RDP, netbios, or whatever.


The exercise of bringing
`TRANUS <http://www.modelistica.com/tranus_english.htm>`__ compilation
up on the virtualized XP helped me debug some unknown dependencies on
the way stuff in my old XP was configured.

Repartitioning
--------------

I found that Linux already has stable read/write access to NTFS
partitions through `ntfs-3g <http://www.ntfs-3g.org/>`__, so I decided
to keep my NTFS partitions:

-  On the first disk, the old Windows partition, for "just in case", and
   for copying stuff to the new virtualized XP (more on that later).

-  On the second disk, the partition where photographs, music, videos,
   and downloaded installers are kept. It has only 32GiB of free space
   left, so I expect to fill it up by the end of the year. When it
   becomes legacy, it won't matter the format it is in.

I upgraded the Linux partitions (the main one on the first disk, and the
auxiliary one on the second disk) to
`ext4 <http://en.wikipedia.org/wiki/Ext4>`__.

Printing
--------

Printing works great using Ubuntu printer sharing for Ubuntu machines,
and SAMBA for (the two remaining) Windows machines.

Scanning
--------

The `XSane <http://www.xsane.org/>`__ image scanner works great. I
hadn't grokked it on the first try.

Email
-----

Since a learning curve was inevitable, and almost all my email is routed
through GMail, I decided to try the GMail Web interface. It took some
time to get used to it, but it works great. I enabled offline GMail in
case my Internet connection goes down. I still log into the old XP every
once in a while to backup my emails locally to MS Outlook PST files.

Web
---

The beta version of Google Chrome for Linux is very stable. Oddly, it
still doesn't support Google Gears well, so I have to launch Firefox to
get my email backed up locally.

VPN
---

I still haven't been able to connect to a Windows PPTP server from
Ubuntu, but I can do it from the virtualized XP, so I consider this
issue dead, at least until Ubuntu 9.10 comes out by the end of the
month. I only need the VPNs for maintenance of Windows servers, so...

Bluetooth
---------

Still not working. I'll wait for Ubuntu 9.10 (Karmic Koala). I got a
Genius wireless (USB) mouse similar to the Logitech bluetooth I had to
deal with the mousing problem.

Remote Access
-------------

Oddly enough, remote access to my desktop using Ubuntu's Remote Desktop
Viewer sucks big time, but RDP to the virtualized XP using Terminal
Server Client shines. I tried xrdp, but it sucks worse than Remote
Desktop Viewer. I may try with plain tightvnc later. Remoting single
programs using plain XWindows works great, of course.

Office
------

OpenOffice is diffrent enough from MS Office than some pain ahead is for
sure. My MS Excel macros don't work with OO Spreadsheet, but I took care
of the most urgent need with the
`Hamster <http://projecthamster.wordpress.com/screenshots/>`__ time
tracking applet. MS Office documents, including invoices, print fine
from OpenOffice, and that takes care of the rest. As I mentioned in a
previous post, most of my writing is nowadays done on Web applications.
