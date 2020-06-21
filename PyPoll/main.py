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

    for candidate in candidate_dict:
        votes = len(candidate_dict[candidate])
        percentage_votes = "{:.3%}".format(votes / total_votes * 100)
        print(f"{candidate}: {percentage_votes} ({votes})")