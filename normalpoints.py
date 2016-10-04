from sys import argv
from geojson import Point
from random import normalvariate

def randnormpt(count, mu, sigma):
    print('''
    {
        "type": "FeatureCollection",
        "features": [
    ''')
    for i in range(count):
        if i == range(count)[-1]:
            print('''
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": ''')
            print("\t\t\t",Point((normalvariate(mu,sigma), normalvariate(mu,sigma))))
            print('''
                }''')
        else:
            print('''
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": ''')
            print("\t\t\t",Point((normalvariate(mu,sigma), normalvariate(mu,sigma))))
            print('''
                },''')
    print("""
        ]
    }""")
    return

randnormpt(int(argv[1]), int(argv[2]), int(argv[3]))
