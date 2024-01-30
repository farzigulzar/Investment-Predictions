from sklearn.Linear_model import LinearRegression

def model(X,y):
    lin_reg=LinearRegression()
    lin_reg.fit(X,y)

    return lin_reg