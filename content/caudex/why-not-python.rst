Why not Python
==============

:date: 2007-05-15
:slug: why-not-python
:author: Apalala

.. :tags:
.. :category:
.. :summary:


*2010-03-12 Amendment: After doing the research right, my conclusion
is that the tools*\ ***are***\ *available for Python, that Python is an
excellent software development platform, and one that allows more
productivity than, say, Java.*

This article is about programming languages in the context of
professional software work. While considering several programming
languages with very attractive features for my next project I had to
take a pause and think about what the objective choice criteria should
be. My conclusion, as argued below is that programming language choice
should be dictated by programming pragmatics.

I've been programming for some thirty years now, twenty of them doing
it for a living. In my work I've come well acquainted with several
programming languages, including Fortran, Basic and Visual Basic, Pascal
and Object Pascal, C, C++, Java, and C#. During my university training I
had to deliver assignments in Concurrent C, Simula, LISP, and Prolog,
among others. I specialized in Computer Languages (compilers) and became
a professor of the subject later. I have studied the innards of
programming language implementation and have implemented several
programming languages from scratch. I've studied every promising
programming language I have come upon, including AWK, Perl, Python,
CAML, Haskell, Nemerle, Groovy, and Boo, among others.

My experience with compilers in particular has brought me some
understanding into what some call "programming language beauty", but
that subject is better dealt with
`elsewhere <http://www.dreamsongs.com/WorseIsBetter.html>`__.
Here I want to talk about what makes a programming language work.

By "makes it work" I mean which features of a programming language let
you get the job done in an efficient way. By "in an efficient way" I
mean in a way that lets you do better than just survive in the ever more
competitive field of software development.

It turns out that what makes a programming language work has less to
do with the idiosyncrasies of the language and much more to do with how
the language allows and provides for a good software writing
environment. The first breakthroughs in programming language, in
Fortran, LISP, and Algol68, consisted in raising the level of
abstraction so programs could be more about the solution space than the
machine. But the first breakthrough I remember, at least in the context
of programming languages that work, came with the
`Integrated Development Environment <http://en.wikipedia.org/wiki/Integrated_development_environment>`__
(IDE), the first comercialization of which was provided by
`Borland <http://en.wikipedia.org/wiki/Borland>`__ for
its `Turbo Pascal <http://en.wikipedia.org/wiki/Turbo_Pascal>`__
programming language.

Turbo Pascal came with an IDE that included an interactive,
full-screen editor, an incredibly fast compiler, and a debugger. It was
the first time that a generally-available tool reduced the
edit-compile-run-debug cycle to a matter of seconds. Today, IDEs are
common-place, and few professional programmers would think of doing any
significant work without the aid of one.

But what do IDEs have to do with specific programming languages? Turbo
Pascal was a simple, structured, and well defined language, and that
allowed Borland to build a very fast compiler that fitted in the few
kilobytes of RAM remaining in the machines of the time after having
loaded an editor.

By the end of the 1980's
`Apple's <http://en.wikipedia.org/wiki/Apple_Inc.>`__
`MacIntosh <http://en.wikipedia.org/wiki/Macintosh>`__
had made the advantages of
`Graphical User Interfaces <http://en.wikipedia.org/wiki/gui>`__ (GUIs)
for users
obvious, and GUIs became not just desireable but a necessity. The common
language of choice at the time was C. Programmers spent hours dealing
with single event-handling functions (like WindProc) and trying to
manage modal contexts through innumerable heap structures and casts,
while loading and exiting the GUI environment to run a command-line
compiler. The next breakthrough came again in the IDE. GUI designers had
been around for a while, but the linking between UI elements and
event-handling code had to be handcrafted. In 1991
`Microsoft <http://en.wikipedia.org/wiki/Microsoft>`__
launched `Visual Basic <http://en.wikipedia.org/wiki/Visual_basic>`__.
Visual Basic was built around an IDE that was itself graphical and that,
besides edit-compile-run-debug allowed hooking UI elements and events to
individual event handlers with a few clicks. Writing GUIs suddenly
became easy. The language feature that allowed for it all was Visual
Basic's component model, a form of object orientation.

As computers became more powerful, the size and complexity of the
programs we attempted to write increased. Programmers spent an important
part of their time studying and trying to memorize
`Application Programming Interfaces (APIs) <http://en.wikipedia.org/wiki/Api>`__ and third
party libraries. The next breakthrough came again in the IDE in the form
of context-sensitive help, and later in coding assistance. Instead of
having to browse over a huge API reference, the press of a key would
make the IDE produce the exact piece of documentation pertinent to the
context in the editor, or provide assistance in filling out a method
call.

The language features that enabled the new IDE functionality were
`static-typing <http://en.wikipedia.org/wiki/Static_typing#Static_typing>`__
and
`object- orientation <http://en.wikipedia.org/wiki/Object-oriented_programming>`__.
They are the same features that today enable automated
`refactorings <http://en.wikipedia.org/wiki/Refactoring>`__,
a functionality that is indispensable while we try to tackle even more
complex programs with
`iterative <http://en.wikipedia.org/wiki/Iterative_development>`__
and
`agile <http://en.wikipedia.org/wiki/Agile_development>`__
methods.

So, Which are the features a working programmer should look for in a
programming language? They are the ones that enable good tool support
for the act of programming: static-typing, and object-orientation. But
wait... Shouldn't the tools actually be available? Of course! This means
that the primary criteria for choosing a programming language is the
availability of the tools that make us efficient at writing the programs
we have to write. The breakthroughs in programming of today are still
happening in the tooling.

Fans of programming languages without those features or without the
tools available say that their language of choice allows them to think
better and write less code. That criteria is completely a non-issue for
the simple reason that modern programming language are converging to
include every characteristic that programming experience has identified
as useful:
`first-order <http://en.wikipedia.org/wiki/First_order_functions>`__
and
`anonymous <http://en.wikipedia.org/wiki/Anonymous_function>`__
functions,
`closures <http://en.wikipedia.org/wiki/Closure_%28computer_science%29>`__,
list and map
`literals <http://en.wikipedia.org/wiki/Object_literal>`__,
`partial classes <http://en.wikipedia.org/wiki/Partial_class>`__
and
`AOP <http://en.wikipedia.org/wiki/Aspect-oriented_programming>`__
features, `type inference <http://en.wikipedia.org/wiki/Type_inference>`__,
and `duck typing <http://en.wikipedia.org/wiki/Duck_Typing>`__.
You name it. None of then offset the pragmatic need for a complete
development environment that makes us competitive at what we do.
