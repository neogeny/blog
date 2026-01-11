Back to XP
==========

:date: 2009-05-02
:slug: back-to-xp
:author: Apalala

.. :tags:
.. :category:
.. :summary:


There are historical and circumnstantial reasons for my continuing to
run Windows. My first personal computer run HP Basic, the second CP/M,
the third MS/DOS, and after a short and unsuccessful stint with a Mac,
my professional work started with MS Windows 2.0, and stayed on Windows
for two decades or so.

| 

But things have changed. These days I have to support only one Windows
application,and that's something that can be done over a virtual
machine. I have administrative access to several Windows servers for the
rest. It's true I am a Windows junky in being an expert in Excel, Word,
and Outlook, but that can be remediated.

| 

As anyone who has run Windows for a few years knows, there comes a time
in which the operating system becomes so unjustifiably screwed-up that
the only solution is to reinstall everything. Reinstalations are not
easy, and they are full of data-loss risks. Faced with the decision to
reinstall Windows XP, or give Windows 7 a test ride, I decided that the
time seemed right to switch away from WinXP. Ubuntu 8.10, which runs in
two of my computers, seemed a good choice.

| 

Requirements

| 

| 

-  Preserve my e-mail. Ten out of my 12 e-mail accounts go through
   gmail, and the other two through POP3 services that keep a week's
   worth of messages, so that seemed doable.
-  Preserve my data, mostly my projects and my photographs, but music
   and videos are in the list. Writing from Linux to NTFS partitions is
   still discouraged, but the available disk space (about 200Gbit) could
   be managed to deal with that.
-  I need a WinXP virtual machine to be able to run Intel Fortran and
   Borland (now Code Gear or something) Delphi 7. I already know that
   VirtualBox (http://www.virtualbox.org/) can do that.
-  Printing and scanning must work. Either a soft learning curve for
   other users, or moving the devices to one of the remaining Windows
   machines.

| 

| 

Outcome

| 

Yes. Why not let you know about the outcome first?

| 

I was not able to make the switch this time because of some unforseen
issues with Bluetooth, remote desktops, display configurations, and
learning curves, all of them things I could not deal with within the
weekend I had set for the switch.

| 

Ubuntu 9.04 came out during the effort, and several issues got fixed
with the upgrade. The details are below.

| 

Process

| 

| 

#. Backup, backup, backup.
#. Remove all the software that's not needed or that hasn't been used in
   a while.
#. Use `JkDefrag <http://www.kessels.com/Jkdefrag/>`__ to force files
   together at the begining of each disk.
#. Use `Partition
   Magic <http://www.symantec.com/norton/partitionmagic>`__ to resize
   partitions and leave lots of space for the new install.
#. Leave the existing Windows XP partitions alive, just in case, with
   enough free space (a couple of Gibits) to let them operate.
#. Install Ubuntu 8.10 AMD64 with default options using the Live CD.

| 

| 

Details abut the failed switch

| 

| 

#. The Ubuntu resolution had to be fixed manyally for my 19", 1440x900
   LCD display. Fixing the login screen was too difficult. The 9.04
   Ubuntu upgrade fixed all that nicely. SOLVED.
#. My Motorola/Widcom BLuetooth dongle get's recognized, but no devices
   are available. That leaves out my favorite mouse, a Logitech
   Bluetooth portable. ANOYING, but can be dealt with.
#. VPN connections to Windows servers are not working. ANOYING, probably
   a matter of a large learning curve.
#. Remote Desktop Connections suck because they are too slow compared to
   Windows RDP. VNC doesn't cut it. WORKAROUND, connect through a
   console (SSH) and launch graphic applications through X-Windows,
   which works fine.
#. RDP connections to Windows machines works much better in 9.04. The
   sound, wich was broken in 8.10 is back, and Ctrl-Enter for a windowed
   remote desktop works again. NICE. A WiFi RDP is still not good enough
   for things like YouTube: unexplainable and ANNOYING.
#. Chat works fine using Pidgin.
#. Skype did not work on AMD64. Maybe a SHOW-STOPPER.
#. The procedure for moving e-mail from Outlook to Thunderstorm and then
   to Evolution did not recover all emails. ANNOYING. I can get recent
   e-mail from GMail/POP3, and the history can ve recovered from (very
   backed up) Outlook .PST files. The trick for making these experiments
   with GMail is to prepend "recent:" to your login, whichever e-mail
   client you are using.
#. Office. I know that OpenOffice works, but there are enough
   differences with MS Office to make for a steep learning curve.
   ANNOYING, but expected.
#. Audio and video conferencing. Steep learning curve to know how to
   make Ekiga connect to the servers I use. ANNOYING to SHOW-STOPPER.
#. Ubuntu (aptitude) certified software is not always to the latest
   version. UNKNOWN.

| 

| 

Conclusion

| 

After Ubuntu 9.04, it is definitely worth it to spend another weekend
trying to make the switch.

| 

This report may be updated or corrected later.