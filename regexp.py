import re

a = 'AlaH adu res dio'

res = re.findall(r"alah+", a, flags=re.IGNORECASE)[0]

if re.findall(r"alah", a, flags=re.IGNORECASE):
    print(re.findall(r"alah", a, flags=re.IGNORECASE)[0])
else:
    print('fuck you')

# print(re.findall(r"banana+", "BananA", flags=re.IGNORECASE)[0])