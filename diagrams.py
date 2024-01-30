from matplotlib import pyplot as plt

def dig(raw):
    fig, ax = plt.subplots()
    ax.plot(raw['Days'],raw['Close'])