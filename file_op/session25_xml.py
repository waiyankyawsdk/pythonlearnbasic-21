#run in terminal $pip install xmltodict
#check python freeze

import xmltodict
handle = open("xml_input.xml","r")
content = handle.read()
# print(content)
#parse()
d = xmltodict.parse(content)
print(d)
print(d['Result'])
print(d['Result']['RequestCode'])
d['Result']['RequestCode'] = 4

print(d['Result']['RequestCode'])
#unparse
x = xmltodict.unparse(d)
print(x)