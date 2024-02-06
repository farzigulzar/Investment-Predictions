from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import numpy as np
def ARIMA_model(X,p,d,q):
    arima_mod = ARIMA(X, order = (p,d,q))
    model_fit = arima_mod.fit()

    return model_fit

def check_stationary(X):
    test_=adfuller(X, autolag ='AIC')
    print('P Value : ', test_[1])
    print('Lags used : ', test_[2])

def create_series (y_start_arima, y_train_arima):
    '''
        y_start_arima => numpy int
        s => Dataframe
        y_create => numpy array
    '''

    y_create = np.array(y_start_arima)
    s= np.array(y_train_arima)
    final = np.append(y_create,s)

    for i in range(1,len(final)):
        final[i]=final[i-1]+final[i]
    
    return final