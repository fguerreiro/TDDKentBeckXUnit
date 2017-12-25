import xunit

# What is a constancy in code ? It will change.
# Code will change, and it needs to be flexible
# how do you flex it ? Changing it, using TDD

# Invoke tearDown even if the test method fails
# Run multiple tests
# Report collected results

class TestCaseTest(xunit.TestCase):
    def testTemplateMethod(self):
        test = xunit.WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = xunit.WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = xunit.WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed", result.summary()

    def testFailedResultFormatting(self):
        result = xunit.TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()


# next task: see the results of running any nr of tests


## TDD Tips by Kent Beck:
# How I pick the next test to implement:
# - What's the next test that will teach me something to gain confidence ?
# If test works but I get stuck in the next, go back two steps !
# This way works as a Checkpoint for code, on how do we know about the problem