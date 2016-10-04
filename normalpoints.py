from sys import argv
from geojson import Point
from random import normalvariate

def randnormpt(count, mu1, sigma1, mu2, sigma2):
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
            print("\t\t\t",Point((normalvariate(mu1,sigma1), normalvariate(mu2,sigma2))))
            print('''
                }''')
        else:
            print('''
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": ''')
            print("\t\t\t",Point((normalvariate(mu1,sigma1), normalvariate(mu2,sigma2))))
            print('''
                },''')
    print("""
        ]
    }""")
    return

randnormpt(int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]))
