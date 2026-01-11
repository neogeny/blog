Pulseaudio Sucks!
=================

:date: 2010-04-07
:slug: pulseaudio-p-sucks
:author: Apalala

.. :tags:
.. :category:
.. :summary:


Either that, or `Ubuntu <http://www.ubuntu.com/>`__ hasn't implemented
it well either on Karmic or Lucid. Many people complain all over the Web
about problems like the ones I've experienced:

-  Skips, skips, skips. Launch an apllication, skip; open a new page on
   the browser, skip; switch worskpaces, skip; do almost anything but
   stay still, skip.
-  Moving the balance control changed the volume, and made the balance
   jump to wherever it wanted.
-  The audio options in Skype were all *Pulse Audio Server*, which had
   me jump through hoops every time I wanted to set up an audio
   conference using my headset.
-  Volume and equalizer settings got lost after logout.
-  The equalizer worked or didn't at its own discresion.
-  Etc.

The almost unanimous advice about how to solve to the above problems
according to the Web is to get rid of
`Pulseaudio <http://en.wikipedia.org/wiki/PulseAudio>`__\ and make
`ALSA <http://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture>`__
and `ESound <http://en.wikipedia.org/wiki/Enlightened_Sound_Daemon>`__
take over, so that's what I did... not without problems, because Ubuntu
has been embedding Pulseaudio into the desktop the hard way:

-  The volume control on the toolbar disappears, and
   System/Preferences/Sound stops working. To work around that I
   installed the GNome Alsa Mixer, and docked it to the toolbar. I
   haven't been able (haven't known how) to make the GNome Volume
   Control work again.
-  No more equalizer. To fix that I ditched the `Rhythmbox Music
   Player <http://projects.gnome.org/rhythmbox/>`__ that Ubuntu
   installs, and started using `Banshee <http://banshee-project.org/>`__
   instead. That not only gave me an equalizer, but also inter-song gain
   control, and randomization that works, all with an interface very
   similar to that of Rhythmbox, and with all the goodies.
-  The sound is great.
-  Skype keeps the correct settings for teleconferencing between
   sessions.

I'm running the first beta of the `Lucid Lynx <https://wiki.ubuntu.com/LucidLynx>`__ now, but the issues were the
same with Karmic. The feeling I get after having had to work hard to get
my audio the way I wanted it is that having distributions couple to one
specific option when there are many is very much agains the freedom to
choose that has always characterized Linux.
