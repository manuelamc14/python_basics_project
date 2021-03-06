# Modules
import os
import csv
import statistics

# Set path for file

csv_path = os.path.join("..", "Resources", "election_data.csv")
#csv_path = "../Resources/election_data.csv"
# Open csv

with open(csv_path) as csv_file:
    py_poll = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)

    csv_header = next(csv_file)

    # Starting variables

    total_votes = 0
    candidates = []

    for row in py_poll:
        # Total votes

        total_votes += 1
 
        # For readability, we store the data in one variable

        candidates.append(row[2])

    # A complete list of candidates who received votes
    
    candidate_list = list(set(candidates))

    # Define a function to summarize the candidate's results

    def results(candidate_name):

        # Starting a variable to store the votes per candidate

        votes_per_candidate = int(0)

        # Iterate through the candidate information

        for row in candidates:
            if candidate_name == row:
                votes_per_candidate += 1
        
        # Calculate the percentage of votes per candidate

        percentage = format(round((votes_per_candidate / total_votes)* 100, 2), '.3f')
        return "{}: {}% ({})".format(candidate_name, percentage, votes_per_candidate)

     #Find the winner 
   
    winner = statistics.mode(candidates)

    # Print the resulst out in the terminal

    print("Election Results")
    print("-------------------------")
    print("Total Votes: {}".format(total_votes))
    print("-------------------------")
    print(results('Khan'))
    print(results('Correy'))
    print(results('Li'))
    print(results("O'Tooley"))
    print('-------------------------')
    print('Winner: {}'.format(winner))

# Set the path for output file

output = os.path.join("Analysis","pypoll_analysis.txt")

# Open the file and write in the text document

with open(output, "w") as poll_results:
    poll_results.write("Election Results\n")
    poll_results.write("-------------------------\n")
    poll_results.write("Total Votes: {}\n".format(total_votes))
    poll_results.write("-------------------------\n")
    poll_results.write(("{}\n".format(results('Khan'))))
    poll_results.write(("{}\n".format(results('Correy'))))
    poll_results.write(("{}\n".format(results('Li'))))
    poll_results.write(("{}\n".format(results("O'Tooley"))))
    poll_results.write("-------------------------\n")
    poll_results.write('Winner: {}'.format(winner)) 
