import re


t = input()

for i in range(t):
    reg  = raw_input()
    try:
        re.compile(reg)
        print(True)
    except re.error:
        print(False)
