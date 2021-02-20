import re
pat = re.compile('AA')
# m = pat.search('CBAA')
# m = pat.search('ABCAAA')
# print(m)

# m = re.search("asd","Aasd")
# print(m)

# print(re.findall("[A-Z]+","ASDaDFGAa"))

print(re.sub("a","A","abcdasdfsafa")) #找到a替换A

a = r"\asfsfd-\'"
print(a)