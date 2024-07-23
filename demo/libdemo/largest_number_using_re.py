import re

data = "abc 98 123 xyz 456 def 9383"

nums = re.findall(r"\d+", data)
print(nums)
print(max(map(int, nums)))
