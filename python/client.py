#!/usr/bin/env python3
"""
A simple HTTP client to test our API 
Usage:
    ./client.py
"""
import requests
# we request the url
data_json_name = {
    'name': 'Malik Sealy'
}
data_json = {
    'Name': 'Malik Sealy',
    'GP': 58,
    'MIN': 11.6,
    'PTS': 5.7,
    'FGM': 2.3,
    'FGA': 5.5,
    'FTM': 0.9,
    'FTA': 1.3,
    'OREB': 1.0,
    'DREB': 0.9,
    'REB': 1.9,
    'AST': 0.8,
    'STL': 0.6,
    'BLK': 0.1,
    'TOV': 1.0
}

def send_request(data):
    req = requests.post('http://localhost:8000/', json=data)

    # we raise an Exception if the status code is not 200
    if req.status_code != 200:
        raise Exception('Couldn\'t get open URL')
    else:
        print(req.content.decode())

if __name__ == '__main__':
    print("Sending just a name:")
    send_request(data_json_name)

    print("Sending stats to get a prediction")
    send_request(data_json)