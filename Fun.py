from pymongo import MongoClient
import pandas as pd
import time
import requests
import os
from dotenv import load_dotenv
import folium
from folium import Choropleth, Circle, Marker, Icon, Map, TileLayer
from folium.plugins import HeatMap, MarkerCluster
import geopandas as gpd
import json
import random

load_dotenv()
token=os.getenv("token")



def Mapa(lat, lon):
    origen = Map(location=[lat, lon], zoom_start=13)
    
    icon1 = Icon(
        color="lightred",
        prefix="fa",
        icon="gamepad",
        icon_color="white"
    )

    game = Marker(
        location=[lat, lon],
        tooltip="Game",
        icon=icon1
    )
    game.add_to(origen)
    
    return origen

    '''
        
    url = f"https://api.foursquare.com/v3/places/search?query=Starbucks&near={lat}%2C{lon}&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response = requests.get(url, headers=headers)
    coffe = response.json()["results"][0]
    loncoffe = coffe["location"]["lng"]
    latcoffe = coffe["location"]["lat"]
    
    icon2 = Icon(
        color="white",
        prefix="fa",
        icon="coffee",
        icon_color="green"
    )

    coffee = Marker(
        location=[latcoffe, loncoffe],
        tooltip="coffee",
        icon=icon2
    )
    coffee.add_to(origen)
    
    '''