#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, redirect
import requests
import urllib2 
import eatfood
import test2
import test3
import os
import random

import json 
app = Flask(__name__)


random.seed()
imgcount = random.randint(0, 65536)
def get_coordinates(query):
    LISTING_REQUEST='http://dev.virtualearth.net/REST/v1/Locations/'
    LISTING_REQUEST = LISTING_REQUEST + query
    LISTING_REQUEST = LISTING_REQUEST + '?key=AuuvwD9piSkUPB6tmyjruLS88Cecl-pR4SWViI4ucbfH7twMFD_Alr7Go6-P__11'
    response = requests.get(LISTING_REQUEST)
    data = response.json()['resourceSets'][0]['resources'][0]['point']['coordinates']

    return data
def is_member(results, query):
    for i in range(0, len(results)):
       if query in results[i]:
           return True
    return False


@app.route('/')
def hello_world():
    global imgcount
    #delete image files
    for k in range(1, 65536):
        deleted = 'static/image'
        deleted += str(k)
        deleted += '.jpeg'
        if os.path.isfile(deleted):
            os.remove(deleted)

    LISTING_REQUEST='http://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial/'
    coords = get_coordinates('555 W 116 St, New York NY 10027')
    LISTING_REQUEST += str(coords[0]) 
    LISTING_REQUEST += ',' 
    LISTING_REQUEST += str(coords[1])
    LISTING_REQUEST += '/17?mapSize=500,500&key=AuuvwD9piSkUPB6tmyjruLS88Cecl-pR4SWViI4ucbfH7twMFD_Alr7Go6-P__11'
    endpoint = LISTING_REQUEST
    response = requests.get(endpoint)
    with open('static/image.jpeg', 'wb') as f:
        for chunk in response.iter_content(4096):
            f.write(chunk)

    return render_template('index.html')

@app.route('/food', methods=['POST'])
def get_locs():
    global imgcount
    if request.form['foodtype'] is None or request.form['foodtype'] == "":
        return redirect('/')
    if request.form['location'] is None or request.form['location'] == "":
        return redirect('/')
    foodtype = request.form['foodtype']
    location = request.form['location']
    LISTING_REQUEST='http://dev.virtualearth.net/REST/v1/Imagery/Map/Road/'
    coords = get_coordinates(location)
    MY_COORDS = str(coords[0])
    MY_COORDS += ','
    MY_COORDS += str(coords[1])
    results1 = test3.yelp(MY_COORDS, foodtype)
    results2 = test2.foursquare(MY_COORDS, foodtype)
    LISTING_REQUEST += MY_COORDS
    LISTING_REQUEST += '/15?mapSize=800,800'
    count = 1
    restaurantNames = []

    for i in range(1, len(results1), 2):
        currentName = str(count)
        currentName += ": "
        currentName += results1[i-1]
        currentName += ", "
        currentName += results1[i]
        restaurantNames.append(currentName)
        coords = get_coordinates(results1[i]) 
        LISTING_REQUEST+= '&pp='
        LISTING_REQUEST+= str(coords[0])
        LISTING_REQUEST+= ','
        LISTING_REQUEST += str(coords[1])
        LISTING_REQUEST += ';;'
        LISTING_REQUEST += str(count)
        count = count + 1
        

    for i in range(1, len(results2), 2):
        if not is_member(restaurantNames, results2[i-1]):
            currentName = str(count)
            currentName += ": "
            currentName += results2[i-1]
            currentName += ", "
            currentName += results2[i]
            restaurantNames.append(currentName)
            coords = get_coordinates(results2[i]) 
            LISTING_REQUEST+= '&pp='
            LISTING_REQUEST+= str(coords[0])
            LISTING_REQUEST+= ','
            LISTING_REQUEST += str(coords[1])
            LISTING_REQUEST += ';;'
            LISTING_REQUEST += str(count)
            count = count + 1

    LISTING_REQUEST += '&dcl=1&key=AuuvwD9piSkUPB6tmyjruLS88Cecl-pR4SWViI4ucbfH7twMFD_Alr7Go6-P__11'
    response = requests.get(LISTING_REQUEST)
    filename = 'static/image' + str(imgcount) + '.jpeg'

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(4096):
            f.write(chunk)

    imgcount += 1 
    print restaurantNames[0]
    return render_template('food.html', img_num=filename, results=restaurantNames)

if __name__ == '__main__':
    app.run(debug=False)
