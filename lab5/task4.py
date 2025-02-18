
import re
text="Nuray Kanat ASDasd A ASDFG"
print(*re.findall(r"[A-Z][a-z]+",text))