from flask import Flask, jsonify, render_template, request
from sportradar import NCAAMB
from NCAAMB import NCAAMB


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/get_league_hierarchy')
def get_league_hierarchy():
    ncaamb_api = NCAAMB(api_key='mvychbfvhmngbatf8ba7pege')
    response = ncaamb_api.get_league_hierarchy()
    if response.status_code == 200:
        league_hierarchy = response.json()
        return jsonify(league_hierarchy)
    else:
        return jsonify({"error": "Failed to fetch data"}), 500
    

# Add a new route in server.py

@app.route('/get_team_statistics/<season_year>/<season_type>/<team_id>')
def get_team_statistics(season_year, season_type, team_id):
    ncaamb_api = NCAAMB(api_key='mvychbfvhmngbatf8ba7pege')
    response = ncaamb_api.get_team_statistics(season_year, season_type, team_id)
    if response.status_code == 200:
        team_statistics = response.json()
        return jsonify(team_statistics)
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)