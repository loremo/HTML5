import json
import decimal
from shapely.geometry import Polygon, MultiPolygon

with open('countriesData_small.js') as f:
    content = f.readlines();

countries = {};
for line in content:
    if not line.startswith('{"'):
        continue
    line = line.strip()
    line = line[0:-1]
    j = json.loads(line, parse_float=decimal.Decimal)
    countries[j['name']] = j['border']
    
for country, borders in countries.iteritems():
    print(country + ' has ' + str(len(borders)) + ' borders')
    polygons = [];
    for border in borders:
        #print(len(border))
        if len(border) < 3:
            continue
        p = Polygon(border)
        if p.area < 5:
            continue
        print("current border's area: " + str(p.area))
        polygons.append(p)
    if len(polygons) > 1:
        areas = [p.area for p in polygons]
        countries[country] = polygons[areas.index(max(areas))]
    elif len(polygons) == 1:
        countries[country] = polygons[0]
    else:
        raise('Country must contain at least one Polygon')
 
for this_country, this_polygon in countries.iteritems():
    #print(this_country)
    #print(this_polygon)
    try:
        print('representative point of ' + this_country + ': ' + str(this_polygon.representative_point()))
    except ValueError: 
        print('representative point of ' + this_country + ': ' + str(this_polygon.convex_hull.representative_point()))
    for other_country, other_polygon in countries.iteritems():
        if this_country == other_country:
            continue
        if this_polygon.intersects(other_polygon):
            print(this_country + ' has a border with ' + other_country)
    
    
ger = countries['Germany']
pol = countries['Poland']
spa = countries['Spain']
fra = countries['France']
print('Germany')
#print(ger)
print('---------------------')
print('Poland')
#print(pol)
print('---------------------')
print('Spain')
#print(spa)
print('---------------------')
print(ger.area)
print(pol.area)
print(spa.area)
print(fra.area)
print('---------------------')
#print(ger.representative_point())


