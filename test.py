from pnpoly import pnpoly
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    m = 10000

    vert = np.array(((-1,-1),(1,-1),(1,1),(-1,1)))

    test = np.random.randn(m,2)

    result = pnpoly(vert,test)

    dexi = np.where(result)[0]
    dexo = np.where(~result)[0]

    plt.plot(test[dexo,0],test[dexo,1],'b.')
    plt.plot(test[dexi,0],test[dexi,1],'r.')

    plt.show()
