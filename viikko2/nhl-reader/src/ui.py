from rich import print as rprint
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

class UI:
    def __init__(self, url, seasons=""):
        self.url = url
        self.console = Console()
        self.seasons =  seasons
        rprint("\nNHL statistics by nationality\n")

    def import_stats(self, stats):
        self.stats = stats

    def select_season(self):
        seasons = f"[{'/'.join(self.seasons)}]"

        season = ""
        while season not in self.seasons:
            season = Prompt.ask(f"Select season [magenta]{seasons}[/magenta]")

        self.season = season

        return self.url + season + "/players"

    def select_national(self):
        nationalities = self.stats.get_nationalities()
        nation_str = f"[{'/'.join(nationalities)}]"

        nationality = ""
        while nationality not in nationalities:
            nationality = Prompt.ask(f"Select nationality [magenta]{nation_str}[/magenta]")
        return nationality

    def show(self):
        nation = self.select_national()
        players = self.stats.top_scorers_by_nationality(nation)
        print()

        table = Table(title=f"Top scorers of {nation} season {self.season}")
        table.add_column("name", justify="left", style="cyan", no_wrap=True)
        table.add_column("team", justify="right", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")

        for player in players:
            points = player.goals + player.assists
            
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(points))
        
        self.console.print(table)
        print()