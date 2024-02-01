from sklearn import linear_model
import helperfunc as hf

def model(X,y):
    lin_reg=linear_model.LinearRegression()
    lin_reg.fit(X,y)

    return lin_reg

def predict_index(model,x, range ):
    y= model.predict(x)
    y_output, _ = hf.scl(y,range)

    return y_output
