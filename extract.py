import requests
import pandas as pd
responce=requests.get('https://jsonplaceholder.typicode.com/users')
data=responce.json()

df=pd.DataFrame(data)
print(df)
