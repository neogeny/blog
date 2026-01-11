The true meaning behind open source licenses
============================================

:date: 1999-10-03
:slug: the-true-meaning-behind-open-source-licenses
:author: Apalala

.. :tags:
.. :category:
.. :summary:


*What does all this licensing stuff really mean?*

I develop software for a living, so my position regarding third-party
software has always been pragmatic: consider the cost and evaluate how
well each solution meets your requirements. Most open source software is
licensed free of charge. But does software that is licensed for free
really have zero cost?

`Property rights <http://electriciti.com/1.01/property-wp.html>`__ --
who has the right to own what -- are at the ideological core of
political systems and are one of the fundamental individual liberties in
a capitalist society. Software is considered a form of property by law,
so talking about software licenses -- including open source licenses --
in that context makes sense.

I'm not a lawyer, so none of my views or interpretations of this
matter would necessarily stand up in a court of law. Also, I'm talking
primarily about United States copyright law because the copyright
licenses I'll discuss were written in the US; the laws of other
countries and of the international community might be different.

Property law establishes three basic rights: the right to use, the
right to enjoy (profit from), and the right to dispose of the property.
When dealing with intellectual property, and more specifically with
copyrighted work such as software, such rights are exclusive to the
copyright owner. Most software licenses explicitly reference the right
to:

#. perform the work -- that is, to execute the software
#. prepare derivative works -- that is, to debug, patch, enhance, or
   otherwise modify the software
#. make copies of the work
#. distribute copies of the work
#. authorize others to exercise the above rights
#. sublicense the software (charge for it)
#. prevent others from exercising the above rights
#. transfer or license the above rights

I want to analyze several well-known (and some lesser-known) open
source licenses in terms of the three basic rights property law
establishes and the more specific rights held by copyright owners.
Politics and philosophy aside, I want to evaluate what the different
licenses mean to someone who develops software for a living, like me.

The licenses I'll be considering are those mentioned at the `Open
Source Initiative's <http://www.opensource.org/>`__ Web site: the `BSD
license <http://www.us.debian.org/OpenSource/bsd-license.html>`__; the
`MIT
License <http://geosci.uchicago.edu/paleo/csource/licenses/mit.html>`__;
the `Artistic License <http://language.perl.com/misc/Artisitc.html>`__;
the `Mozilla Public
License <http://www.mozilla.org/MPL/MPL-1.0.html>`__; the `GNU General
Public License <http://www.gnu.org/copyleft/gpl.html>`__ and its lesser
form, the `LGPL <http://www.gnu.org/copyleft/lesser.html>`__; as well as
lesser-known licenses like the `Java Community Source
License <http://www.sun.com/software/communitysource/index.html>`__ and
the `IBM XML4J <http://www.alphaworks.ibm.com/formula/xml/>`__ (XML for
Java) evaluation and commercial licenses.

In the Public Domain
--------------------

We should first look at one of the most widely used terms in open
source distribution that has not yet been certified by the Open Source
Institute: placing the work "in the public domain." A work placed in the
public domain has the same legal status as one for which the legal
copyright term (usually 50 years after the death of all the authors) has
elapsed. This condition is particularly interesting because the rights
to use and profit from the work (execute, copy, and distribute the
software) can be exercised by anyone, yet the ultimate right of
disposing of the work (the right to authorize or restrict other's rights
to it) belongs to no one and, therefore, cannot be exercised.

Software placed in the public domain essentially follows the same
copyright law as the works of long-dead literary and musical authors.
You can perform (execute) the works of Shakespeare, copy them, and
distribute them, but remember that derivative works, compilations, and
specific performances can have their own lawful copyright owners. You
can include public domain software in your own work, modify it, copy it,
and talk about it in publications and at conferences. You can't do the
same with someone else's work, however, just because it happens to use
or contain public domain work. You're otherwise free to derive any
profits from public domain software.

Public domain software is unique in that it is the only form of work
whose disposal rights are not retained by anyone. Every form of software
licensing reserves rights 5, 6, and 7 for some entity, including the
right to license work under a different scheme whenever desired. From a
business perspective, it's guaranteed that legal claims of copyright
violation can not be brought against users of software that is in the
public domain.

The least restrictive licensing
-------------------------------

Software licensing schemes always reserve the right to dispose of the
work (grant, restrict, transfer, and license the rights). This is
redundant because licensing can only exist if someone holds those basic
rights, unlike work placed in the public domain. All open source
licenses have that element in common, but differ in the other rights
they grant or restrict.

