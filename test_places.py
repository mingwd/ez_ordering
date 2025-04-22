import requests
import json


API_KEY = ''
LOCATION = '47.6062,-122.3321'  # Seattle center
RADIUS = 500  # meter
TYPE = 'restaurant'

url = (
    f'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    f'?location={LOCATION}&radius={RADIUS}&type={TYPE}&key={API_KEY}'
)

response = requests.get(url)
data = response.json()

print(f"Found {len(data['results'])} restaurants: ")
for place in data['results']:
    print(f"- {place['name']}（{place.get('vicinity', 'no Addr')}）Rating：{place.get('rating', 'no Rating')}")

with open('places_output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

"""
Found 20 restaurants: 
- Kimpton Hotel Vintage Seattle（1100 5th Avenue, Seattle）Rating：4.3
- Purple Cafe and Wine Bar（1225 4th Avenue, Seattle）Rating：4.4
- Metropolitan Grill（820 2nd Avenue, Seattle）Rating：4.6
- Washington Athletic Club（1325 6th Avenue, Seattle）Rating：4.5
- Market Fresh（701 5th Avenue Class / Lab Service Area, Seattle）Rating：4.2
- Tulio（1100 5th Avenue, Seattle）Rating：4.4
- The Capital Grille（1301 4th Avenue, Seattle）Rating：4.6
- Moghul Express（701 5th Avenue # 111, Seattle）Rating：4.2
- Wild Ginger（1401 3rd Avenue, Seattle）Rating：4.3
- MOD Pizza（1302 6th Avenue, Seattle）Rating：4.4
- Owl N' Thistle（808 Post Avenue, Seattle）Rating：4.4
- Jimmy John's（1420 5th Avenue #200, Seattle）Rating：3.7
- The Triple Door（216 Union Street, Seattle）Rating：4.6
- Cherry Street Coffee House（700 1st Avenue, Seattle）Rating：4.4
- Original Deli（1215 4th Avenue # A-B, Seattle）Rating：4.8
- SHUCKERS OYSTER BAR（411 University Street, Seattle）Rating：4.4
- Sushi Kudasai（1420 5th Avenue #203, Seattle）Rating：4.4
- Collins Pub（526 2nd Avenue, Seattle）Rating：4.4
- TRACE Market（1112 4th Avenue, Seattle）Rating：4
- Vito's（927 9th Avenue, Seattle）Rating：4.5
"""