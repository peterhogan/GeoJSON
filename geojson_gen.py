from geojson import Point

print('''
{
    "type": "FeatureCollection",
    "features": [
''')
for i in range(10):
    if i == range(10)[-1]:
        print('''
                "type": "Feature",
                "properties": {},
                "geometry": {''')
        print("\t\t\t",Point((i,0)))
        print('''
            }''')
    else:
        print('''
                "type": "Feature",
                "properties": {},
                "geometry": {''')
        print("\t\t\t",Point((i,0)))
        print('''
            },''')
print("""
    ]
}""")
