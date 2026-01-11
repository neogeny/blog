Xtreme testing for Delphi programs
==================================

:date: 1999-11-28
:slug: xtreme-testing-for-delphi-programs
:author: Apalala

.. :tags:
.. :category:
.. :summary:


*A standard testing framework for Delphi has been long overdue. Now
there is one and it's even open source.*

In my `article <http://www.neogeny.org/writings/1999-10-18.html>`__ on
Xtreme testing, I talked about how it could improve the quality of
programs as well as the speed and confidence with which they were
developed. For the examples, I used Kent Beck and Erich Gamma's JUnit
open-source testing framework and I wrote the program fragments using
Java -- a language I'm comfortable with. But those who know me from
previous writing gigs or my once-frequent postings in online forums know
that I've long been a Borland Pascal programmer. My online buddies are
probably wondering why I didn't write the examples in Object Pascal. The
reason is that I discovered Xtreme testing only recently, and, as far as
I know, there are no testing frameworks available for Delphi.

But we're about to change that.

I've been choosing the latest version of Borland's Pascal as the best
solution to most of my programming needs for 15 years now. The reasons
are varied. The tool's suitability to the kind of applications I've been
developing is one reason. Its overall quality is another. Not to mention
its blazing instant-feedback speed. A large reason has been the
community of developers that has gathered around the tool.

I met that community when I joined CompuServe and the BPASCAL forum
back in 1993. BPASCAL quickly became an invaluable asset. The forum was
filled with excellent questions, prompt answers, expert advice, and
loads of useful source code. Examples, workarounds, patches, libraries,
frameworks, and even complete applications were available for download
and free use. The forum's motto was "Don't pay back -- pay forward," and
these guys took it seriously. I started contributing advice and source
code as soon as I was confident enough to do so, and eventually became
expert enough to start writing about Delphi for trade publications --
but that's another story.

Even after all these years I have never felt that I had managed to
fully pay back -- er, forward -- all the help. That's the reason for
this contribution: DUnit, a port of the JUnit Xtreme testing framework
to Delphi.

Porting from JUnit
------------------

The original JUnit framework is extremely easy to use and very
effective. I wanted the Delphi port to be as good.

To speed up the port, I decided to translate the classes and
interfaces in JUnit almost literally. It was a compromise that required
heavy use of method overloading, which means that DUnit won't be usable
with versions of Delphi prior to version 4.

I made another compromise. I could translate the methods in JUnit
almost literally if I used the Delphi port of the Java collections
library that I had begun implementing, so that's exactly what I did.

These two decisions let me do the port in a single afternoon and
resulted in a framework that I find very easy to use. But the
implementation relies heavily on interfaces and iterators -- idioms
seldom used by Delphi programmers. Although the first idiom is fully
supported by Delphi, most programmers reserve it for dealing with COM
and ActiveX objects. Interfaces provide the advantage of memory
management by reference counting, so a little work up-front with
interfaces translates into much less code to write. You do have to be
careful with some interface implementation issues. For example, a loop
with references to interfaces will make it impossible for Delphi to
reclaim the memory used.
| The second idiom is common in Java and C++ programs, but may be
unfamiliar to Delphi programmers. Iterators enable you to write
implementation-independent loops that process the objects contained in a
collection. JUnit uses iterators, so DUnit does too.

Classes that test classes
-------------------------

To apply DUnit to your Delphi programs, you write a descendant of the
class TTestCase for each test case you want to apply to a unit. I
decided to apply DUnit to the collections library used in its own
implementation. To avoid circular unit references, I had to declare the
test case classes in the main program (DPR) file, but I recommend that
in general you place the test classes inside the units they test. Doing
so will let you test protected and private methods in addition to the
public and published ones.

This is the class declaration for a simple test case:

::

    type
        TListTests = class(TTestCase, ITest)
            published
            // published, so we get RTTI;
            // virtual, so the compiler
            // doesn't eliminate them;
            procedure testEmptyArrayList; virtual;
            procedure testEmptyLinkedList; virtual;
            procedure doEmptyTests(list :IList);
            procedure testFailure; virtual;
            procedure testError; virtual;
        end;

