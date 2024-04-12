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

def flatten(data, append=None):
    if type(data) == dict:
        
        for key in data.keys():
            if type(data[key]) in [str, int, None]:
                if key == 'href':
                    href.append(data[key])
                    columns[key] = href
                elif key == 'id':
                    ids.append(data[key])
                    columns[key] = ids
                elif key == 'name':
                    name.append(data[key])
                    columns[key] = name
                elif key == 'type':
                    types.append(data[key])
                    columns[key] = types                    
                elif key == 'popularity':
                    popularity.append(data[key])
                    columns[key] = popularity 
                elif key == 'spotify':
                    spotify.append(data[key])
                    columns[key] = spotify   
                elif key == 'total':
                    total.append(data[key])
                    columns[key] = total                    
            
            elif type(data[key]) == list:
                if sum([True for k in data[key] if type(k) == str]) == len(data[key]):
                    if key == 'genres':
                        genre.append(data[key])
                        columns[key] = genre
            else: 
                flatten(data[key])
   
    elif type(data) == list:
        for item in data:
            flatten(item)

    else:
        print(f"{data} cannot be transformed at this time")

    return columns
