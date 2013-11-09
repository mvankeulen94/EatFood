from flask import Flask, request, render_template, redirect
import requests
import json

def yelp(latlon, foodtype):
    lat = latlon.split(',')[0]
    lon = latlon.split(',')[1]
    rest_location = []
    LIST_REQUEST = 'http://api.yelp.com/business_review_search?term=' + foodtype + '&radius=0.5' + '&lat=' + lat + '&long=' + lon + '&limit=3&ywsid=32tTdedsTD1_uh4wha739w'
    response = requests.get(LIST_REQUEST)
    cut = response.json()['businesses']
    if len(cut) > 0:
        rest_location.append(cut[0]['name'])
        street = cut[0]['address1']
        city = cut[0]['city']
        state = cut[0]['state_code']
        zip_code = cut[0]['zip']
        whole = street + ', ' + city + ', ' + state + " " + zip_code
        rest_location.append(whole)
    if len(cut) > 1:
        rest_location.append(cut[1]['name'])
        street = cut[1]['address1']
        city = cut[1]['city']
        state = cut[1]['state_code']
        zip_code = cut[1]['zip']
        whole = street + ', ' + city + ', ' + state + " " + zip_code
        rest_location.append(whole)
    if len(cut) > 2:
        rest_location.append(cut[2]['name'])
        street = cut[2]['address1']
        city = cut[2]['city']
        state = cut[2]['state_code']
        zip_code = cut[2]['zip']
        whole = street + ', ' + city + ', ' + state + " " + zip_code
        rest_location.append(whole)
    return rest_location
    
yelp('40.807313025,-73.9621080458', 'food')
    
