#import os

import os 

#import csv 
import csv 

#set path variable 

csvpath = os.path.join('Resources', 'budget_data.csv')
	
#Open csv using module. Set delimiter and variable holding content.

with open(csvpath) as csvfile:

	pybank_csv = csv.reader(csvfile,delimiter=',')

	#Check by reading header row. 

	pybank_header = next(pybank_csv)

	print(pybank_header)


#find lengeth of Date column 

#set variable to 0 

	pybank_months = 0 
	pybank_net = 0 
	greatest_increase = 0
	greatest_decrease = 0
	previous = 0 

#loop through rows to count months and find net profit and loss 
	for row in pybank_csv:  
		
		pybank_months += 1

		pybank_net += int(row[1])

		#average change in profit and loss
		if row[0] == "Jan-10":
			start = int(row[1])
		if row[0] == "Feb-17":
			end = int(row[1])
			average_change = round((end - start)/(pybank_months-1),2)

		# The greatest increase in profits (date and amount) over the entire period
		if int(row[1])-previous > greatest_increase:
			greatest_increase = int(row[1])-previous
			time_increase = row[0]

		# The greatest decrease in profits (date and amount) over the entire period
		if int(row[1])-previous < greatest_decrease:
			greatest_decrease = int(row[1])-previous
			time_decrease = row[0]
		previous = int(row[1])

	#print to terminal 	
	print('Financial Analysis')
	print('---------------------------')
	print(f'Total Months: {pybank_months}')
	print(f'Total: ${pybank_net}')
	print(f'Average Change: ${average_change}')
	print(f'Greatest Increase in Profits: {time_increase} ${greatest_increase}')
	print(f'Greatest Decrease in Profits: {time_decrease} ${greatest_decrease}')

pybank_txt = os.path.join('analysis','budget_data_output.txt')

with open(pybank_txt, 'w') as txtfile:
	txtfile.write(f'Financial Analysis\n---------------------------\n\tTotal Months: {pybank_months}\n\tTotal: ${pybank_net}\n\tAverage Change: ${average_change}\n\tGreatest Increase in Profits: {time_increase} ${greatest_increase}\n\tGreatest Decrease in Profits: {time_decrease} ${greatest_decrease}')

