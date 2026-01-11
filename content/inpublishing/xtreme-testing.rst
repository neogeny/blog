Xtreme testing
==============

:date: 1999-10-17
:slug: xtreme-testing
:author: Apalala

.. :tags:
.. :category:
.. :summary:


*Extreme programmers brave the open source slopes.*

You can't do it. You can't add the feature. It's too risky. You'd have
to change a core part of the program, and who knows what kind of subtle
bugs might creep in doing that! You got hold of the source code and made
sure that the license allows you to modify it, but it's too dangerous.
Isn't it?

Well, the proponents of `Extreme Programming <http://www.xprogramming.com/>`__
say not only that you can,
but that you should!

Extreme programmers aim for code that's small, lean, mean, and
functional. To achieve the lean and mean, x-programmers always `do the
simplest thing that could possibly
work <http://www.xprogramming.com/Practices/PracSimplest.html>`__. They
resist the temptation to implement stuff that may be useful later,
because they assume they're `not going to need
it <http://www.xprogramming.com/Practices/PracNotNeed.html>`__.
X-programmers are fearless about modifying the code, so their software
is always functional. They will edit, refactor, or reimplement even
large sections when they need to add a new feature.

But what about the risks? What about the bugs? The extreme
programmers' answer: extreme testing. They write a test case for every
feature they implement, even before they start coding the feature. Need
to add new functionality? Write a test case. Found a bug? Write a test
case. Have doubts about how something really works? Write a test case.
The set of test cases thus produced serves to guarantee that the system
keeps doing what it should even after important modifications.
X-programmers run the whole battery of tests after each change, and they
never release the code until all the test cases run flawlessly.
| Extreme testing produces a large number of test cases, and the process
of running all the tests and evaluating the results could get unwieldy.
X-programmers use automation to keep extreme testing under their
control. They have written testing frameworks for Java, C++, and several
different flavors of Smalltalk. The frameworks are all freely available
from the `XProgramming software
page <http://www.xprogramming.com/software.htm>`__. The Java testing
framework provides one example of how extreme testing can be used.

JUnit
-----

JUnit is a small testing framework written in Java by Kent Beck and
Erich Gamma. Beck and Gamma are well-known as two of the founders of the
`Software Patterns <http://c2.com/cgi/wiki?PatternIndex>`__ movement,
and this shows in the design simplicity of JUnit. Using JUnit to test
Java programs is very easy. You start by writing a descendant of
junit.framework.TestCase. This is an example from my Java Diff package:

    ``import junit.framework.*;public class DiffTest extends TestCase {public DiffTest(String testName) {super(testName);}``
    `` ``\ `` public void testDeleteAll() {Revision revision =              Diff.diff(original, empty);assertEquals(revision.size(),              1);assertEquals(revision.getDelta(0).getClass(),              DeleteDelta.class);assert(Diff.compare(revision.patch(original),              empty));}//...``

Each method in a test case exercises a different aspect of the tested
software. The aim, as is customary in software testing, is not to show
that your program works fine, but to show that it doesn't. Interaction
with the JUnit framework is achieved through assertions, which are
method calls that check (assert) that given conditions hold at specified
points in the test execution.

JUnit allows for several ways to run the different tests, either
individually or in batches, but the simplest one by far is to let the
TestSuite collect the tests using Java introspection:

::

        public TestSuite suite() {         return new TestSuite(DiffTest.class);     }     //...     TestResult result = DiffTest.suite().run();

When a class is passed to the constructor of a new instance of
TestSuite, the instance uses Java introspection to find all the methods
in the class with names that start with "test." A subsequent call to
TestSuite's run method executes all the tests and returns the results as
an instance of TestResult. TestSuite also allows the creation of, well,
suites, which include any combination of test cases.

For maximum convenience, JUnit provides both text-based and GUI
(Swing) user interfaces that facilitate the execution of test suites.
Both user interfaces can be run as standalone programs by passing the
class name of the test suite to run as the first command-line argument.

|image0|

*JUnit's GUI interface reports progress and results as the tests are executed.*

You can also run the tests from within your favorite integrated
development environment (IDE), and have the debugger stop as soon as a
problem is found. Your static main method would look something like
this:

::

     public static void main(String args[]) {     junit.textui.TestRunner.run(DiffTest.suite()); }


Open tests
----------

Proponents of extreme programming qualify their approach as a
"`lightweight methodology <http://www.extremeprogramming.org/light1.html>`__," to
contrast it with the heavyweight
`methodologies <http://c2.com/cgi/wiki?CategoryMethodology>`__ that
became popular during the 80s, and that few software projects continue
to follow. XP establishes only a `small set of common sense rules and
practices <http://www.xprogramming.com/Practices/xpractices.htm>`__, and
the documentation generated is no more than the minimum required to keep
things flowing smoothly. Almost all software development projects,
including open source ones, could benefit from some amount of XP.

Why talk about testing and methodologies in an open source column?
Much open source discourse is devoted to the "freedom" programmers enjoy
to modify open source code at will. The truth is that this supposed
freedom is only partial. Most of the open source software one can get
hold of lacks the testing infrastructure required to make sure that
adding features to the code doesn't also break it. As things stand, open
source programmers must devise their own ways to verify the software
they change, resulting in an incalculable amount of duplicated -- and
mostly wasted -- effort.

Open source projects greatly benefit when they adopt testing policies
and a testing framework from the start. Most open source projects do
perform formal testing. All such projects would be improved if the
numerous test cases produced could be collected and officially
distributed. Adopting the test frameworks provided by the XP people is
one approach, but almost any other test framework would do.

Extreme testing needs to become an integral part of open source
practice. Only then will we truly experience the freedom of working to
improve a piece of code without the fear of breaking it.

| Originally written for *In Publishing LLC*
| Copyright © 1999 Inprise Corp.

.. |image0| image:: /images/junit_gui.gif
