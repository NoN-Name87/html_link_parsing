import requests
import re
string = requests.get(input())
pat = r"<a.*href=[\'\"]([\w]*://)?([^.][\w\.\-]*)"
prs = re.findall(pat, string.text)
result = set()
for i in prs:
    result.add(i[1])
lst = list(result)
lst.sort()
for i in lst:
    print(i)