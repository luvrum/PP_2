import re
text="abb abbbb ab abbbbbbb abbb"
print(*re.findall(r"ab{2,3}",text))