import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class preprocess:
    def __init__(self):
        self.ts_time_column=None
        self.trai_data= None
        self.y=None
        self.time_interval=None
    def check_date_column(self,date, X_train, target):
        self.ts_time_column=date
        self.trai_data=X_train
        self.y=target
        #making the date/time column as index of the dataframe
        if X_train.index.dtype == 'int' or X_train.index.dtype == 'float':
            X_train = X_train.set_index(self.ts_time_column)
        ts_index = X_train.index

        # time interval will be taken as the input from the user
        if(self.time_interval is None):
            ts_index = pd.to_datetime(X_train.index)
            diff = (ts_index[1] - ts_index[0]).to_pytimedelta()
            # pytimedelata is a unit for measuring difference in time.. in-built library
            diffdays = diff.days
            diffsecs = diff.seconds
            if diffsecs == 0:
                diff_in_hours = 0
                diff_in_days = abs(diffdays)
            else:
                diff_in_hours = abs(diffdays*24*3600 + diffsecs)/3600
            if diff_in_hours == 0 and diff_in_days >= 1:
                print('Time series input in days = %s' % diff_in_days)
                if diff_in_days == 7:
                    print('It is a Weekly time series.')
                    self.time_interval = 'weeks'
                elif diff_in_days == 1:
                    print('It is a Daily time series.')
                    self.time_interval = 'days'
                elif 28 <= diff_in_days < 89:
                    print('It is a Monthly time series.')
                    self.time_interval = 'months'
                elif 89 <= diff_in_days < 178:
                    print('It is a Quarterly time series.')
                    self.time_interval = 'qtr'
                elif 178 <= diff_in_days < 360:
                    print('It is a Semi Annual time series.')
                    self.time_interval = 'semi'
                elif diff_in_days >= 360:
                    print('It is an Annual time series.')
                    self.time_interval = 'years'
                else:
                    print('Time Series time delta is unknown')
                    return None
            if diff_in_days == 0:
                if diff_in_hours == 0:
                    print('Time series input in Minutes or Seconds = %s' % diff_in_hours)
                    print('It is a Minute time series.')
                    self.time_interval = 'minutes'
                elif diff_in_hours >= 1:
                    print('It is an Hourly time series.')
                    self.time_interval = 'hours'
                else:
                    print('It is an Unknown Time Series delta')
                    return None
        else:
            print('Time Interval is given as %s' % self.time_interval)

        # we will have to make some assigned labels for time interval taken as input from user,
        # eg:- M- months, Y- years
        # we will then have to check whether our self,time_interval is valid.


        # checking stationarity of data
        test_stationarity(X_train, date, target)







