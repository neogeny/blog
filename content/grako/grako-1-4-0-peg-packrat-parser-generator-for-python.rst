Grako 1.4.0 PEG/Packrat parser generator for Python
===================================================

:date: 2013-05-02
:slug: grako-1-4-0-peg-packrat-parser-generator-for-python
:author: Apalala

.. :tags:
.. :category:
.. :summary:



|image0|

Grako 1.4.0 has been published with this changelog:

-  BUG! Sometimes the AST for a closure ({}) was not a list.
-  Semantic actions can now be implemented by a delegate.
-  Reset synthetic method count and use decorators to increase
   readability of generated parsers.
-  The Grako EBNF grammar and the bootstrap parser now align, so the
   grammar can be used to bootstrap Grako.
-  The bootstrap parser was refactored to use semantic delegates.
-  Proved that grammar models can be pickled, unpickled, and reused.
-  Added the antlr example with an ANTLR-to-Grako grammar translator.
-  Changed the licensing to simplified BSD.


.. |image0| image:: /images/grako.png
