Setting up a CVS repository on Linux
====================================

:date: 2006-09-05
:slug: setting-up-a-cvs-repository-on-linux
:author: Apalala

.. :tags:
.. :category:
.. :summary:


| 

    It takes more than you'd think to bootstrap a team

One might think that it is enough to create a directory under
**/var/lib/cvs** to get a new CVS repository working for a project. My
experience is that it takes much more to set up a CVS repository that
can be securely and seamlessly shared among members of a project group.

What follows is based on Fedora (RedHat) distributions of Linux, but it
will work with any other distribution with very few changes.

Work as **root**
~~~~~~~~~~~~~~~~

Most of the commands that need to be executed for this setup are
privileged, so it is much easier to work as root. So do:

::

    $ su

or try:

::

    $ sudo su

If the first doesn't work (it doesn't on most Debian-based systems).

Install CVS
~~~~~~~~~~~

Update to the latest version of CVS:

::

    $ up2date cvs

Create a user for your project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are many way to set up directories for CVS. Many just create
directories (modules in CVS parlance) under **/var/lib/cvs**. In my
experience it is best to create a user/group pair for each project with
the corresponding directory under **/home**. That makes permission
management much easier and provides an obvious place to store
project-related files, create *cron* tasks, etc.

::

    $ adduser myproject

Create a directory for the CVS repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This needs little explanation:

::

    $ mkdir /home/myproject/cvs

Set directory permissions
~~~~~~~~~~~~~~~~~~~~~~~~~

The basic permissions must give read, write, and navigation abilities to
members of the project group, and to no one else.

::

    $ chmod ug+rwX /home/myproject$ chmod ug+rwx /home/myproject/cvs$ chmod o-rwx --recursive /home/myproject

Set the SGUID bit on the CVS repository directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's a little known fact that setting the SGID (Set Group Id) bit on a
directory makes files and directories created under it inherit the
permissions of the parent. Setting the bit for a CVS repository is
indispensable because otherwise users will be able to create archive
files which only they can change.

::

    $ chmod g+s /home/myproject/cvs

More information on the SGID bit over directories can be found
`here <http://www.library.yale.edu/~lso/workstation/docs/permissions/sgid.htm>`__.

Initialize the CVS repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

$ cvs -d /home/myproject/cvs init

If you execute:

$ ls -l /home/myproject/cvs

You should see this:

::

    drwxrws--- 3 myproject myproject 4096 2006-09-05 11:26 CVSROOT

Create the root CVS module
~~~~~~~~~~~~~~~~~~~~~~~~~~

CVS has this somewhat confusing concept of *modules*. To make a
potentially long explanation short, it is best if you create a directory
under the CVS repository to serve as root for all project files under
version control.

::

    $ mkdir /home/myproject/cvs/myproject

Add the users to the project's group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you haven't created the users on the system, create them now:

::

    $ adduser john$ adduser mary

Because we're going to use SSH (Secure Shell) access to the cvs
repository, it is important that each user has their own Linux login.
Otherwise CVS won't be able to capture who changed what.

Now add the users to the project's group:

::

    $ usermod john -G myproject$ usermod mary -G myproject

Install and configure SSH
~~~~~~~~~~~~~~~~~~~~~~~~~

$ up2date ssh

You might want to tighten up security by restricting which users have
SSH access to the server, and you might have to tweak your firewall to
let traffic go through the SSH port (port 22).

Test
~~~~

You can try checking out the (for now empty) root module from CVS using
a remote desktop or server. The first step is to tell CVS that you want
to use SSH for remote repository access (something you might to set up
permanently in your **~/.bashrc** file or the likes):

::

    $ export CVS_RSH=ssh

Next we extract the repository root:

::

    $ cd ~ # switch to our home directory$ cvs -d :ext:myserver.com:/home/myproject/cvs co myproject

If you execute:

::

    $ ls -l myproject

You should see something like:

::

    drwxr-x--- 2 myname myname 4096 2006-09-05 11:39 CVS

If that works, you're almost a 100% set. "Almost", because on some
systems you might need to set each project group member's UMASK to 007
in their **~/.bashrc** to avoid creation of archive files in the CVS
repository which are not group writable.

**That's it!**

As you many have noted, most of the steps in this process can be easily
automated using a shell script that is invoked as:

::

    $ addproject myproject

That is exactly what I've done for gigs in which projects are created
frequently. In this case, writing the script is left as homework =)