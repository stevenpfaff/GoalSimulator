import random
from team import Team
from league import League

class Sim:
    def __init__(self):
        self.team = Team()
        self.league = League()
    def simulate(self):
        self.select_teams()

    def select_teams(self):
        print("Choose A Team")
        home_team_selection = input(f'1:{self.Team[0].name}, 2:{self.Team[1].name},')
        away_team_selection = input(f'1:{self.Team[0].name}, 2:{self.Team[1].name},')
        HomeTeam = home_team_selection
        AwayTeam = away_team_selection
        Games = int(input("Enter Amount of Games You'd Like to Simulate"))
        HomeWins = 0
        HomeLosses = 0
        HomePoints = 0
        AwayWins = 0
        AwayLosses = 0
        AwayPoints = 0
        Ties = 0
        TotalHomeGoals = 0
        TotalAwayGoals = 0
        TotalHomeShots = 0
        TotalAwayShots = 0

        for i in range(Games):
            HomeShots = 0
            HomeGoals = 0
            HomeSaves = 0
            AwayShots = 0
            AwayGoals = 0
            AwaySaves = 0

            # Home Shooting% logic set here
        #     if HomeOffense <= 20:
        #         #Shots On Goal Randomly Generated
        #         hSog = random.randint(13, 30)
        #         HomeShots += hSog
        #         TotalHomeShots += HomeShots
        #         for i in range(HomeShots):
        #             Goals = random.randrange(1, 1000)
        #             if Goals <= 68:
        #                 HomeGoals += 1
        #                 TotalHomeGoals += 1
        #             else:
        #                 HomeSaves += 1
        #     elif HomeOffense <= 30 & HomeOffense > 20:
        #         hSog = random.randint(18, 32)
        #         HomeShots += hSog
        #         TotalHomeShots += HomeShots
        #         for i in range(HomeShots):
        #             Goals = random.randrange(1, 1000)
        #             if Goals <= 76:
        #                 HomeGoals += 1
        #                 TotalHomeGoals += 1
        #             else:
        #                 HomeSaves += 1
        #     elif HomeOffense <= 40 & HomeOffense > 30:
        #         hSog = random.randint(20, 35)
        #         HomeShots += hSog
        #         TotalHomeShots += HomeShots
        #         for i in range(HomeShots):
        #             Goals = random.randrange(1, 1000)
        #             if Goals <= 83:
        #                 HomeGoals += 1
        #                 TotalHomeGoals += 1
        #             else:
        #                 HomeSaves += 1
        #     elif HomeOffense <= 50 & HomeOffense > 40:
        #         hSog = random.randint(22, 38)
        #         HomeShots += hSog
        #         TotalHomeShots += HomeShots
        #         for i in range(HomeShots):
        #             Goals = random.randrange(1, 1000)
        #             if Goals <= 86:
        #                 HomeGoals += 1
        #                 TotalHomeGoals += 1
        #             else:
        #                 HomeSaves += 1
        #     elif HomeOffense <= 60 & HomeOffense > 50:
        #         hSog = random.randint(25, 40)
        #         HomeShots += hSog
        #         TotalHomeShots += HomeShots
        #         for i in range(HomeShots):
        #             Goals = random.randrange(1, 1000)
        #             if Goals <= 89:
        #                 HomeGoals += 1
        #                 TotalHomeGoals += 1
        #             else:
        #                 HomeSaves += 1
        #     elif HomeOffense <= 70 & HomeOffense > 60:
        #         hSog = random.randint(28, 45)
        #         HomeShots += hSog
        #         TotalHomeShots += HomeShots
        #         for i in range(HomeShots):
        #             Goals = random.randrange(1, 1000)
        #             if Goals <= 93:
        #                 HomeGoals += 1
        #                 TotalHomeGoals += 1
        #             else:
        #                 HomeSaves += 1
        #     elif HomeOffense <= 80 & HomeOffense > 70:
        #         hSog = random.randint(30, 50)
        #         HomeShots += hSog
        #         TotalHomeShots += HomeShots
        #         for i in range(HomeShots):
        #             Goals = random.randrange(1, 1000)
        #             if Goals <= 105:
        #                 HomeGoals += 1
        #                 TotalHomeGoals += 1
        #             else:
        #                 HomeSaves += 1
        #
        # # Away Shooting% logic set here
        # if AwayOffense <= 20:
        #     aSog = random.randint(13, 30)
        #     AwayShots += aSog
        #     TotalAwayShots += AwayShots
        #     for i in range(AwayShots):
        #         Goals = random.randrange(1, 1000)
        #         if Goals <= 68:
        #             AwayGoals += 1
        #             TotalAwayGoals += 1
        #         else:
        #             AwaySaves += 1
        # elif AwayOffense <= 30 & AwayOffense > 20:
        #     aSog = random.randint(18, 32)
        #     AwayShots += aSog
        #     TotalAwayShots += AwayShots
        #     for i in range(AwayShots):
        #         Goals = random.randrange(1, 1000)
        #         if Goals <= 76:
        #             AwayGoals += 1
        #             TotalAwayGoals += 1
        #         else:
        #             AwaySaves += 1
        # elif AwayOffense <= 40 & AwayOffense > 30:
        #     aSog = random.randint(20, 35)
        #     AwayShots += aSog
        #     TotalAwayShots += AwayShots
        #     for i in range(AwayShots):
        #         Goals = random.randrange(1, 1000)
        #         if Goals <= 83:
        #             AwayGoals += 1
        #             TotalAwayGoals += 1
        #         else:
        #             AwaySaves += 1
        # elif AwayOffense <= 50 & AwayOffense > 40:
        #     aSog = random.randint(22, 38)
        #     AwayShots += aSog
        #     TotalAwayShots += AwayShots
        #     for i in range(AwayShots):
        #         Goals = random.randrange(1, 1000)
        #         if Goals <= 86:
        #             AwayGoals += 1
        #             TotalAwayGoals += 1
        #         else:
        #             AwaySaves += 1
        # elif AwayOffense <= 60 & AwayOffense > 50:
        #     aSog = random.randint(25, 42)
        #     AwayShots += aSog
        #     TotalAwayShots += AwayShots
        #     for i in range(AwayShots):
        #         Goals = random.randrange(1, 1000)
        #         if Goals <= 89:
        #             AwayGoals += 1
        #             TotalAwayGoals += 1
        #         else:
        #             AwaySaves += 1
        # elif AwayOffense <= 70 & AwayOffense > 60:
        #     aSog = random.randint(28, 45)
        #     AwayShots += aSog
        #     TotalAwayShots += AwayShots
        #     for i in range(AwayShots):
        #         Goals = random.randrange(1, 1000)
        #         if Goals <= 93:
        #             AwayGoals += 1
        #             TotalAwayGoals += 1
        #         else:
        #             AwaySaves += 1
        # elif AwayOffense <= 80 & AwayOffense > 70:
        #     aSog = random.randint(30, 50)
        #     AwayShots += aSog
        #     TotalAwayShots += AwayShots
        #     for i in range(AwayShots):
        #         Goals = random.randrange(1, 1000)
        #         if Goals <= 105:
        #             AwayGoals += 1
        #             TotalAwayGoals += 1
        #         else:
        #             AwaySaves += 1
        print(HomeTeam, "Shots:", HomeShots, "Goals:", HomeGoals, AwayTeam, "Shots:", AwayShots, "Goals:", AwayGoals)
        # Wins and Losses tracked here
        if AwayGoals > HomeGoals:
            AwayWins += 1
            HomeLosses += 1
            AwayPoints += 2
        elif HomeGoals > AwayGoals:
            HomeWins += 1
            AwayLosses += 1
            HomePoints += 2
        else:
            Ties += 1
            HomePoints += 1
            AwayPoints += 1

        print(HomeTeam, "Wins:", HomeWins, "Losses:", HomeLosses, "Ties:", Ties, "Points:", HomePoints)
        print(HomeTeam,"Total Goals:", TotalHomeGoals)
        print(HomeTeam,"Total Shots:", TotalHomeShots)
        print(AwayTeam, "Wins:", AwayWins, "Losses:", AwayLosses, "Ties:", Ties, "Points:", AwayPoints)
        print(AwayTeam, "Total Goals:", TotalAwayGoals)
        print(HomeTeam,"Total Shots:", TotalAwayShots)