from playerreader import PlayerReader
from playerstats import PlayerStats
from ui import UI

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/"
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    ui = UI(url, seasons)
    reader = PlayerReader(ui.select_season())
    stats = PlayerStats(reader)
    ui.import_stats(stats)

    while True:
        ui.show()

if __name__ == "__main__":
    main()
