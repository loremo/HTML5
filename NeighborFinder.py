import json
import decimal
from shapely.geometry import Polygon, MultiPolygon

with open('countriesData_small.js') as f:
    content = f.readlines();

countries = {};
for line in content:
    if not line.startswith('{"code":'):
        continue
    line = line.strip()
    line = line[0:-1]
    j = json.loads(line, parse_float=decimal.Decimal)
    countries[j['name']] = j['border']
    
for country, borders in countries.iteritems():
    print(country + ' has ' + str(len(borders)) + ' borders')
    polygons = [];
    for border in borders:
        print(len(border))
        if len(border) < 3:
            continue;
        p = Polygon(border)
        polygons.append(p)
    polygons = MultiPolygon(polygons)
    countries[country] = polygons
    
ger = countries['Germany']
ger = ger.geoms[4]
ger = ger.convex_hull
pol = countries['Poland']
pol = pol[0]
pol = pol.convex_hull
spa = countries['Spain']
spa = spa[11]
spa = spa.convex_hull
print('Germany')
print(ger)
print('---------------------')
print('Poland')
print(pol)
print('---------------------')
print('Spain')
print(spa)
print('---------------------')
print(ger.area)
print(pol.area)
print(spa.area)
print('---------------------')
print(ger.intersection(pol))


#json.loads(content)

