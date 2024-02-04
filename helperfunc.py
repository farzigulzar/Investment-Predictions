import pandas as pd


def scl(X,target_range):
    '''
        standardise the values between [-1,1]
        returns a tuple, so use indexing [0][i]
    '''
    #standardise values to 0,1
    xmin= min(X)
    xmax= max(X)
    X_std = (X-xmin)/(xmax-xmin)

    range=[xmin,xmax]

    # do the scaling to target[0] to target[1] 
    X_scl = X_std * (target_range[1]-target_range[0]) + target_range[0]

    # return the scaled X and range
    return X_scl, range

def test_train_split_arima(raw):
    X=raw['Days']
    y=raw['Close']

    split = int(len(X)*0.8)
    X_train = X.iloc[:split]
    X_test = X.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    return X_train, X_test, y_train, y_test



def test_train_split_lin_reg(raw):
    ''' 
        Return X_train, X_test, y_train, y_test
        standardise the values between [-1,1] using scl function
        train/test ratio should be 80/20 
    '''
    
    X=raw['Days']
    y=raw['Close']

    X_scl, _ = scl(X,[-1,1])
    y_scl, y_range = scl(y,[-1,1])

    split = int(len(X)*0.8)
    X_train = X_scl.iloc[:split]
    X_test = X_scl.iloc[split:]

    y_train = y_scl.iloc[:split]
    y_test = y_scl.iloc[split:]
    # check if this split method is working or not

    return X_train, X_test, y_train, y_test, y_range