The first two methods test several conditions on arrays and linked
lists. The third procedure is a utility used by the preceding routines.
The last two methods generate a test failure and an exception
respectively, to make sure DUnit responds properly when errors are
detected. The test methods must be declared within a published section
so that Delphi generates runtime type information for them and DUnit has
access to method names at runtime. Here's part of the implementation of
doEmptyTests:

::

    procedure TListTests.doEmptyTests(list: IList);
    var i :IIterator;
    begin
        assert('isEmpty', list.isEmpty);
        assertEquals('size', 0, list.size);
        assert('iterator at end', not list.iterator.hasNext);
        list.add('anItem');   assertEquals('size', 1, list.size);
        //...

Yes, writing the test cases is that easy. Each line in the test method
checks (asserts) a condition that should be true if the tested code is
working properly. DUnit provides several different assertXXX methods to
make writing tests easier.

Pulling it all together
-----------------------

To assemble all the test methods into a single test suite, you write a
function like this:

::

    function suite :ITestSuite;
    begin
        result := TTestSuite.Create;
        result.addTest(TListTests.Create('testEmptyArrayList'));
        result.addTest(TListTests.Create('testEmptyLinkedList'));
        result.addTest(TListTests.Create('testFailure'));
        result.addTest(TListTests.Create('testError'));
    end;

Finally, you run the tests in console mode with a single statement in
the main program block:

::

    begin
        DUnit.runTest(suite, true);
    end.

Oops! Two bugs in the collections library surfaced while I was
executing the tests. So the framework has already paid for the effort I
invested in it. After fixing the bugs and running the tests again, the
output looks exactly as expected:

::

    DUnit: Testing.
    ...F.ETime: 0.0
    FAILURES!!!
    Test Results:Run: 4 Failures: 1 Errors: 1
    There was 1 error:
    1) TListTests.testError: EAbort: Raised exception on purpose
    There was 1 failure:
    1) TListTests.testFailure: AssertionFailedError: Failed on purposePress [return] to continue.


A license to test
-----------------

What are the licensing terms for DUnit? In open source development,
when you enhance, fix or port someone else's code, it is customary to:

-  Give as many rights to the original software as the original authors
   did.
-  Give the same rights to your contributions (some licenses, such as
   the GNU GPL, require that you to do this).
-  Give credit to the original authors for their work.
-  Preserve all disclaimers made by the original authors, in particular
   those about lack of warranty and protection from their names being
   used for promotion without authorization.

The license to the original JUnit is very flexible, so I made the
license to DUnit almost an exact copy of it. The part about your rights
reads like this:

    Permission to reproduce and create derivative works from the
    Software ("Software Derivative Works") is hereby granted to you
    under the copyrights of [...] (THE AUTHORS). The authors also grant
    you the right to distribute the Software and Software Derivative
    Works.


Next steps
----------

As it stands, DUnit lacks any documentation. If you can read Java
code, then the documentation that comes with JUnit is probably
sufficient.

At this time the following still needs to be done:

-  Create a GUI interface to the framework like the one JUnit has. Given
   Delphi's GUI capabilities, this shouldn't take more than an hour or
   so.
-  Use Delphi's RTTI to build a test suite automatically by gathering
   all the methods with names that start with "test." JUnit does this,
   and the feature is very useful. I'll leave this task to someone else.
-  Translate JUnit's excellent documentation and examples to Delphi.

If you'd like to contribute to the DUnit project, please do so. But
try to refrain from sending me suggestions. What I think should be done
in DUnit I will likely do, time permitting. As Linus Torvald says, I'd
rather you "show me the source code!"

Oh -- the source code! You can download the source code to the latest
version of DUnit from my always-under-construction Web site:
`http://www.suigeneris.org/dunit <http://www.neogeny.org/dunit/index.html>`__.
I hope you find this small testing framework useful. If you do, please
forget about expressing thanks. Pay forward.

| Originally written for *In Publishing LLC*
| Copyright © 1999 Inprise Corp.
