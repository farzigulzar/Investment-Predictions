def scl(X,target_range):

    
    return X_scl, range

def test_train_split_lin_reg(raw):
    ''' 
        Return X_train, X_test, y_train, y_test
        standardise the values between [-1,1]
        train/test ratio should be 80/20 
    '''

    X=raw['Days']
    y=raw['Close']

    X_scl, _ =scl(X,[-1,1])
    y_scl, y_range=scl(y,[-1,1])
    # update the standd function

    X_train = X_scl[:split]
    X_test = X_scl[split:]

    y_train = y_scl[:split]
    y_test = y_scl[split:]
    # update the split number 

    return X_train, X_test, y_train, y_test, y_range