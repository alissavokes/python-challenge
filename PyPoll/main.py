import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidate_dict = {}

with open(csvpath) as election_data_csv:
    read_election_data = csv.reader(election_data_csv, delimiter=',')
    next(election_data_csv)
    for row in read_election_data:
        voter_id = row[0]
        candidate = row[2]
        #counting each row after header for count of total votes
        total_votes = total_votes + 1

        if candidate not in candidate_dict:
            #creating array for each candidate to store voter ids
            candidate_dict[candidate] = []
            candidate_dict[candidate].append(voter_id)
        else:
            #storing voter ids for corresponding candidate
            candidate_dict[candidate].append(voter_id)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    prior_votes = 0
    for candidate in candidate_dict:
        votes = len(candidate_dict[candidate])
        percentage_votes = "{:.3f}".format(votes / total_votes * 100)
        print(f"{candidate}: {percentage_votes}% ({votes})")
        if votes > prior_votes:
            election_winner = candidate
        prior_votes = votes
    print("-------------------------")
    print(f"Winner: {election_winner}")

output_file = os.path.join("Analysis", "election_results.txt")
with open(output_file, "w") as datafile:
    datafile.write("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write("-------------------------\n")
    prior_votes = 0
    for candidate in candidate_dict:
        votes = len(candidate_dict[candidate])
        percentage_votes = "{:.3f}".format(votes / total_votes * 100)
        datafile.write(f"{candidate}: {percentage_votes}% ({votes})\n")
        if votes > prior_votes:
            election_winner = candidate
        prior_votes = votes
    datafile.write("-------------------------\n")
    datafile.write(f"Winner: {election_winner}\n")