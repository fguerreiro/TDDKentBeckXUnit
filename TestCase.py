import xunit

# What is a constancy in code ? It will change.
# Code will change, and it needs to be flexible
# how do you flex it ? Changing it, using TDD

# Invoke tearDown even if the test method fails
# Run multiple tests
# Report collected results

class TestCaseTest(xunit.TestCase):
    def setUp(self):
        self.result = xunit.TestResult()

    def testTemplateMethod(self):
        test = xunit.WasRun("testMethod")
        test.run(self.result)
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = xunit.WasRun("testMethod")
        test.run(self.result)
        assert "1 run, 0 failed" == self.result.summary()

    def testFailedResult(self):
        test = xunit.WasRun("testBrokenMethod")
        test.run(self.result)
        assert "1 run, 1 failed", self.result.summary()

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())


suite = xunit.TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
result = xunit.TestResult()
suite.run(result)
print result.summary()
# next task: Run multiple tests


## TDD Tips by Kent Beck:
# How I pick the next test to implement:
# - What's the next test that will teach me something to gain confidence ?
# If test works but I get stuck in the next, go back two steps !
# This way works as a Checkpoint for code, on how do we know about the problem