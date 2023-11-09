import re
s = "abbcccaa"
print(*re.findall(r"(?P<p>[a-z])p*", s))