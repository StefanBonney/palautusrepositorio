from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text

from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    
    season_options = Text("Select season ", style="default") + Text("[2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25]", style="magenta")
    nationality_options = Text("Select nationality ", style="default") + Text("[AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR]", style="magenta")

    season = Prompt.ask(season_options)
    nationality = Prompt.ask(nationality_options)

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)


    console = Console()

    table = Table(title=f"Top Scorers of {nationality} season {season}", caption="Season 2023-24", show_header=True, header_style="bold white")

    table.add_column("Name", style="blue")
    table.add_column("Team", style="purple")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")


    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))
    console.print(table)

main()