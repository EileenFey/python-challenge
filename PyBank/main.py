import csv

#Selecting file to open and open it
file = './Resources/budget_data.csv'
with open (file, 'r') as data:

    #Creating iterable data structure
    csv_reader = csv.reader(data, delimiter=',')

    #getting the first row and printing it
    csv_header = next(csv_reader)
    print(f"CSV HEADER: {csv_header}")

    #declaring variables
    counter = 0
    profit_loss = 0
    max_profit = 0
    max_profit_month = ""
    min_profit = 0
    min_profit_month = ""
    monthly_change = []
    previous_month = None

    #Looping through the data structure we created
    for row in csv_reader:
        #for each row that we are looping through this tells us the profit
        current_month_profit = int(row[1])
        #this gets us the month of the current row
        current_month = row[0]
        #since each row is a month, we add one for each row we are loop through
        counter += 1
        #for each row we add the current month's profit to this variable to get the total profit
        profit_loss += current_month_profit
        
        #When the max_profit is less than the current_month_profit then the max_profit becomes the current_month_profit
        if max_profit < current_month_profit: 
            max_profit = current_month_profit
            max_profit_month = current_month
        
        #When the min_profit is more than the current_month_profit then the min_profit becomes the current_month_profit
        if min_profit > current_month_profit:
            min_profit = current_month_profit
            min_profit_month = current_month
        
        #There is no previous month for the first month so we start at the second
        if previous_month is not None:
            #Change is the current monnth's profit minus the last months profit
            change = current_month_profit - previous_month 
            #We are getting the changes between every month so we can add them together later and calculate the average
            monthly_change.append(change)
        #We set the previous month equal to the current month so the next itteration of the loop uses this current month as its previous months
        previous_month = current_month_profit

    #The average change is equal to the sum of all of the monthly changes divided by the total number of months    
    average_change = sum(monthly_change)/len(monthly_change)
       
    print(f"Months: {counter}")
    print(f"profit/loss: {profit_loss}")
    print(f"profit change: {average_change}")
    print(f"max profit:  {max_profit_month} (${max_profit})")
    print(f"min profit: {min_profit_month} (${min_profit})")

    file = open("./Analysis/bank_text.txt","w")
    file.writelines(["Financial  Analysis \n", "-----------------------------\n" "Total Months:" + str(counter) + "\n", "Total: $" + str(profit_loss) +"\n", "Average Change: $" + str(average_change) + "\n", "Greatest Increase in Profits: $" +  str(max_profit) +"\n", "Greatest Decrease in Profits: $" + str(min_profit) + "\n"])
    file.close


   

    
    
   

