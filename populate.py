import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geodjango.settings')

import django
django.setup()
from django.contrib.gis.geos import Point, fromstr

from restraunts.models import Restraunt

                #(          name,    latitude,  longitude )
location_data = [('Himani Hotel', '30.904486', '77.096733'),
                 ('Deokali', '25.830952', '82.676369'),
                 ('Maya Heritage', '9.618521', '76.438469'),
                 ('Carlton Towers', '12.960878', '77.643951'),
                 ('Koonimedu', '12.085485', '79.892403'),
                 ('Taj Mahal Palace Hotel', '18.922028', '72.833358'),
                 ('Sagar Hotel', '29.8672682', '77.8921256'), ]

def populate():
    for location in location_data:
        name = location[0]
        latitude = float(location[1])
        longitude = float(location[2])
        point = fromstr("POINT(%s %s)" % (longitude, latitude))
        restraunt_obj = Restraunt(name = name, coordinates = point)
        restraunt_obj.save()
        print restraunt_obj,point.tuple

if __name__== '__main__':
    print "Starting population script.."
    populate()

        
