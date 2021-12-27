from statsmodels.tsa.stattools import adfuller
from pmdarima.arima import ADFTest

class stationary:
    def __init__(self):
        "checking"
    def test_stationarity(selfself, df, target):
        # using adfuller test to check stationarity
        #Null hypothesis: the series is non-stationary.
        #If p >= alpha, the series is non-stationary.
        # If p < alpha, reject the null hypothesis
# uusing statsmodel for augment test

        # adfuller test for checking stationarity

        adf_test = ADFTest(alpha=0.05)
        print(adf_test.should_diff(df))
        t = adf_test.should_diff(df)

        if (t[1] == False):
            print("data not stationary--------------> will select the value of d")




