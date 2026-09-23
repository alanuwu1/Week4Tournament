#############################################
# Name: Your name
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
# name = ["","Rajasthan Royals (RR)","Punjab Kings (PBKS)","Sunrisers Hyderabad (SRH)","Mumbai Indians (MI)","Chennai Super Kings (CSK)"]
# wins=[0,0,0,0,0,0]
# losses=[0,0,0,0,0,0]
# ties=[0,0,0,0,0,0]
#
# for i in range(6):
#     print("Team Name ", i + 1)
#
#
#     name[i] = input("Team name: ")
#     wins[i] = int(input("wins: "))
#     losses[i] = int(input("losses: "))
#     ties[i] = int(input("ties:"))
#
#     teampoints = wins * 2 + ties * 1
#
# search = input("Hey, which team do you want information about? ")
#
# for team in name:
#     if search.lower() == team.lower():
#         print("Team Name: " , team)
#         print("Wins: ", team[1])
#         print("Losses: ", team[3])
#         print("team points: ", team[2])
#         print("ties: ", team[4])
#
#         team1 = input("Enter team 1 name: ")
#         win1 = int(input(wins: ""))
#
#     top = points.index(max(points))
#
#     print("\nTop of the standings:", teams[top][0])


team1 = input("Team 1")
wins1 = int(input("wins  "))
ties1 = int(input("ties   "))
losses1 = int(input("losses  "))
points1 = wins1 * 2 + ties1

team2 = input("Team 2")
wins2 = int(input("wins "))
ties2 = int(input("ties  "))
losses2 = int(input("losses  "))
points2 = wins2 * 2 + ties2

team3 = input("Team 3")
wins3 = int(input("wins "))
wins3 = int(input("wins "))
ties3 = int(input("ties  "))
losses3 = int(input("losses  "))
points3 = wins3 * 2 + ties3

team4 = input("team 4")
wins4 = int(input("wins "))
wins4 = int(input("wins "))
ties4 = int(input("ties  "))
losses4 = int(input("losses  "))
points4 = wins4 * 2 + ties4

team5 = input("Team 5")
wins5 = int(input("wins "))
wins5 = int(input("wins "))
ties5 = int(input("ties  "))
losses5 = int(input("losses  "))
points5 = wins5 * 2 + ties5

team6 = input("Team 6")
wins6 = int(input("wins "))
wins6 = int(input("wins "))
ties6 = int(input("ties  "))
losses6 = int(input("losses  "))
points6 = wins6 * 2 + ties6

print(team1, wins1, ties1, losses1, points1)
print(team2, wins2, ties2, losses2, points2)
print(team3, wins3, ties3, losses3, points3)
print(team4, wins4, ties4, losses4, points4)
print(team5, wins5, ties5, losses5, points5)
print(team6, wins6, ties6, losses6, points6)

top = max(points1, points2, points3, points4, points5, points6)

if top == points1:
    print("Top of the standings: ", team1)
elif top == points2:
    print("Top of the standings: ", team2)
elif top == points3:
    print("Top of the standings: ", team3)
elif top == points4:
    print("Top of the standings: ", team4)
elif top == points5:
    print("Top of the standings: ", team5)
elif top == points6:
    print("Top of the standings: ", team6)

