

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
    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1

    # def run(self):
    #     method = getattr(self, self.name)
    #     method()

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        print(test.wasRun)
        assert(not test.wasRun)
        test.run()
        print(test.wasRun)
        assert(test.wasRun)

TestCaseTest("testRunning").run()
