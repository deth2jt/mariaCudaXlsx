#!/usr/bin/env python
#reset; python3.6 readXls13CU3.py -i 'Dbx1-E13_Raw data_Counts with EGFP_names.xlsx' -o foo.xlsx
import Maria13
import xlrd
import xlwt
import sys
from numba import cuda, float32
import numpy
import math
#from numba import float32


starts = "ENSMUSG"
#writeToFile = 'writeFileOut.xlsx'
#fileName = 'Dbx1-E13_Raw data_Counts with EGFP_names1.xlsx'
#writeToXls(orderCells())
#added for git changes for jenkins hooks
threadsPerBlock = 1024
IMP0LEN = 0

def getRowCount(fileName):
    workbook = xlrd.open_workbook(fileName)
    worksheet = workbook.sheet_by_index(0)
    count = worksheet.nrows
    workbook.release_resources()
    print("Count: ", count)
    return count -2

def getLen(fileName):
    print ('Get column length...')
    workbook = xlrd.open_workbook(fileName)
    worksheet = workbook.sheet_by_index(0)

    row = 2

    IMP0LEN = 0
    IMP1LEN = 0
    IMP2LEN = 0

    impCount = 0
    count = 0

    try:
        val = str(worksheet.cell(row, count).value)
    
        while(val != xlrd.XL_CELL_EMPTY):
        
            #print "count",count
        
            if(val.startswith( starts )):
                if(impCount == 0):
                    IMP0LEN = count + 1
                elif(impCount == 1):
                    IMP1LEN = count + 1
                elif(impCount == 2):
                    IMP2LEN = count + 1
                
                impCount = impCount + 1

            count = count + 1
            val = str(worksheet.cell(row, count).value)
            
    except IndexError:
        return (IMP1LEN - (IMP0LEN + 1), IMP2LEN - (IMP1LEN + 1) , count - IMP2LEN)
    return (IMP1LEN - (IMP0LEN + 1), IMP2LEN - (IMP1LEN + 1) , count - IMP2LEN)

        
def get_market_list1(fileName):
    workbook = xlrd.open_workbook(fileName)
    worksheet = workbook.sheet_by_index(0)

    
    MariaList = []
    

    LEN = getLen(fileName)

    IMP0LEN = LEN[0]
    IMP1LEN = LEN[1]
    IMP2LEN = LEN[2]
        

    count = 2
    try:
        
        while( (worksheet.cell_type(count, 0) != xlrd.XL_CELL_EMPTY)):
                IMP0=str(worksheet.cell(count, 0).value)
                IMP0F1=str(worksheet.cell(count, 1).value)
                IMP0F2=str(worksheet.cell(count, 2).value)
                IMP0F3=str(worksheet.cell(count, 3).value)
                IMP0F4=str(worksheet.cell(count, 4).value)
                IMP0F5=str(worksheet.cell(count, 5).value)
                IMP0F6=str(worksheet.cell(count, 6).value)

                increment = 0
                if(IMP0LEN == 8):
                    IMP0F7=str(worksheet.cell(count, 7).value)
                    #print "IMP0F7", IMP0F7
                    IMP0F8=str(worksheet.cell(count, 8).value)
                    increment = 2

                
                IMP1=str(worksheet.cell(count,  7 + increment).value)
                #print "IMP1IMP1",IMP1
                
                IMP1F1=str(worksheet.cell(count, 8+ increment).value)
                IMP1F2=str(worksheet.cell(count, 9 + increment).value)
                IMP1F3=str(worksheet.cell(count, 10 + increment).value)

                
                IMP2=str(worksheet.cell(count, 11 + + increment).value)
                IMP2F1=str(worksheet.cell(count, 12 + increment).value)
                IMP2F2=str(worksheet.cell(count, 13 +  increment).value)
                IMP2F3=str(worksheet.cell(count, 14  + increment).value)
                #print 'IMP2F2', IMP2F2

                if(IMP0LEN == 8):
                    excelCell = Maria13.Maria13(IMP0,IMP0F1,IMP0F2,IMP0F3,IMP0F4,IMP0F5,IMP0F6, IMP0F7, IMP0F8, IMP1,IMP1F1,IMP1F2,IMP1F3,IMP2,IMP2F1,IMP2F2,IMP2F3)
                    excelCell.setIMPLENS(IMP0LEN, IMP1LEN, IMP2LEN)
                else:
                    excelCell = Maria13.Maria13(IMP0,IMP0F1,IMP0F2,IMP0F3,IMP0F4,IMP0F5,IMP0F6, '', '', IMP1,IMP1F1,IMP1F2,IMP1F3,IMP2,IMP2F1,IMP2F2,IMP2F3)
                    excelCell.setIMPLENS(IMP0LEN, IMP1LEN, IMP2LEN)
                MariaList = MariaList + [excelCell]
                count = count + 1
                #print count

    except IndexError:
        return MariaList
    return MariaList


