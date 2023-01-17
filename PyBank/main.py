import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

date=0
prolo=0
datechange=0
change=0
avgchange=0
changelist=[]
greatinc=[0,""]
greatdec=[0,""]
date2=0


with open(csvpath) as csvfile:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)
    print(csvheader)

    for row in csvreader:
            #count total months
            date+=1
            date2=date-1

            #total Profit/Loses entire period
            prolo=prolo+float(row[1])


            #changes in Profit/Loses
            datechange=float(row[1]) - change
            change=float(row[1])
            #storing all changes
            changelist= changelist + [datechange]

            #calculating greatest decrease
            if datechange<greatdec[0]:
                greatdec[0]=datechange
                greatdec[1]=row[0]

            #calculating greatest increase
            if datechange> greatinc[0]:
                greatinc[0]=datechange
                greatinc[1]=row[0]



                

    #erasing first value of the list bacause have no change
    del changelist[0]
    #calculaten Avarage change in Profits Loses
    avgchange=sum(changelist)/date2
   
   
   
    #print(changelist) for testing
    #print(avgchange) for testing
    #file= csvfile.readlines() foun this one to count the rows but cracks the code
    

    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months: {(date)}")
    print(f"Average Change: $ {(avgchange)}")
    print(f"Greatest Increase in Profits {(greatinc[1])} (${(greatinc[0])})")
    print(f"Greatest Decrease in Profits {(greatdec[1])} (${(greatdec[0])})")
    
with open("results.txt","w") as f:
        f.write("\nFinancial Analysis")
        f.write("\n")
        f.write("\n-------------------")
        f.write("\n")
        f.write(f"\nTotal Months: {(date)}")
        f.write("\n")
        f.write(f"\nAverage Change: $ {(avgchange)}")
        f.write("\n")
        f.write(f"\nGreatest Increase in Profits {(greatinc[1])} (${(greatinc[0])})")
        f.write("\n")
        f.write(f"\nGreatest Decrease in Profits {(greatdec[1])} (${(greatdec[0])})")