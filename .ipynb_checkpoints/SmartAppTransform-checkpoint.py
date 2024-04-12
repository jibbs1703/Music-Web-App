# Import Necessary Libraries
import pandas as pd

# Columns Needed
href = []
ids = []
spotify = []
genre = []
total = []
name = []
popularity = []
types = []

columns = {}

def flatten(data):
    if type(data) == dict:
        
        for key in data.keys():
            if type(data[key]) in [str, int, None]:
                if key == 'href':
                    href.append(data[key])
                elif key == 'id':
                    ids.append(data[key])
                elif key == 'name':
                    name.append(data[key])
                elif key == 'type':
                    types.append(data[key])
                elif key == 'popularity':
                    popularity.append(data[key]) 
                elif key == 'spotify':
                        spotify.append(data[key])
                elif key == 'total':
                    total.append(data[key])               
            
            elif type(data[key]) == list:
                if sum([True for k in data[key] if type(k) == str]) == len(data[key]):
                    genre.append(data[key])
                else:
                     flatten(data[key])
            else: 
                flatten(data[key])
   
    elif type(data) == list:
        for item in data:
            flatten(item)

    else:
        print(f"{data} cannot be transformed at this time")