The least restrictive form of software licensing is that which
reserves only the right to disposition. The BSD and MIT licenses, for
example, grant ample rights of use, creation of derivative works, and
redistribution (as long as the right to dispose of the work is
explicitly reserved to the original authors). Included is the right to
make different licensing arrangements with whomever the licensee sees
fit. The Artistic (Perl) license is somewhat less clear in its section
3, which addresses copying and modification of the original "package,"
but does not talk about distribution.

Tightening the reins
--------------------

Most frequently, open source licenses grant ample rights for use of
the software and creation of derivative works, but restrict distribution
in some important way. The four most common restrictions on distribution
are:

-  You may only distribute the software and the modifications within
   your company or institution (an aspect the Artistic License).
-  You may only distribute the software and the modifications in object
   (compiled) form as long as some value-added is provided (the XML4J
   commercial license).
-  You may only distribute the software and the modifications for free
   (Artistic License).
-  You must provide the source to all your modifications, or otherwise
   guarantee that users of your software can get hold of the source free
   of charge (the GPL).

These restrictions mainly affect how you profit from the intellectual
property. The only restrictions made by the controversial GPL are
restrictions on distribution.

Normally, these kinds of licenses don't place restrictions on the work
created with the software, which gives such licenses a broad range of
uses. This applies to end-user applications -- such as word processors
and spreadsheets -- and to most of the tools used in software
development, even commercial ones like compilers, libraries, editors,
and text manipulation and make tools.

Some other licenses place absolute restrictions on distribution in
order to avoid so-called "forking." As a result, most of the
enhancements end up in the primary source base. But other licenses
restrict distribution just to maintain control over the software. I've
known only a few licenses that do this.

The most restrictive licenses
-----------------------------

Paradoxically, one of the most restrictive licenses -- the GPL -- is
very liberal about redistribution rights. Under the GPL, you can
distribute the original work or its derivatives to whomever you like, as
long as you make readily available the source to the original work, the
modifications you obtained, and any modifications you made. Any licenses
you give must also follow the GPL restrictions.

Many source code licenses restrict the use that can be made of the
software. Such is the case with the Java Community Source License, which
appears to restrict free use to research. Other uses require that
compatibility tests be made and royalties be paid. Other licenses, like
the XML4J Evaluation License, restrict the use to that which is "lawful
and non-commercial." More restrictive licenses grant these rights only
for a limited period of time.

Some would argue that source licenses that restrict the use or the
creation of derivative works are not really open source. This, however,
is the most common form of licensing use in academia, which is driving
the so-called open source movement and is a main provider of useful
source code.

Surprisingly, licenses that completely prohibit executing the software
can still be useful. The trend is a new one, but I've seen it applied to
the source code in books about algorithms and coding techniques. These
books provide source code, but they restrict its use to study purposes
only. You cannot copy the software, be it directly, by optical
recognition, or even by typing it in, which eliminates any possibility
of passing it through a compiler, much less executing it.

If the license fits
-------------------

If all you want to do with a given open source package is use it as a
tool to produce work separate from the package, then most open source
licenses will do. Tools like compilers and text editors fall into this
category. Libraries and interpreters might not, so pay attention.

For other purposes, choose public domain software. Or, if you want to
distribute your software commercially but do not want to distribute the
source to the modifications you made, go with a license like the MIT or
the BSD. The GPL and LPGL are good choices if you don't mind
distributing your source code.

Licenses like the Java Community Source License are so complicated
that I'd keep away from the code unless I could count on the services of
a good lawyer.

In all other cases, read carefully and look for the following keywords
and phrases: use, copy, distribute, modify, derivative works,
sublicense, and charge. Those words and phrases describe the rights that
can be claimed on copyrighted work, and they will be specifically
mentioned in documents that grant or restrict them. When in doubt,
(gulp!) consult a lawyer.

If you're planning on distributing your own work as open source, then
I suggest you adopt one of the licenses mentioned at the Open Source
Institute's web site. I hope that my analysis will make the choice
easier. These licenses have already been reviewed by lawyers and, just
as important, they are free to use. Licenses can also be copyrighted,
you know, and not all licenses are open source.

| Originally written for *In Publishing LLC*
| Copyright © 1999 Inprise Corp.
