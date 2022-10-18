import pandas as pd
import random as rand
from datetime import datetime
from time import sleep


locality = ['Albaro', 'San Martino', 'Molo', 'Darsena', 'Prè', 'San Vincenzo', 'Castelletto']

loc_dep = {'San Martino': ['DIFI', 'DIMA', 'DCCI', 'DIBRIS'],
           'Albaro': ['DIME'],
           'Molo': ['DAD'],
           'Darsena': ['Economia'],
           'Prè': ['DAFIST', 'DIRAAS'],
           'San Vincenzo': ['DISFOR'],
           'Castelletto': ['DISPO']
           }

device_dep = {'DIFI':1,
              'DIMA':2,
              'DCCI':3,
              'DIBRIS':4,
              'DIME':5,
              'DAD':6,
              'Economia':7,
              'DAFIST':8,
              'DIRAAS':9,
              'DISFOR':10,
              'DISPO':11
           }

device_idsensors = {1: [1.1, 1.2, 1.3],
                    2: [2.1, 2.2, 2.3],
                    3: [3.1, 3.2, 3.3],
                    4: [4.1, 4.2, 4.3],
                    5: [5.1, 5.2, 5.3],
                    6: [6.1, 6.2, 6.3],
                    7: [7.1, 7.2, 7.3],
                    8: [8.1, 8.2, 8.3],
                    9: [9.1, 9.2, 9.3],
                    10: [10.1, 10.2, 10.3],
                    11: [11.1, 11.2, 11.3]
                    }


device_type = {1: 'Arduino',
               2: 'Raspberry pi',
               3: 'Arduino',
               4: 'Raspberry pi',
               5: 'Arduino',
               6: 'Raspberry pi',
               7: 'Arduino',
               8: 'Raspberry pi',
               9: 'Arduino',
               10: 'Raspberry pi',
               11: 'Arduino'
               }

idsensor_room = {1.1: 101,
                 1.2: 102,
                 1.3: 103,
                 2.1: 201,
                 2.2: 202,
                 2.3: 203,
                 3.1: 301,
                 3.2: 302,
                 3.3: 303,
                 4.1: 401,
                 4.2: 402,
                 4.3: 403,
                 5.1: 501,
                 5.2: 502,
                 5.3: 503,
                 6.1: 601,
                 6.2: 602,
                 6.3: 603,
                 7.1: 701,
                 7.2: 702,
                 7.3: 703,
                 8.1: 801,
                 8.2: 802,
                 8.3: 803,
                 9.1: 901,
                 9.2: 902,
                 9.3: 903,
                 10.1: 1001,
                 10.2: 1002,
                 10.3: 1003,
                 11.1: 1101,
                 11.2: 1102,
                 11.3: 1103
                }
     
def generate_temperature():
    return rand.uniform(7, 28)
    
def generate_humidity():
    return rand.randint(0, 100)

def generate_datetime():
    return round(datetime.now())
    
def generate_pressure():
    return rand.uniform(1013.25, 1013.6)

def generate_tuple(df):
    loc = rand.choice(locality)
    dep = rand.choice(loc_dep[loc])
    id_dev = device_dep[dep]
    dev_type = device_type[id_dev]
    id_sens = rand.choice(device_idsensors[id_dev])
    nbr_r = idsensor_room[id_sens]
    temp = generate_temperature()
    hum = generate_humidity()
    pres = generate_pressure()
    timestamp = generate_datetime()
    row = pd.Series([dep, loc, id_dev, dev_type, 
              id_sens, temp, hum, pres, timestamp, nbr_r], index=df.columns)
    
    df = df.append(row, ignore_index=True)
    return df

cols = ['name_department', 'locality', 'id_device', 
        'device_type', 'id_sensor', 'temperature', 'humidity', 
        'pressure', 'datetime', 'nbrRoom']

df = pd.DataFrame(columns = cols)

for i in range(0,30000):   
    df = generate_tuple(df)


df.to_csv('dataset.csv', index=False)

           

