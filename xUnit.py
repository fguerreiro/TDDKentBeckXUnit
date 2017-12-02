

# Invoke test method
# Invoke setUp first
# Invoke tearDown afterward
# Invoke tearDown even if the test method fails
# Run multiple tests
# Report collected results

# We'll call the test class WasRun, because it's a test case that reports
# if the method was run

class WasRun:
    pass



test = WasRun("testMethod")
print(test.wasRun)

test.testMethod()
print(test.wasRun)
