import pymongo
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

db_client = pymongo.MongoClient('localhost', 27017)
db = db_client.okdeep
depths = db.depths

X, Y, Z = [], [], []

data = depths.find({}).sort('_id')
index = 0;
for item in data:
    pairs = item['asks'] + item['bids']
    pairs.reverse()
    for pair in pairs:
        X.append(int(item['_id']))
        Y.append(pair[0])
        Z.append(pair[1])
        index += 1

    if index > 1000:
        break


def show():
    fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
    # X, Y, Z = axes3d.get_test_data(0.05)
    ax1.plot_wireframe(X, Y, Z, rstride=1000, cstride=0)
    ax1.set_title("Column stride 0")
    ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=1000)
    ax2.set_title("Row stride 0")
    plt.tight_layout()
    plt.show()


def scatter():
    N = len(X)
    x = Y
    y = Z
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N)) ** 2  # 0 to 15 point radiuses

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()


if __name__ == '__main__':
    show()
    # scatter()
