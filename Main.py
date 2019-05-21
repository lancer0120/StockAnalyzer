import os
import twstock
import StockDB

def main():
    StockCodeLst = 'StockCode.txt'
    aStDB = StockDB.StockDB()

    #aStDB.GetAllStockCode(StockCodeLst)   => Initial Stock Code list. Only use it when we need to update

    with open(StockCodeLst) as Code_f:
        CodesLst = Code_f.read().strip().split()
    Cnt = 0
    for aCode in CodesLst:
        try:
            aStDB.GetOneStock(aCode)
        except:
            print('%s is Error' % aCode)
        Cnt = Cnt + 1
        print('%s: %s ... Processing ...' % (Cnt,aCode) )
        if Cnt % 50 == 0 : aStDB.SaveDB()
    #aStDB.GetOneStock('2330')
    #aStDB.GetOneStock('00672L')

    aStDB.SaveDB()

if __name__ == '__main__':main()
