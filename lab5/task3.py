import re
text="sjafskff_ gfhjb_ jv_ HF_ fvkll kkk FJFJFFJ"
print(*re.findall(r"[a-z]+_",text))