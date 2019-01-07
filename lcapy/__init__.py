"""
Lcapy is a Python library for linear circuit analysis.  It uses SymPy
for symbolic mathematics.

Lcapy can analyse circuits described with netlists using modified nodal
analysis.  See lcapy.netlist

Alternatively, Lcapy can analyse networks and circuits formed by
combining one, two, and three port networks.

Copyright 2014--2019 Michael Hayes, UCECE
"""

from __future__ import absolute_import, print_function
del absolute_import, print_function

from pkg_resources import get_distribution

__version__ = get_distribution('lcapy').version

import sys
if sys.version_info[0] == 2 and sys.version_info[1] < 6:
    raise ImportError("Python Version 2.6 or above is required for Lcapy.")
else:  # Python 3
    pass
    # Here we can also check for specific Python 3 versions, if needed

del sys

from sympy import init_printing
init_printing()


from .functions import *
from .symbols import *
from .circuit import *
from .oneport import *
from .twoport import *
from .schematic import *
from .cexpr import *
from .fexpr import *
from .sexpr import *
from .texpr import *
from .noiseexpr import *
from .phasor import *
from .omegaexpr import *
from .sup import *


def show_version():
    
    from sys import version as python_version
    from sympy import __version__ as sympy_version
    from numpy import __version__ as numpy_version

    print('Python: %s\nSymPy: %s\nNumPy: %s\nLcapy: %s' % 
          (python_version, sympy_version, numpy_version, __version__))

