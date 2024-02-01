from matplotlib import pyplot as plt

def dig(raw):
    fig, ax = plt.subplots()
    ax.plot(raw['Days'],raw['Close'])

def draw_(x):
    fig, ax= plt.subplots()
    ax.plot(len(x),x)


def digvs2(y1,y2,x):
    fig, ax = plt.subplots()
    ax.plot(x,y1)
    plt.plot(x,y2)