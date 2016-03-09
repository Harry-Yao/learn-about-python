import re

str = "some.one@gmail.org"
str2 = "bill.gates@microsoft.com"
str3 = "<Tom Paris> tom@voyager.org"
def runRe(str):
    return re.match(r'^([0-9a-zA-Z\.]+)@(\w+)(\.com|\.org)$',str).groups()
print(runRe(str))
print(runRe(str2))

def runRe2(str):
    m = re.match(r'^<([0-9a-zA-Z\.\s]+)>\s+(.+)$',str)
    if m:
        print(m.group(1))
        return runRe(m.group(2))
    else:
        return runRe(str)

print(runRe2(str3))