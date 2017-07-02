import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.getcwd()))

from pynewtonmath import core, wrapper


class TestWrapper (unittest.TestCase):
    def test_expose_endpoints (self):
        for op in core.ENDPOINTS:
            self.assertTrue(op in dir(wrapper))
            print('.', end='', flush=True)
    
    
    def test_endpoints (self):
        # operation: (expression, result)
        tests = {
            'simplify': ('x^2 + 2x', 'x^2 + 2 x'),
            'factor': ('x^2 + 2x', 'x (x + 2)'),
            'derive': ('x^2+2x', '2 x + 2'),
            'integrate': ('x^2+2x', '1/3 x^3 + x^2'), # + C missing
            'zeroes': ('x^2+2x', [-2, 0]),
            'tangent': ('2|x^3', '12 x + -16'),
            'area': ('2:4|x^3', 60),
            'cos': ('pi', -1),
            'sin': ('0', 0),
            'tan': ('0', 0),
            'arccos': ('1', 0),
            'arcsin': ('0', 0),
            'arctan': ('0', 0),
            'abs': ('-1', 1),
            'log': ('2|8', 3),
        }
        
        for op, test in tests.items():
            exp, result = test
            self.assertEqual(getattr(wrapper, op)(exp), result)
            print('.', end='', flush=True)
    
    
    def test_extended_endpoints (self):
        self.assertEqual(wrapper.tangent('x^3', 2), '12 x + -16')
        self.assertEqual(wrapper.area('x^3', 2, 4), 60)
        self.assertEqual(wrapper.log(8, 2), 3)


if __name__ == '__main__':
    unittest.main()
