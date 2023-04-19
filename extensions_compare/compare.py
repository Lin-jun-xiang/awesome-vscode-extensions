import os
import chardet

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

with open('./new_extensions.ps1', 'rb') as f1, open('../extensions.ps1', 'rb') as f2:
    contents1, contents2 = f1.read(), f2.read()
    detected_encoding1, detected_encoding2 = chardet.detect(contents1)['encoding'], chardet.detect(contents2)['encoding']

with open('./new_extensions.ps1', encoding=detected_encoding1) as f1, open('../extensions.ps1', encoding=detected_encoding2) as f2:
    lines1 = [line.strip() for line in f1.readlines()]
    lines2 = [line.strip() for line in f2.readlines()]

lines1 = [line for line in lines1 if not line.startswith('#')]
lines2 = [line for line in lines2 if not line.startswith('#')]

ps1_set = set(lines1)
ps2_set = set(lines2)

ps1_diff = ps1_set - ps2_set
ps2_diff = ps2_set - ps1_set

result = {"ps1 have not": ps1_diff, "ps2 have not": ps2_diff}
print(result)
