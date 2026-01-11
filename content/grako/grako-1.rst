GRAKO
=====

:date: 2013-01-09
:slug: grako-1
:author: Apalala

.. :tags:
.. :category:
.. :summary:





After my difficulties translating SoftAG Natural using ANTLR v3, and a
new request to do the likes with COBOL, which is a programming language
as large and as ambiguous, I decided to explore other options.

I found that most of the solutions out there are lack a maintainer,
lack users, or lack significant projects that use them. That scenario
maid ANTLR the only reasonable option, which meant going though the same
problems I went through with Natural while dealing with COBOL.

So, with a bit of desperation, a bit of arrogance, a bunch of ideas
about how things should work, and unbelievable support from my boss, I
wrote an EBNF to memoizing-PEG parser compiler in Python. It's callked
GRAKO, and it's GPL open at:

    `https://bitbucket.org/apalala/grako/ <https://bitbucket.org/apalala/grako/>`__


The tool must be called "beta" because it hasn't yet seen a major
project delivered using it, but the consistency checks I wrote are the
nastiest I could think off: the bootstrap parser can parse a grammar for
the GRAKO EBNF description, and generate a parsing engine that can parse
the same input again, and generate a structured and readable Python
program that can do the same.

On the other hand, a GRAKO generated parser is parsing 1.8 million
lines of COBOL in about seconds. It's over 500 programs, of which about
200 fail to parse, and manual inspection says that the failures are
about invalid COBOL, and not grammar, or generated parser errors.

The reasons why I built this tool are the ones you've seen me discuss
in the current and previous incarnations of this forum:

#. To deal with languages like COBOL or NATURAL, in which important
   statement words (can't call them keywords) may be used as identifiers
   in programs, the parser must be able to lead the lexer. The parser
   also must lead the lexer to parse languages like Ruby.
#. When ambiguity is the norm in the parsed language (Natural, Cobol),
   the grammar becomes contaminated with lookaheads (just to make the
   parser greedy) in ANTLR v3, and unknowns for me in v4 (because I
   haven't tried).
#. My opinion, after the experience with Natural, is that semantic
   actions like AST transformations or whatever DO NOT belong in the
   grammar. Semantic actions in the grammar create yet another
   programming language to deal with (the source language, ANTLR,
   ANTLR+semantics, and target language). In fewer words, it is
   impossible for me to find a programmer to whom delegate the current
   grammar for Natural, while the current COBOL grammar is approachable
   to anyone with a CS degree, and the generated code approachable by
   anyone with sound knowledge of Python.
#. (Probably a restatement of the above) Pre-processing (like includes,
   or COBOL's fixed column format), tree construction, translation,
   interpretation, etc., belong to soundly developed program code, and
   not in the grammar.




I have deadlines to meet using GRAKO, and, to be honest, I don't know
if I'll succeed. I do know that ANTLR is sound and field proved (even by
me!), so I could fall back to it eventually. But currently, I'm placing
my bets on doing things in a simpler way::

    $ python -c "import this"
