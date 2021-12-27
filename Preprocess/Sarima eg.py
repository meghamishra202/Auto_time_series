import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima import auto_arima
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
import  numpy as np


data= pd.read_csv(r'C:\Users\pihu2\OneDrive\Documents\Sandlogic\Auto_sarima.csv')
print(data.head())

#making sure our data doent have any null values
def check_null():
    if((data.isnull().sum().sum())==0):
        print("no null values... gtg")
    else:
        print("there should not be any NAN values")

data = data.rename(columns = {"IPG2211A2N":"Energy Production"})
#converting index to date time format
data['DATE']= pd.to_datetime(data['DATE'])
data.set_index('DATE', inplace= True)


#visualizing the series
plt.plot(data['Energy Production'])
plt.show()

stepwise_model = auto_arima(data, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',
                           suppress_warnings=True,
                           stepwise=True)
print(stepwise_model.aic())
#train test split here
train = data.loc['1985-01-01':'2016-12-01']
print(train.tail())
test = data.loc['2015-01-01':]
periods_to_predict= len(test)
print(test.head())
stepwise_model.fit(train)
future_forecast = stepwise_model.predict(n_periods=periods_to_predict)
print(future_forecast)

#plt.figure(figsize=(16, 8), dpi=150)

# using plot method to plot open prices.
# in plot method we set the label and color of the curve.
#test.plot(label='Test', color='orange')
#future_forecast.plot(label='prediction')

# adding title to the plot
#plt.title('Plot')
#plt.legend()
#plt.show()
#testing the accuracy of the model
rmse = lambda act, pred: np.sqrt(mean_squared_error(act, pred))
print(f'RMSE: {rmse(test, future_forecast)}')
