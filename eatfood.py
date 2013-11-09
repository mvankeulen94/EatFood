#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, redirect
import requests
import json 
app = Flask(__name__)

#US/NY/10027/New York/535%20W%20116th%20St

#@app.route('/')
def get_coordinates(query):
    LISTING_REQUEST='http://dev.virtualearth.net/REST/v1/Locations/'
    LISTING_REQUEST = LISTING_REQUEST + query
    LISTING_REQUEST = LISTING_REQUEST + '?key=AuuvwD9piSkUPB6tmyjruLS88Cecl-pR4SWViI4ucbfH7twMFD_Alr7Go6-P__11'
    response = requests.get(LISTING_REQUEST)
    data = response.json()['resourceSets'][0]['resources'][0]['point']['coordinates']

    return data

#   print data

get_coordinates('555 W 116 St, New York NY 10027')

#if __name__ == '__main__':
 #   app.run(debug=True)
