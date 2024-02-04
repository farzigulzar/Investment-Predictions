from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
def ARIMA_model(X,p,d,q):
    arima_mod = ARIMA(X, order = (p,d,q))
    model_fit = arima_mod.fit()

    return model_fit

def check_stationary(X):
    test_=adfuller(X, autolag ='AIC')
    print('P Value : ', test_[1])
    print('Lags used : ', test_[2])