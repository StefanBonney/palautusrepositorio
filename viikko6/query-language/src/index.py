from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, HasFewerThan, Not, PlaysIn, All

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)



    all = stats.matches(All()); print(len(all))  # 958

    '''
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    '''

    
    matcher = And(
    Not(HasAtLeast(2, "goals")),
    PlaysIn("NYR")
    )
    
    '''
    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    '''

    for player in stats.matches(matcher):
        print(player)




if __name__ == "__main__":
    main()
