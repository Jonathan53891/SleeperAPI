# SleeperAPI
Wrote a few Python scripts for my fantasy football leagues in Sleeper.

The three python scripts can pull every current NFL player on the Sleeper platform (nfl_players.py), pull every player on each roster (game_of_inches_rosters.py), and web scrape calculated values for each player (player_values.py). 

The final Excel document (Fantasy Rosters (Game of Inches)) is a combination of the three Excel outputs (nfl_players.xlsx, game_of_inches_rosters.xlsx, player_values.xlsx). 
The document uses text-to-columns to parse the individual player IDs in Sleeper. 
Then, index formulas are used to map each current player on a team's roster to their specific owner in another tab. 
Lastly, VLOOKUP is used to determine the value of each player and is then used for analysis on the entire team as a whole. 
