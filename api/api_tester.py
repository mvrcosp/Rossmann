# %%
import pandas as pd
import requests
import json

# %%
dftest = pd.read_csv("/home/mvrcosp/repos/DSP/Rossmann/data/raw/test.csv")
dfstore = pd.read_csv("/home/mvrcosp/repos/DSP/Rossmann/data/raw/store.csv")

df = pd.merge(dftest, dfstore, how="left", on="Store")

# choose store for prediction
df_testing = df[df['Store'].isin( [20, 23, 22] )]

# remove closed days
df_testing = df_testing[df_testing['Open'] != 0]
df_testing = df_testing[~df_testing['Open'].isnull()]
df_testing = df_testing.drop( 'Id', axis=1 )

 # convert Dataframe to json
data = json.dumps( df_testing.to_dict( orient='records' ) )

 # API Call
#url = 'http://192.168.15.35:5000/rossmann/predict'
url = 'https://rossmann-model-mp.herokuapp.com/rossmann/predict'
header = {'Content-type': 'application/json' } 
data = data

# %%
r = requests.post( url, data=data, headers=header )
print( 'Status Code {}'.format( r.status_code ) )

# %%
d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )
 
# %%
d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

for i in range( len( d2 ) ):
    print( 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format( 
            d2.loc[i, 'store'], 
            d2.loc[i, 'prediction'] ) )

# %%
