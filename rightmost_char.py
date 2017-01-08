import sys

# test_cases = open(sys.argv[1], 'r')
# test_lines = [line.rstrip() for line in test_cases]
test_lines = ["sajdkadkjam,r", "43131kjkjkjfkajdfkladf,l"]
for test in test_lines:
    word = test.split(",")[0]
    clue = test.split(",")[1]
    maxPos = -1
    #TODO: make sure it is working
    if len(word) > 0:
        for l in range(len(word)):
            if word[l] == clue:
                maxPos = l
        sys.stdout.write(str(maxPos))
        if test_lines.index(test) != len(test_lines) - 1:
            sys.stdout.write("\n")
        sys.stdout.flush()
# test_cases.close()

