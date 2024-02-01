from statsmodels.tsa.arima.model import ARIMA

def ARIMA_model(X,p,d,q):
    arima_mod = ARIMA(X, order = (p,d,q))
    model_fit = arima_mod.fit()

    return model_fit
