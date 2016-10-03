from geojson import Point

print('''{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {},
            "geometry": {''')
for i in range(10):
    print("\t\t\t",Point((i,0)))

print("""
                    }
                ]
            }
        }
    ]
}""")
