# PyNewtonMath
## Basics

PyNewtonMath is a Python 3.x API wrapper providing full support for the newton micro-service.

* [GitHub](https://github.com/aunyks/newton-api)
* [Website](https://newton.now.sh)

Newton does anything from numerical calculation to symbolic math parsing.

## Installation

Using pip:

    pip install pynewtonmath

From GitHub:

    pip install git+https://github.com/benpryke/pynewtonmath

## Usage

    import pynewtonmath as newton
    
    newton.derive('x^2') # -> '2 x'
    newton.cos('pi') # -> -1
    newton.zeroes('x^2+2x') # -> [-2, 0]

* No instantiation required
* Supports natural return types

The following methods take optional extra arguments for convenience. As per the API, if these are not specified they must be included before a horizontal bar `'|'` in the expression for newton.

    newton.log('2|8') # -> 3
    newton.log(8, base=2) # -> 3
    
    newton.tangent('2|x^3') # -> '12 x + -16'
    newton.tangent('x^3', x=2) # -> '12 x + -16'
    
    newton.area('2:4|x^3') # -> 60
    newton.area('x^3', start=2, end=4) # -> 60

See [the newton API GitHub repo](https://github.com/aunyks/newton-api) for the full list of endpoints.
