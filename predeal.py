import csv
import pymongo


def write_csv():
    db_client = pymongo.MongoClient('localhost', 27017)
    db = db_client.okdeep
    tickers = db.tickers
    tickers_v2 = db.tickers_v2
    depths = db.depths
    depths_v2 = db.depths_v2

    for x in tickers.find():
        if x['_id'] == x['timestamp']:
            tickers.remove({'_id': x['_id']})

    tickers_v2.remove()
    for x in tickers.find():
        x['_id'] = x['timestamp']
        tickers_v2.insert_one(x)

    depths_v2.remove()
    for x in depths.find():
        x['_id'] = x['timestamp']
        depths_v2.insert_one(x)


if __name__ == '__main__':
    write_csv()
