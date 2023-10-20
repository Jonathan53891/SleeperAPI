import requests
import pandas as pd

def get_rosters_data(league_id):
    url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch rosters data. Status Code: {response.status_code}")

def export_to_excel(rosters_data):
    df = pd.DataFrame(rosters_data)
    writer = pd.ExcelWriter('game_of_inches_rosters.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Game of Inches', index=False)
    writer.save()

if __name__ == "__main__":
    league_id = "917207160055136256"

    try:
        rosters_data = get_rosters_data(league_id)
        export_to_excel(rosters_data)
        print("Data exported to game_of_inches_rosters.xlsx successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
