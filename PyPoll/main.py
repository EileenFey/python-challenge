import csv

file = './Resources/election_data.csv'
with open (file, 'r') as data:
    
    csv_reader = csv.reader(data, delimiter=',')

    csv_header = next(csv_reader)

    print(f"CSV HEADER: {csv_header}")

    counter  = 0
    votes = {}

    #looping through the data structure we created
    for row in csv_reader:
        #Since each row is one ballet, we keeping adding one to the counter to get the total votes
        counter += 1
        #For each row this gets us the candidate's name
        candidate = row[2]
        #This gets us the each candidates total votes by adding every ballot to their dictionary entry
        votes[candidate] = votes.get(candidate, 0) + 1
        
    print(f"Ballots Cast: {counter}")
    print(votes)

    winner = ""
    winner_votes = 0

    #We are looping through the dictionary of candidates
    for name in votes:
        #This gets us the percentage of votes each candidate recieved by taking the nnumber of votes they recieved and dividing it by the total number of votes. It also provides candidate name and the total votes they recieved.
        print(f"{name} {votes[name]}   {(votes[name]/counter)*100:5,.2f}%\n")
        #If the winner votes is less than the current candidate's votes, then the winner votes becomes that candidates votes.
        if winner_votes < votes[name]: 
            winner_votes = votes[name]
            winner = name
    print(f"Winner: {winner}")

    lines = [f"{k + ':':24}" f"{votes[k]:10,}" f"{votes[k]/counter * 100:11,.2f}%\n"
    for k in sorted(votes)]

    # Generate the report string text
    report = (
        f"{' Election Results ':^46}\n"
        f"{'--':-^46}\n"
        f"{'Total Votes:':24}{counter:10,}{100:11,.2f}%\n"
        f"{'--':-^46}\n"
        f"{''.join(lines)}"
        f"{'--':-^46}\n"
        f"{'Winner:':10}{winner:>24}{votes[winner]/counter * 100:11,.2f}%\n"
        f"{'--':-^46}\n"
    )
    file = open("./Analysis/poll_text.txt","w")
    file.write(report)
    file.close
    
           



    