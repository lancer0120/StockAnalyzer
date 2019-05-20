import os
import twstock
import StockDB

def AnalysisOneCase(StockId):
    try:
        stock = twstock.Stock(str(StockId))
    except:
        print("Error in %d" % StockId)
        return "false"
    avg5 = stock.moving_average(stock.capacity,5)
    vol = stock.capacity
    for i in range(len(avg5)):
        if avg5[i]*3.5 < vol[i+4]:
            print("%d has large vol" % StockId)
            return "true"
    return "false"

def GenInputId():
    f = open("input.lst","w")
    
    for i in range(1000,9999):
        IsExisted = str(i) in twstock.twse
        if IsExisted:
            print("%d is existed, code = %s" % (i,IsExisted))
            f.write("%d\n" % i)
    f.close()


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

    #aStDB.LoadDB()

#GenInputId()
#f = open("input.lst","r")
#f_o = open("output.lst","w")
#for line in f:
#    line.rstrip()
#    rst = AnalysisOneCase(int(line))
#    if rst == "true":
#        f_o.write(line)
#    #print("process %d" % int(line))
#
#f.close()
#f_o.close()
#
if __name__ == '__main__':main()
