import re
text = "String: abb , a0 , ab"
print(*re.findall(r"ab*", text))