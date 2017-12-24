import xunit

# Invoke test method
# Invoke setUp first
# Invoke tearDown afterward
# Invoke tearDown even if the test method fails
# Run multiple tests
# Report collected results

# We'll call the test class WasRun, because it's a test case that reports
# if the method was run

# What is a constancy in code ? It will change.
# Code will change, and it needs to be flexible
# how do you flex it ? Changing it, using TDD


class TestCaseTest(xunit.TestCase):
    def testTemplateMethod(self):
        test = xunit.WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log

TestCaseTest("testTemplateMethod").run()

# keep a little log of the methods that are called -> we know the order of the tests are called
