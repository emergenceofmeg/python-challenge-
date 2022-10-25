#import os

import os 

#import csv 
import csv 

#set path variable 

csvpath = os.path.join('Resources', 'election_data.csv')
	
#Open csv using module. Set delimiter and variable holding content.

with open(csvpath) as csvfile:

	pypoll_csv = csv.reader(csvfile,delimiter=',')

	#Check by reading header row. 

	pypoll_header = next(pypoll_csv)

	print(pypoll_header)

	#define variables 

	total_votes = 0 
	Stockholm = 0 
	DeGette = 0 
	Doane = 0 


	candidates = []

	#define percent function 
	def percentage(a, b): 
		 return round(100 * (a/b),3) 


	#loop to find total votes 

	for row in pypoll_csv: 
		
		total_votes +=1


		#find candidate names 

		if row[2] not in candidates:
			name = row[2]
			candidates.append(name) 


		#Total number of votes for each candidate. Count votes through if statement. 
		if row[2] == candidates[0]:
			Stockholm +=1

		elif  row[2] == candidates[1]:
			DeGette +=1 
		else: 
			Doane +=1 

		#percentage of votes for each candidate

		per_Stockholm = percentage(Stockholm, total_votes)
		per_DeGette = percentage(DeGette, total_votes)
		per_Doane = percentage(Doane, total_votes)

		#Program to find winner 

		if per_Stockholm > per_DeGette:
			winner = candidates[0]
			winner_perc = per_Stockholm
		else:
			winner = candidates[1]
			winner_perc = per_DeGette
		if winner_perc > per_Doane:
			winner = winner 
		else: 
			winner = candidates[2]




	print(f'Election Results') 
	print(f'---------------------------')
	print(f'Total Votes: {total_votes}')
	print(f'---------------------------')
	print(f'{candidates[0]}: {per_Stockholm}% ({Stockholm})') 
	print(f'{candidates[1]}: {per_DeGette}% ({DeGette})')
	print(f'{candidates[2]}: {per_Doane}% ({Doane})')  
	print(f'---------------------------')
	print(f'Winner: {winner}')
	print(f'---------------------------')

	pypoll_txt = os.path.join('analysis','election_data_output.txt')

	with open(pypoll_txt, 'w') as txtfile:
		txtfile.write(f'Election Results\n---------------------------\n\tTotal Votes: {total_votes}\n---------------------------\n\t{candidates[0]}: {per_Stockholm}% ({Stockholm})\n{candidates[1]}: {per_DeGette}% ({DeGette})\n\t{candidates[2]}: {per_Doane}% ({Doane})\n---------------------------\n\tWinner: {winner}\n---------------------------')



