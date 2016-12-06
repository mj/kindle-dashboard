#!/usr/bin/python2
# encoding=utf8

import pystache
import redis
import math
import codecs
from datetime import datetime
import calendar
import locale

locale.setlocale(locale.LC_TIME, 'de_DE')

r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)

outside = r.hget('temperature', 'outside')
driving = r.hget('signage', 'pascalstr')
sunrise = r.hget('signage', 'sunrise')
sunset = r.hget('signage', 'sunset')
moon = r.hget('signage', 'moon_phase').lower()
waste = r.hgetall('waste').keys()

moon_type = {
    'full moon': 'Vollmond',
    'waxing crescent': 'Zunehmend',
    'first quarter': 'Zunehmend',
    'waxing gibbous': 'Zunehmend',
    'waning gibbous': 'Abnehmend',
    'third quarter': 'Abnehmend',
    'Waning crescent': 'Abnehmend',
}.get(moon, 'Neumond')

waste_types = {
    'bio': u'Biomüll',
    'residual': u'Restmüll',
    'paper': 'Papier',
    'gelber_sack': 'Gelber Sack'
}

output = codecs.open('template.svg', 'r', encoding = 'utf-8').read()

output = pystache.render(
    output,
    {
        'outside': int(float(outside)),
        'driving': int(math.ceil(int(driving) / 60)),
        'today': {
            'day': calendar.day_name[datetime.today().weekday()],
            'date': datetime.today().strftime('%d.%m.'),
            'time': datetime.today().strftime('%H:%M'),
        },
        'sunrise': sunrise[0:5],
        'sunset': sunset[0:5],
        'moon': {
            'phase': moon.lower().replace(' ', '-'),
            'type': moon_type,
        },
        'waste': ", ".join(waste_types.get(x, '?') for x in waste),
    }
)

codecs.open('output.svg', 'w', encoding = 'utf-8').write(output)
