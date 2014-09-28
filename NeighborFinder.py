import json
import decimal

with open('countriesData_small.js') as f:
    content = f.readlines();

countries = {};
for line in content:
    if not line.startswith('{"code":'):
        continue
    line = line.strip()
    line = line[0:-1]
    #print(line)
    j = json.loads(line, parse_float=decimal.Decimal)
    countries[j['name']] = j['border']
print(countries)
#json.loads(content)
