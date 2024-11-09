import requests

def get_elevation(lat, lon):
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
    response = requests.get(url)
    if response.status_code == 200:
        elevation = response.json()['results'][0]['elevation']
        return elevation
    else:
        print("Error fetching data")
        return None

# Read GPS data from source file
import pandas as pd

file_path = './GPS_Taxi_third_square.csv'
gps_data = pd.read_csv(file_path)

gps_data.drop(columns='date time', inplace=True)
gps_data['second'] = range(1, len(gps_data) + 1)
gps_data.insert(0, 'second', gps_data.pop('second'))

lat = gps_data['latitude'].tolist()
lon = gps_data['longitude'].tolist()
real_elevation = gps_data['altitude(m)'].tolist()


df = pd.DataFrame(columns=['real_elevation', 'elevation', 'diff'], index=range(3))
for i in range(len(lat)):
    elevation = get_elevation(lat[i], lon[i])
    diff = real_elevation[i] - elevation
    print('real_elevation:', real_elevation[i], '\n elevation:', elevation, '\n diff:', diff)
    df.at[i, 'real_elevation'] = real_elevation[i]
    df.at[i, 'elevation'] = elevation
    df.at[i, 'diff'] = diff

df = pd.read_csv('output_file.csv')









