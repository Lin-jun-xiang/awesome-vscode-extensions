# 讀取第一個檔案中的所有行
with open('extensions.ps1', 'rb') as file:
    lines1 = [line.strip() for line in file.readlines()]

# 讀取第二個檔案中的所有行
with open('2.ps2', 'rb') as file:
    lines2 = [line.strip() for line in file.readlines()]

# 忽略兩個檔案中的 '#' 字符
lines1 = [line for line in lines1 if not line.startswith('#')]
lines2 = [line for line in lines2 if not line.startswith('#')]

# 找出1.ps1沒有出現在 2.ps2之中的所有行
lines_not_in_lines2 = list(set(lines1) - set(lines2))

print(lines_not_in_lines2)
