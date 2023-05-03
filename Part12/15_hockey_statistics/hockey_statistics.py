import json

ask_file = input("file name:")
with open(ask_file) as my_file:
    data = my_file.read()
nhl_stats_file = json.loads(data)
print(f"read the data of {len(nhl_stats_file)} players")


class NhlStats():
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def name(self):
        return self.name

    def nationality(self):
        return self.nationality

    def assists(self):
        return self.assists

    def goals(self):
        return self.goals

    def penalties(self):
        return self.penalties

    def team(self):
        return self.team

    def games(self):
        return self.games

    def __str__(self):
        return f"{self.name:21}{self.team:3}{self.goals:4} +{self.assists:3} ={self.goals + self.assists:4}"
        # return f"{self.name} {self.nationality} {self.team} {self.assists} {self.goals} {self.penalties} {self.games}"


class NhlStatsApplication():
    def __init__(self):
        self.players = []

    def add_player(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        player = NhlStats(name, nationality, assists, goals, penalties, team, games)
        self.players.append(player)

    def instructions(self):
        instructions_str = """
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals"""
        print(instructions_str)

    def search(self):  # 1
        player_name = input("name: ")
        data = self.players
        for player in data:
            if player.name == player_name:
                print(player)

    def teams_list(self):  # 2
        data = self.players
        team_list = sorted(set([teams.team for teams in data]))
        for team in team_list:
            print(team)

    def countries(self):  # 3
        data = self.players
        countries = sorted(set([countries.nationality for countries in data]))
        for country in countries:
            print(country)

    def team_players(self):  # 4
        team = input("team: ")
        data = self.players
        data_filtered = sorted(filter(lambda teams: teams.team == team, data), key=lambda teams: teams.name)
        for player in data_filtered:
            print(player)

    def country_players(self):  # 5
        country = input("country: ")
        data = self.players
        data_filtered = sorted(filter(lambda countries: countries.nationality == country, data),
                               key=lambda teams: (teams.goals + teams.assists), reverse=True)
        for player in data_filtered:
            print(player)

    def most_points(self):  # 6
        how_many = int(input("how many: "))
        data = self.players
        data_filtered = sorted(data, key=lambda player: (player.goals + player.assists), reverse=True)

        count = 0
        for player in data_filtered:
            print(player)
            count += 1
            if count == how_many:
                break

    def most_goals(self):  # 7
        how_many = int(input("how many: "))
        data = self.players
        data_filtered = sorted(data, key=lambda player: (player.goals, -player.games), reverse=True)

        count = 0
        for player in data_filtered:
            print(player)
            count += 1
            if count == how_many:
                break

    def run(self):
        for data in nhl_stats_file:
            name = data["name"]
            nationality = data["nationality"]
            assists = data["assists"]
            goals = data["goals"]
            penalties = data["penalties"]
            team = data["team"]
            games = data["games"]
            self.add_player(name, nationality, assists, goals, penalties, team, games)
        self.instructions()
        while True:
            command = input("command: ")
            if command == "0":
                break
            if command == "1":
                self.search()
            if command == "2":
                self.teams_list()
            if command == "3":
                self.countries()
            if command == "4":
                self.team_players()
            if command == "5":
                self.country_players()
            if command == "6":
                self.most_points()
            if command == "7":
                self.most_goals()


# application below
NhlStatsApplication().run()
