Scanning 35mm film
==================

:date: 2006-08-20
:slug: scanning-35mm-film
:author: Apalala

.. :tags:
.. :category:
.. :summary:


*About why to design before implementing*

Yesterday I gave a shot at trying to scan some of the 35mm negatives
of my old
`Black&White <http://www.neogeny.org/blog/2006/06/22/black_and_white.html%5D>`__
photos using a 1200 DPI flat-bed scanner. It failed misserably:

-  The scan showed severe `Moiré <http://en.wikipedia.org/wiki/Moire>`__
   and other kinds of noise in the pictures.
-  The sizes of the TIFF files were enormous.
-  At 1200 DPI the flat-bed scanner picked up dust and stains from the
   glass.

Although it was just an experiment, the terrible results led me to do
some research. Unless otherwise stated, the following numbers come from
the article about `Digital Photography at
Wikipedia <http://en.wikipedia.org/wiki/Digital_photography>`__.

Resoluiton of 35mm film
~~~~~~~~~~~~~~~~~~~~~~~

The `Wikipedia <http://en.wikipedia.org/wiki/Digital_photography>`__
article says that a `DSLR <http://en.wikipedia.org/wiki/Dslr>`__
resoluiton of 6 to 14
`megapixels <http://en.wikipedia.org/wiki/Megapixel#Megapixel>`__
aproximates that of 35mm film, and that one of 16 megapixels exceeds it,
so lets asume that the resolution of 35mm film is 14 megapixels.

To compare with the scanner resolution we need to translate that to
`DPI <http://en.wikipedia.org/wiki/Dpi>`__. Megapixels are calculated as
the product of the vertical and horizontal resolutions:

::

    M=x*y

The `Aspect Ratio <http://en.wikipedia.org/wiki/Aspect_ratio>`__ of 35mm
and DSLRs is known to be (3:2), or 1.5. Thus:

::

    x=1.5*yy=x/1.5

and

::

    M=x*(x/1.5)
    M=x^2/1.5x=sqrt(1.5*M)

So, at 14 (actually 14.7) megapixels, the number of horizontal pixels in
35mm film is about 4693. If we divide that by 1.38" (35mm translated to
inches), we obtain 3405 DPI for 35mm film.

Required resolution
~~~~~~~~~~~~~~~~~~~

With that result it is not surprising why scanning 35mm with a 1200 DPI
scanner produces terrible results: 65% of the information in the
negative is not captured. Even more, according to `Information
Theory <http://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem>`__,
the sampling density must be the double of the information density,
which means that the scanner should have a resolution of at least 6810
DPI to sample a 35mm negative without bias.

Guess what? The resoluiton of specialized 35mm film scanners is of above
7000 DPI…
