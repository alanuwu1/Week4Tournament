#############################################
# Name: Your name
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
name = ["","Rajasthan Royals (RR)","Punjab Kings (PBKS)","Sunrisers Hyderabad (SRH)","Mumbai Indians (MI)","Chennai Super Kings (CSK)"]
wins=[0,0,0,0,0,0]
losses=[0,0,0,0,0,0]
ties=[0,0,0,0,0,0]

for i in range(6):
    print("Team Name ", i + 1)


    name[i] = input("Team name: ")
    wins[i] = int(input("wins: "))
    losses[i] = int(input("losses: "))
    ties[i] = int(input("ties:"))

    teampoints = wins * 2 + ties * 1

search = input("Hey, which team do you want information about? ")

for team in name:
    if search.lower() == team.lower():
        print("Team Name: " , team)
        print("Wins: ", team[1])
        print("Losses: ", team[3])
        print("team points: ", team[2])
        print("ties: ", team[4])

        team1 = input("Enter team 1 name: ")
        win1 = int(input(wins: ""))

    top = points.index(max(points))

    print("\nTop of the standings:", teams[top][0])