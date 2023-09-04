
 # Moldel

import pandas as pd

data=pd.read_csv('prediction/prediction_Model/PROTOM_DEC2022_CSV_DATA_UPDATED.csv')
from sklearn.tree import DecisionTreeRegressor 
# create a regressor object

regressor = DecisionTreeRegressor(random_state = 0) 
y=data['BOX_PRICE'].values
x=data[["HIGH_TEMP","LOW_TEMP","HIMUDITY"]].values
# fit the regressor with X and Y data
regressor.fit(x,y)
def prd(a,b,c):
    price=regressor.predict([[a,b,c]])
    prd_value=int(price[0])
    return prd_value

# [request.GET['HT'],request.GET['HD'],request.GET['LT']]    