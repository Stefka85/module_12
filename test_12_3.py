import unittest
import suite_12_3

TestSuite = unittest.TestSuite()
TestSuite.addTest(unittest.TestLoader().
                  loadTestsFromTestCase(suite_12_3.Tournament))
TestSuite.addTest(unittest.TestLoader().
                  loadTestsFromTestCase(suite_12_3.RunnerTest))

r = unittest.TextTestRunner(verbosity=2)
r.run(TestSuite)