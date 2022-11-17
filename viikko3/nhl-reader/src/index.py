import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(
                player_dict['name'], player_dict['nationality'], player_dict['assists'], player_dict['goals'], player_dict['penalties'],
                player_dict['team'], player_dict['games']
            )

            players.append(player)

    print("Oliot:")

    sorted_players = sorted(players, key=lambda player: player.assists + player.goals, reverse=True)
    for player in sorted_players:
        print(player)

def sort_key(Player):
    return Player[2] + Player[3]

if __name__ == "__main__":
    main()
