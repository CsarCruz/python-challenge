import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

votes=0
charles=0
diana=0
raymon=0
namecharles="Charles Casper Stockham"
namediana="Diana DeGette"
nameraymon="Raymon Anthony Doane"

with open(csvpath) as csvfile:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)


    for row in csvreader:
            #count total votes
            votes+=1
        
            if row[2]==namecharles:
                charles+=1
            elif row[2]==namediana:
                diana+=1
            elif row[2]==nameraymon:
                raymon+=1
if charles > diana and charles > raymon:
    winner=namecharles
elif diana > charles and diana > raymon:
    winner=namediana
elif raymon > diana and raymon > charles:
    winner=nameraymon
    


charlesperc=float(charles/votes)
dianaperc=float(diana/votes)
raymonperc=float(raymon/votes)
          
print("\n")
print("Election Results")
print("\n----------------------")
print(f"\nTotal Votes: {votes}")
print("\n----------------------")
print(f"\n{namecharles}: {round((charlesperc*100),3)}%  ({charles})")
print(f"\n{namediana}: {round((dianaperc*100),3)}%  ({diana})")
print(f"\n{nameraymon}: {round((raymonperc*100),3)}%  ({raymon})")
print("\n----------------------")
print(f"\nWinner: {winner}")
print("\n----------------------")

with open("results.txt","w") as f:
    f.write("Election Results")
    f.write("\n----------------------")
    f.write(f"\nTotal Votes: {votes}")
    f.write("\n----------------------")
    f.write(f"\n{namecharles}: {round((charlesperc*100),3)}%  ({charles})")
    f.write(f"\n{namediana}: {round((dianaperc*100),3)}%  ({diana})")
    f.write(f"\n{nameraymon}: {round((raymonperc*100),3)}%  ({raymon})")
    f.write("\n----------------------")
    f.write(f"\nWinner: {winner}")
    f.write("\n----------------------")