def orderCells(fileName):
    mList = get_market_list1(fileName)
    mList2 = get_market_list1(fileName)
    print ("done getting list")
    for num in range(len(mList)):
        if(num % 500 == 0):
            print ("odering this: ",num)
        match = False
            
        if(mList[num].getIMP0 != mList[num].getIMP1()):
            for count in range(len(mList2)):
                #print "not same"
                if(mList[num].getIMP0() == mList2[count].getIMP1()):
                    lst = mList2[count].getIMP1List()
                    mList[num].setIMP1(lst[0],lst[1],lst[2],lst[3], '','')
                    #print "lst[0]", lst[0]
                    match = True
                    count = len(mList2)

            if(not match):
                    #m = maria()
                mList[num].setIMP1ToBlank()
            match = False

        if(mList[num].getIMP0() != mList[num].getIMP2()):
            for count in range(len(mList2)):
                    
                if(mList[num].getIMP0() == mList2[count].getIMP2()):
                    lst = mList2[count].getIMP2List()
##                    print lst
                    mList[num].setIMP2(lst[0],lst[1],lst[2],lst[3], '', '')
                    match = True
                    count = len(mList2)

                if(not match):
                    #m = maria()
                    mList[num].setIMP2ToBlank()
    return mList    

def convertValToInt(lst):
    
    if(starts in lst):
        lst = lst[7:]
        
        for num in range(len(lst)):
            if(lst[num] == '0'):
                lst[num+1:]
        return int(lst) 
    else:
        return 0        

def convertToListPostion(mariaList):
    lst1 = []
    lst2 = []
    lst3 = []

    for num in range(len(mariaList)):
        lst1 += [[  convertValToInt(mariaList[num].getIMP0()), num]]
        lst2 += [[  convertValToInt(mariaList[num].getIMP1()), num]]
        lst3 += [[  convertValToInt(mariaList[num].getIMP2()), num]]
    return (lst1, lst2, lst3)


def convertToMariaOrdList(mariaList, orderLst):

    MariaList = []
    for num in range(len(orderLst)):

        val = orderLst[num]
        mariaLstCurrent = mariaList[val[0]-1]
        IMP0LEN = mariaList[val[0]-1].getIMP0LEN() 
        IMP1LEN = mariaLstCurrent.getIMP1LEN() 
        IMP2LEN = mariaLstCurrent.getIMP2LEN() 

        IMP0List=mariaLstCurrent.getIMP0List()
        IMP1List=mariaList[val[1]-1].getIMP1List()
        IMP2List=mariaList[val[2]-1].getIMP2List()
        
        if (IMP2List[2] is None):
            IMP2List[2]='' 
        else:
            IMP2List[2]=IMP2List[2]

        if (IMP2List[3] is None):
            IMP2List[3]='' 
        else:
            IMP2List[3]=IMP2List[3]

        if(IMP0LEN == 8):
            newMariaList = Maria13.Maria13(IMP0List[0],IMP0List[1],IMP0List[2],IMP0List[3],IMP0List[4],IMP0List[5],IMP0List[6], IMP0List[7], IMP0List[8], IMP1List[0],IMP1List[1],IMP1List[2],IMP1List[3],IMP2List[0],IMP2List[1],IMP2List[2],IMP2List[3])
            newMariaList.setIMPLENS(IMP0LEN, IMP1LEN, IMP2LEN)
        else:
            newMariaList = Maria13.Maria13(IMP0List[0],IMP0List[1],IMP0List[2],IMP0List[3],IMP0List[4],IMP0List[5],IMP0List[6], '','', IMP1List[0],IMP1List[1],IMP1List[2],IMP1List[3],IMP2List[0],IMP2List[1],IMP2List[2],IMP2List[3])
            newMariaList.setIMPLENS(IMP0LEN, IMP1LEN, IMP2LEN)
            MariaList = MariaList + [newMariaList]
        print (newMariaList)
    return MariaList


