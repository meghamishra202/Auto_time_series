import pandas as pd
from sklearn.model_selection import train_test_split
df=pd.read_csv(r'C:\Users\pihu2\OneDrive\Documents\Sandlogic\Champagne Sales.csv')
print(df.head())
df['Month'] = pd.to_datetime(df['Month'])
df = df.sort_values('Month')


# will have to input date time column and target column from user
import pmdarima
from pmdarima.arima import auto_arima

# preprocessing part--- to check null values---

def check_null():
    if((df.isnull().sum().sum())==0):
        print("no null values... gtg")
    else:
        print("there should not be any NAN values")
        # Question- how can we deal with NaN values ...Forward fill????


# input date time and target column from the userr.
# date- time column, target- y column

df['Month']= pd.to_datetime(df['Month'])
df.set_index('Month', inplace= True)
#ts_column= df['Sales']

print(df.head())
import matplotlib.pyplot as plt
#df['Champagne sales'].plot()

# EDA- plotting the series

plt.plot(df['Champagne sales'])
plt.show()



from pmdarima.arima import ADFTest

# adfuller test for checking stationarity

adf_test = ADFTest(alpha = 0.05)
print(adf_test.should_diff(df))
t= adf_test.should_diff(df)

if(t[1]==False):
    print("data not stationary--------------> will select the value of d")

    # will do the train test split here

    train = df[:85]
    test = df[-20:]
    plt.plot(train)
    plt.plot(test)
    arima_model = auto_arima(train, start_p=0, d=1, start_q=0,
                             max_p=5, max_d=5, max_q=5, start_P=0,
                             D=1, start_Q=0, max_P=5, max_D=5,
                             max_Q=5, m=12, seasonal=True,
                             error_action='warn', trace=True,
                             supress_warnings=True, stepwise=True,
                             random_state=20, n_fits=50)
    arima_model.summary()
    prediction = pd.DataFrame(arima_model.predict(n_periods=20), index=test.index)
    prediction.columns = ['predicted_sales']
    prediction
    plt.figure(figsize=(8, 5))
    plt.plot(train, label="Training")
    plt.plot(test, label="Test")
    plt.plot(prediction, label="Predicted")
    plt.legend(loc='upper right')
    plt.show()
    from sklearn.metrics import r2_score

    test['predicted_sales'] = prediction
    r2_score(test['Champagne sales'], test['predicted_sales'])




else:
    print("stationary data------------> d will be none")