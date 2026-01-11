Snake charming
==============

:date: 2000-06-19
:slug: snake-charming
:author: Apalala

.. :tags:
.. :category:
.. :summary:


*Like the reptile it's named after, Python squishes problems little by
little.*

Today I spent the whole afternoon with a snake. I've known Python for
several years now -- the oldest version of Python on my hard drive is v.
1.3, dated March 1996 -- and I've studied and played with the language
several times. But it wasn't until today that I actually tried to do
something useful with it.

The task at hand? I wanted to lay out the articles I've written during
the last couple of months in an HTML format that is consistent with that
of the rest of my Web site. My site is a modest one, and producing the
few pages of HTML in it is fairly easy, even by hand. But doing the same
formatting for a dozen or so articles (and the many more to come), even
with a WISIWYG editor, is the kind of task that makes us lazy
programmers start thinking about a better way: writing a program.

Figuring out that the formatting of the articles had to be automated
was the easy part. Deciding on how to automate the process was more
difficult. It's not that I lacked a tool to do the job, but rather that
I didn't know the right tool to use. One of the mantras of programming
is "When in doubt, start hacking," so I did. After some experimenting
with Perl, SED, and AWK, I remembered Python, a programming language
often touted as capable of accomplishing everything easily. I hacked my
way out of this problem with Python, and I wasn't disappointed.

A breed apart
-------------

Python is an interpreted, interactive, object-oriented programming
language that offers advanced features like modules, exception handling,
and classes. Python's syntax is simple, yet the native support for
first-order functions (functions you can assign to variables or pass as
parameters), lists, tuples, and maps (associative arrays) make it quite
powerful. The compiler/interpreter and libraries are extensible, very
portable, and open source. The language has been ported to the most
diverse platforms, including several brands of Unix, Linux, MacOS,
MS-DOS, Windows, and OS/2. Python libraries support everything from
string handling to system calls to concurrency to Internet programming
-- including sockets, HTTP servers and clients, and HTML and XML parsing
and formatting.

The greatest strength of Python is that it lets you think big, yet
start small. Using Python, you can expand a four- line procedural or
functional program into a full- blown web of concurrently interacting
objects. Like the snake, Python can squish a problem, little by little.

Getting the snake out of the basket
-----------------------------------

The simplest automated scheme I could think of was to strip the
original articles of everything but the basic HTML and embed them into a
pre-formatted template, much like is done with server-side includes. I
wrote the template and placed the tag right in the middle of it. I
launched a browser with the Python HTML documentation, opened a console
window, and started hacking.

To begin, I needed to open the template and target files. Python is an
eclectic language; it borrows concepts from procedural, functional, and
object-oriented programming languages. Whatever seems to work well,
Python does. According to the Python documentation, to open a file I
just needed to call the open function:

::

    template = open("template.html")
    target = open(article.html')

You don't have to declare variables in Python and you can enclose
strings in either single or double quotation marks.

Reading the files came next. Python provides an assortment of file
reading functions, the simplest of which was precisely what I needed. In
Python, the result from a call to open is an object of File type.
Calling read on the object returns the complete contents of the file as
a string:

::

    template_text = template.read()

I finally opted for the more straightforward:

::

    template = open("template.html").read()
    target = open('article.html').read()

To embed the article in the template I needed a text substitution
function, the simplest of which was to be found in the string module. As
in many other languages, Python modules are used to hold related stuff
together. Module string holds a set of useful string manipulation
functions. The one I needed was the replace method. To use a module, you
have to import it like this:

::

    import string

After importing the module, I just had to call replace to do the
substitution:

::

    result = string.replace(template, "", target)

So far, the complete Python program I had written looked like this:

::

    import string
    template = open("template.html").read()
    target = open(sys.argv[1]).read()
    result = string.replace(template, "", target)
    print result


I saved the program to a file, then made a couple of adjustments to
make it more generic. For example, I made the program work on any file
passed as a command-line parameter by using the functions available in
the sys module. Here was the program after the changes:

::

    import string
    template = open("template.html").read()
    target = open(sys.argv[1]).read()
    result = string.replace(template, "", target)
    print result

Now I could call the program up on any of my articles from the command
line, like this:

::

    python format.py article.html > formatted_article.html



Try, try again
--------------

Alas, my initial attempt at automating the formatting of the articles
wasn't good enough. For starters, it didn't cope with important HTML
meta-information such as the
tag, which should be included in every HTML file. Nor did it deal with
the specific placement and formatting I wanted to give to the article's
abstract or the author's name (mine). But Python was still up to the
task. First I edited the articles and added the relevant
meta-information on the very few lines of each file. Then I told Python
to read the files as a list of lines instead of as a string, like this::

    raw = open(filename).readlines()

Then I retrieved the information items by indexing the already read
list:

::

    title = raw[0]
    author = raw[1]
    text = string.join(raw[2:])

To convert the non-field article text from a list of lines back into a
string, I used the string module's join function, which does exactly
what you'd expect. The expression raw[2:] retrieves the items from
position 2 onward, as a new list.

I added a couple of special tags ( and ) as to the template to embed
the new information at the right places. After adding the replacements
for the new tags, the code looked like this:

::

    import string
    template = open("template.html").read()
    target = open(sys.argv[1]).read()
    result = string.replace(template, "", target)
    result = string.replace(template, "", title)
    result = string.replace(template, "", author)
    print result

That was it for version 1.0: a seven-line program. The current version
of the program (which you can
`download <http://www.suigeneris.org/%7Ejuanca/writings/format.py>`__
from my Web site) is 48 lines long and handles the article abstracts,
parses the article's date and formats it in two different ways, and
manages the hyperlink to the article's original publication URL. Had I
been inclined to do so, I could have parsed the original HTML files to
retrieve the chunks of information using Python's XML and HTML parsing
libraries. I could have also used the built-in dictionary (map) type to
make the text substitutions more generic, and the regular expressions
library to get really fancy. I didn't, though, because my 48-line
program already did what I needed. I'm fond of the KISS principle,
especially in Extreme Programming. My philosophy: Do the simplest thing
that could possibly work.

| Originally written for *In Publishing LLC*
| Copyright © 1999 Inprise Corp.
