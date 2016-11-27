import csv
import pymongo


def write_csv():
    db_client = pymongo.MongoClient('localhost', 27017)
    db = db_client.okdeep
    tickers = db.tickers
    depths = db.depths
    trades = db.trades


if __name__ == '__main__':
    write_csv()
