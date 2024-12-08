from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, HasFewerThan, Not, PlaysIn, All, Or
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)



    # all = stats.matches(All()); print(len(all))  # 958

    '''
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    '''

    '''
    matcher = And(
    Not(HasAtLeast(2, "goals")),
    PlaysIn("NYR")
    )
    '''
    
    '''
    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    '''

    '''
    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    '''

    '''
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    '''

    '''
    query = QueryBuilder()
    matcher = query.build()
    '''

    '''
    query = QueryBuilder()
    matcher = query.plays_in("NYR").build()
    '''

    query = QueryBuilder()
    matcher = (
      query
      .plays_in("NYR")
      .has_at_least(10, "goals")
      .has_fewer_than(20, "goals")
      .build()
    )

    for player in stats.matches(matcher):
        print(player)




if __name__ == "__main__":
    main()
