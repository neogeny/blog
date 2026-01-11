Y2K: the beginning of the end?
==============================

:date: 1999-11-07
:slug: y2k-the-beginning-of-the-end
:author: Apalala

.. :tags:
.. :category:
.. :summary:


*Will open source software development be smothered by the patents
avalanche or help to end it?*

As *Developer News* correspondent Constance Petersen discussed in her
`article <http://community.borland.com/devnews/article/1,1714,20002,00.html>`__
last week, 5 Nov. was Burn All GIFs Day. The protest was organized by a
group of open-source developers and Webmasters opposed to the way Unisys
has exercised the patent it holds on the LZW compression algorithm used
in GIF files. The group proposes getting rid of all GIF files and
substituting files in open graphic file formats such as PNG.

Creating Burn All GIFs Day is just one of the actions taken by just
one of the groups who think that the patent system, as it applies to
software, is being abused.

Another event brought attention to patents last week. As
`CNET <http://news.cnet.com/category/0-1009-200-1426450.html>`__
reported, McDonnell Douglas received a patent for "windowing," one of
the most widely used (and intuitively obvious) Y2K problem-fixing
techniques. The company has handed the patent over to Bruce Dickens, the
technique's inventor. Dickens's attorney will reportedly contact Fortune
500 companies whose programmers have employed the patented technique to
request payment and negotiate licensing terms.

Aren't patent registration and enforcement just business as usual?
Doesn't the owner of a patent have the *right* to exercise it at will?
Yes, of course. But the issues related to this news are not about the
patent system per se. They revolve around the questionable validity of
specific patents and their effect on software development in general --
and especially, perhaps, the development of open source software.

The patent purpose
------------------

According to the text of most patent legislation, the main purpose of
the patent system is not to protect inherent, abstract rights, but to
enhance the common good by promoting the advancement of the arts and
sciences. The system works like this: The government grants inventors
legal monopolies over specific inventions and helps enforce the
monopolies. In return, inventors agree to publish the details of their
inventions and relinquish control over the inventions after a specified
period of time.

Inventors benefit because the government-enforced monopoly gives them
a better chance of recouping the expenses they incurred while developing
their inventions. Society benefits because the common pool of useful
knowledge is constantly augmented, and because everyone has free access
to inventions after patents expire. Patents are a good idea, especially
if you consider the consequences of the alternative -- inventors trying
to keep their inventions as secret as possible.

Not all patents are good deals for society, and the law foresees that.
To be awarded a patent, an invention must be novel; the inventor must
have been the first to invent that particular thing or method. It must
also be non-obvious, meaning the invention can't be a clear extension of
something that is already known. Granting patents for non-novel
inventions (prior art) would allow the imposition of royalties on
methods and practices that have been in wide use, even for a long time.
Patents for obvious stuff -- things that anyone with the right
background could have invented -- are a bad idea and are therefore not
granted.

So what's all the fuss? The problem `according to
analysts <http://www.wired.com/wired/archive/2.07/patents_pr.html>`__,
is that patents *are* being granted in increasingly large numbers for
obvious and non-novel inventions, which defeats the whole purpose of the
patent system. The problem is exacerbated because, as intellectual
property attorney Steven Young explained in a recent `Slashdot
feature <http://www.slashdot.org/features/99/10/19/1032254.shtml>`__,
there is no reasonable way to protect against patent liability. Becoming
informed about the millions of patents, even just the subset that is
relevant to your business, is not at all easy. Patents related to very
specific areas of knowledge number in the tens of thousands. Some
conservative estimates predict that 100,000 new software patents will be
granted this year in the United States alone.

Not a target, but a cure
------------------------

The `League for Programming Freedom <http://lpf.ai.mit.edu/>`__ site
at MIT offers a wealth of information about the patents problem and how
it affects software development. The LPF predictably opposes software
patents altogether, but the information on its site about the use and
abuse of patents is interesting even if you don't share their views.

To protect themselves against the patent avalanche, large companies
seem to be filing for patents on everything imaginable. The strategy is
to use patents as legal weapons against the dubious patents of others,
but this practice is only serving to make the problem worse. Patent
portfolios are being created mainly as a means of defense, but some
developers have begun to
`worry <http://www2.linuxjournal.com/cgi-bin/frames.pl/articles/currents/003.html>`__
about what could happen to the open source movement if companies decide
to try to enforce their patents -- which exist for Save As commands,
multicolored option lists, and other code elements -- against software
projects like Linux.

Is that likely? I don't think so. Some of the companies that hold
large patent portfolios (most notably
`IBM <http://www.patents.ibm.com/>`__) have already positioned
themselves strongly in support of open source software, and they're
likely to defend open-source projects. Because of the open,
collaborative nature of open-source efforts and the peer-recognition
culture behind them, many open-source projects maintain detailed logs of
who did what and when, and where further information about the
techniques and algorithms used can be found. Those logs may be some of
the best documented proof of previous art that can be used in court to
challenge questionable patent claims. Open-source software would not
become the target of the patent craze, but a good part of the cure.

Curbing the craze
-----------------

The windowing technique patented by McDonnell Douglas interprets years
expressed in two digits as belonging to century 2000 if the value is
less than a specific, context-dependent threshold. For example, "15" is
interpreted as "2015" instead of "1915," while "90" is interpreted as
"1990." Windowing is a popular fix for Y2K problems because it is simple
to understand and often easier to implement than other kinds of fixes.

Is the patent on windowing valid? That will be for the courts to
decide. The U.S. lacks administrative procedures to challenge a patent
after it has been granted, so the issue must be resolved in court.

Meanwhile, companies that have used the windowing technique are
legally bound to comply with the conditions set forth by the patent
holder. Abandoning the software or implementing a different fix so close
to the dreaded Y2K date is out of the question. Neither the lack of
knowledge about a filed patent nor the intention to challenge it is a
legal basis for infringement. Analysts contacted by CNET predict that
larger companies will just pay the fees and write them off as part of
their Y2K compliance expenses, but smaller companies may want to fight
the patent in court.

Even if the patent on windowing is valid, pursuing its enforcement so
close to a global death-march deadline seems like placing the sword at
the throat of someone who's already against the wall. It has the sour
taste of extortion about it. It's far from clear if and how society can
benefit from patents like this.

There's a chance that the Fortune 500 giants will join with the
smaller companies to try to set legal precedent against dubious patents.
Maybe Y2K will mark in more than one way the beginning of the end of the
patent craze.

| Originally written for *In Publishing LLC*
| Copyright © 1999 Inprise Corp.
