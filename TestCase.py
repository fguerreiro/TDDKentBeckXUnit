

# Invoke test method
# Invoke setUp first
# Invoke tearDown afterward
# Invoke tearDown even if the test method fails
# Run multiple tests
# Report collected results

# We'll call the test class WasRun, because it's a test case that reports
# if the method was run

# What is a constancy in code ? It will change.
# Code will change, and it needs to be flexibe
# how do you flex it ? Changing it, using TDD

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        self.wasSetup = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.wasSetup = 1

    def testMethod(self):
        self.wasRun = 1
        self.wasSetup = 1


class TestCaseTest(TestCase):
    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert test.wasSetup

    def testRunning(self):
        test = WasRun("testMethod")
        test.run()
        assert test.wasRun


TestCaseTest("testRunning").run()
# TestCaseTest("testSetUp").run()
