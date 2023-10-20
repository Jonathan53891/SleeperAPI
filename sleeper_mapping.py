import requests
import pandas as pd

def get_nfl_players_data():
    url = "https://api.sleeper.app/v1/players/nfl"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        return None

def convert_to_dataframe(players_data):
    player_list = []
    for player_id, player_info in players_data.items():
        player_list.append({
            'Player ID': player_id,
            'Name': player_info['full_name'],
            'Team': player_info['team'],
            'Position': player_info['position'],
            'ADP': player_info.get('adp', None),
            'Average Points': player_info.get('fantasy_points', None),
        })

    df = pd.DataFrame(player_list)
    return df

def export_to_excel(dataframe, output_file):
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    dataframe.to_excel(writer, sheet_name='NFL_Players', index=False)

    workbook = writer.book
    worksheet = writer.sheets['NFL_Players']

    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'fg_color': '#D7E4BC',
        'border': 1
    })

    for col_num, value in enumerate(dataframe.columns.values):
        worksheet.write(0, col_num, value, header_format)

    writer.save()

def main():
    players_data = get_nfl_players_data()

    if players_data:
        dataframe = convert_to_dataframe(players_data)
        output_file = 'nfl_players_data.xlsx'
        export_to_excel(dataframe, output_file)
        print(f"Data successfully exported to '{output_file}'.")

if __name__ == "__main__":
    main()
