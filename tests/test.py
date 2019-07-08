from __future__ import print_function
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# added this to import app.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_simple import TestSimpleSpotter
import unittest

test_cases = unittest.TestLoader().loadTestsFromTestCase(TestSimpleSpotter)
suite = unittest.TestSuite([test_cases])
result = unittest.TextTestRunner().run(suite)
sys.exit(not result.wasSuccessful())
