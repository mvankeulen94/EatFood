from flask import Flask, request, render_template, redirect
import requests
import json

def foursquare(latlon, foodtype):
    LIST_REQUEST = 'https://api.foursquare.com/v2/venues/explore?ll=' + latlon + '&radius=700' + '&limit=10&query=' + foodtype + '&oauth_token=DZ4GXPUGZBTOOOVP1YM5CJPUYIOF5QWUWFYY5HJDY5SWSURN&v=20131109'
    response = requests.get(LIST_REQUEST)
    rest_and_location = []
    cut_response = response.json()['response']['groups'][0]['items']
    i = 0
    street = ""
    zip_code = ""
    city = ""
    state = ""
    while (len(cut_response) > i and len(rest_and_location) < 6):
        full = True
        if 'address' in cut_response[i]['venue']['location']:
            street = cut_response[i]['venue']['location']['address']
        else:
            full = False
        if 'postalCode' in cut_response[i]['venue']['location']:
            zip_code = cut_response[i]['venue']['location']['postalCode']
        else:
            full = False
        if 'city' in cut_response[i]['venue']['location']:
            city = cut_response[i]['venue']['location']['city']
        else:
            full = False
        if 'state' in cut_response[i]['venue']['location']:
            state = cut_response[i]['venue']['location']['state']
        else:
            full = False
        if full != False:
            rest_and_location.append(cut_response[i]['venue']['name'])
            rest_and_location.append(street + ", " + city + ", " + state + " " + zip_code)
        i = i + 1
    return rest_and_location
    
foursquare('40.807313025,-73.9621080458','sushi')
