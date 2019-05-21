import os
import twstock
import StockDB

def main():
    StockCodeLst = 'StockCode.txt'

    aStDB = StockDB.StockDB()
    aStDB.SetCodeLst(StockCodeLst)
    #aStDB.GetAllStockCode(StockCodeLst)   => Initial Stock Code list. Only use it when we need to update

    # Load data from Web, and save it to *.json
    #aStDB.GetAllStockFromWeb()

    # Load data from *.json
    aStDB.GetAllStockFromFile()

    for aCode in aStDB.AllStockData.keys():
        aStockData = aStDB.AllStockData[aCode]
        try:
            print('Code: %s, Cap: %s, avg10Cap: %s' % (aCode, aStockData['price'][0], aStockData['avg10_Price'][0]))
        except:
            print('Error in Code %s' % aCode)

if __name__ == '__main__':main()
