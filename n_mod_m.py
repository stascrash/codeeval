import sys

test_cases = open(sys.argv[1], 'r')
test_lines = (line.rstrip() for line in test_cases)
for test in test_lines:
    n = int(test.split(",")[0])
    m = int(test.split(",")[1])
    mod = n - (m * (n / m))

    print(mod)
test_cases.close()
