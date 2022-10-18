import pandas as pd
from datetime import datetime

file = 'dataset.csv'

df = pd.read_csv(file)


#da controllare
subset_cols_q1_sensor_t = ['id_sensor', 'datetime', 'temperature', 'pressure', 
                    'humidity', 'nbrRoom']
sensor_t = pd.DataFrame(df, columns=subset_cols_q1_sensor_t)
sensorRoom_t_list = sensor_t.values.tolist()

lis = []
for l in sensorRoom_t_list:
    l[1] = round(l[1])
    l[4] = round(l[4])
    l[5] = round(l[5])
    elem = '{{id_sensor:'+str(l[0])+',datetime:'+str(l[1])+',temperature:'+str(l[2])+',pressure:'+str(l[3])+',humidity:'+str(l[4])+',nbrroom:'+str(l[5])+'}}'
    lis.append(elem)

sensor_T = pd.DataFrame(lis, columns=['device_equips'])
df['device_equips'] = sensor_T['device_equips']

subset_cols_q1_department = ['name_department', 'device_equips', 'device_type']
Department = pd.DataFrame(df, columns=subset_cols_q1_department)
Department.to_csv('department.csv', index=False)


subset_cols_q2_10_sensor_by_locality = ['locality', 'name_department', 'id_sensor', 'datetime', 'device_type', 'nbrRoom', 'temperature']

subset_cols_q4_8_sensorRoom = ['id_sensor', 'nbrRoom']
sensorRoom = pd.DataFrame(df, columns = subset_cols_q4_8_sensorRoom)
sensorRoom_list = sensorRoom.values.tolist()

new = []
for l in sensorRoom_list:
    l[1] = round(l[1])
    elem = '{{id_sensor:'+str(l[0])+',nbrroom:'+str(l[1])+'}}'
    new.append(elem)

sensorRoom_t = pd.DataFrame(new, columns = ['equips'])
df['equips']=sensorRoom_t['equips']


subset_cols_q4_8_device = ['device_type', 'id_device', 'equips', 'name_department']
device = pd.DataFrame(df, columns=subset_cols_q4_8_device)

#device.to_csv('device.csv', index=False)

subset_cols_q3_room = ['nbrRoom', 'temperature']

subset_cols_q5_6_7_9_sensor = ['datetime', 'id_sensor', 'temperature', 'humidity', 'name_department', 'nbrRoom', 'pressure']

sensor_by_locality = pd.DataFrame(df, columns = subset_cols_q2_10_sensor_by_locality)
#sensor_by_locality.to_csv('sensor_by_locality.csv', index=False)

room = pd.DataFrame(df, columns = subset_cols_q3_room)
#room.to_csv('room.csv', index=False)

sensor_by_datetime = pd.DataFrame(df, columns = subset_cols_q5_6_7_9_sensor)
#sensor_by_datetime.to_csv('sensor_by_datetime.csv', index=False)