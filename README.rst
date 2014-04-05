SpiderTrap
==========

An http server that responds with an ever-expanding web of links. Use it
to test, benchmark, and confuse web crawlers.

Implemented as a simple python script with no dependencies other than
the standard library. Works with python 2.7 and python 3.

Installation
------------

::

    $ pip install spidertrap

Usage
-----

::

    spidertrap [-h] [-p PORT] [--fanout FANOUT]

    optional arguments:
      -h, --help            show this help message and exit
      -p PORT, --port PORT  [9999]
      --fanout FANOUT       Number of links to create on each page [2]

Licence
-------

MIT
