from pathlib import Path

# to be placed in the Steam/steamapps folder with appmanifest_***.acf files
# file 'games_sorted.txt' is created in the same folder; it contains the game names and the according acf files

def read_names():
    folder = Path()
    steam_files = folder.iterdir()
    for file in steam_files:
        if file.suffix == '.acf':
            with open(file, 'r', encoding='UTF-8') as f:
                for line in f:
                    next_line = line.lstrip()
                    if next_line.startswith('"name"'):
                        game_name = (next_line.split('\t\t')[1][1:-2])
                        break
            yield game_name, file
    print('No more acf files in this directory')
    return


all_games = {}

games = read_names()
if games:
    for g in games:
        all_games[g[0]] = g[1].name
        print(g[0], g[1].name)
    sorted_games = {k: all_games[k] for k in sorted(all_games)}
    print(sorted_games)


with open('games_sorted.txt', 'w+', encoding='UTF-8') as result_file:
    for item in sorted_games.items():
        print(item)
        result_file.write(item[0] + '\n' + item[1] + '\n\n')
