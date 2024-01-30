def test_train_split_lin_reg(raw):
    ''' 
        Return X_train, X_test, y_train, y_test
        standardise the values between [-1,1]
        train/test ratio should be 80/20 
    '''

    X=raw['Days']
    y=raw['Close']
    return X_train, X_test, y_train, y_test