def writeToXls(mariaList, outfile):
    f= open(outfile,"w+")
    f.close() 

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Sheet_1')
    

    
    count = 0
    for num in range(len(mariaList)):
        if(num % 500 == 0):
            print( "writing this: ",num)
        lst0 = mariaList[num].getIMP0List()
        lst1 = mariaList[num].getIMP1List()
        lst2 = mariaList[num].getIMP2List()

        
        sheet.write(count + num, 0,lst0[0])
        sheet.write(count + num, 1,lst0[1])
        sheet.write(count + num, 2,lst0[2])
        sheet.write(count + num, 3,lst0[3])
        sheet.write(count + num, 4,lst0[4])
        sheet.write(count + num, 5,lst0[5])
        sheet.write(count + num, 6,lst0[6])


        
        increment = 0
        if(mariaList[num].getIMP0LEN() == 8):
            sheet.write(count + num, 7,lst0[6])
            sheet.write(count + num, 8,lst0[7])
            increment = 2
        
        sheet.write(count + num, increment + 7,lst1[0])
        
        sheet.write(count + num, increment + 8,lst1[1])
        sheet.write(count + num, increment + 9,lst1[2])
        sheet.write(count + num, increment + 10,lst1[3])

        
        sheet.write(count + num, increment + 11,lst2[0])
        sheet.write(count + num, increment + 12,lst2[1])
        sheet.write(count + num, increment + 13,lst2[2])
        sheet.write(count + num, increment + 14,lst2[3])
    workbook.save(outfile)
    
    return True


@cuda.jit
def orderedCuda(lst0, lst1, lst2, dest, lenOfRec):
    x = cuda.grid(1)
    
    val = lst0[x][0]
    for i in range(lenOfRec):
            
            
            if(val == lst1[i][0] ):
                dest[x][0] = lst0[x][1]+1
                dest[x][1] = lst1[i][1]+1
            if(val == lst2[i][0] ):
                dest[x][0] = lst0[x][1]+1
                dest[x][2] = lst2[i][1]+1
            cuda.syncthreads()
    
if __name__ == '__main__':
    from optparse import OptionParser
    
    parser = OptionParser()
    
    parser.add_option("-i", "--infil", dest="fileName", help="name of file to order", metavar="in_file_name")
    parser.add_option("-o", "--outfile", dest="outputfileName", default='writeFileOut.xlsx', help="name of file to output to", metavar="output_file_name")
    

    (options, args) = parser.parse_args()
    #print 'options: %s, args: %s' % (options, args)


    if not(options.fileName):
	    print( 'need input file name')

    else:
        #check = True
        mariaList = get_market_list1(options.fileName)
        lst = convertToListPostion(mariaList)
        
    	
        numOfRec = getRowCount(options.fileName)

        lst0= numpy.array( lst[0])
        lst1= numpy.array( lst[1])
        lst2= numpy.array( lst[2])
        dest = numpy.full((numOfRec, 3), 0, numpy.int)
        

        lst0_global_mem = cuda.to_device(lst0)
        lst1_global_mem = cuda.to_device(lst1)
        lst2_global_mem = cuda.to_device(lst2)
        dest_global_mem = cuda.to_device(dest)


        # Configure the blocks
        threadsperblock = (threadsPerBlock, 1)
        blockspergrid_x = int(math.ceil(lst0.shape[0] / threadsperblock[0]))
        blockspergrid_y = 1
        blockspergrid = (blockspergrid_x, blockspergrid_y)

        # Start the kernel 
        orderedCuda[blockspergrid, threadsperblock](lst0_global_mem, lst1_global_mem, lst2_global_mem, dest_global_mem,numOfRec)
        res = dest_global_mem.copy_to_host()
      
        
        check = writeToXls(convertToMariaOrdList(mariaList, res), options.outputfileName)

        print ('App returned %s' % check)
        sys.exit(not check)
