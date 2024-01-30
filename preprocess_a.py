import numpy as np
from sklearn.preprocessing import MinMaxScaler

def remove(raw):
    ''' 
        Delete Na rows
        Delete Date,High,Low,Adj Close
    '''
    
    pd=raw.dropna()
    pd=pd.drop(['Date','High','Low','Adj Close'], axis=1)

    # adding days column instead of Date
    pd["Days"]=np.arange(len(pd['Close']))
    
    return pd


def normed_data(raw):
    scaler = MinMaxScaler()
    names=['Open', 'Close', 'Volume']
    raw[names] = scaler.fit_transform(raw[names])

    return raw