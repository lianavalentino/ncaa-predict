from flask import Flask, request, jsonify
from google.cloud import bigquery

app = Flask(__name__)

# Define project details
PROJECT_ID = "ncaambb-443717"
DATASET_ID = "march_madness"
TEAM_STATS_TABLE = f"{PROJECT_ID}.{DATASET_ID}.teams_data"

@app.route('/train', methods=['POST'])
def train():
    client = bigquer.Client()
    query - """
    CREATE OR REPLACE MODEL
  `march_madness.model`
    OPTIONS
      ( model_type='logistic_reg') AS
    
    SELECT
    
      team1Win AS label,
      team1_Wp,
      team2_Wp
      #our offensive four factors
      team1_eFGp,
      team1_TOVp,
      team1_ORBp,
      team1_FTR,
      #our defensive four factores
      team1_opp_eFGp,
      team1_opp_TOVp,
      team1_opp_ORBp,
      team1_opp_FTR,
        #opp offensive four factors
      team2_eFGp,
      team2_TOVp,
      team2_ORBp,
      team2_FTR,
    
      #opp defensive four factores
      team2_opp_eFGp,
      team2_opp_TOVp,
      team2_opp_ORBp,
      team2_opp_FTR,
    
    FROM `march_madness.tournament_games_data`
    
    # here we'll train on 2013 - 2033 and predict on 2023
    WHERE Season BETWEEN 2013 AND 2022 

    """
    return jsonify({"message": "Model training completed and saved in GCP"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    season = data['season']
    team1 = data['team1']
    team2 = data['team2']

    # Query BigQuery to get the trained model's predictions
    client = bigquery.Client()
    query = f"""
    SELECT
      predicted_label_probs
    FROM ML.PREDICT(MODEL `march_madness.model`,
      (
    SELECT
    t1.*,
    t2.Team as team2,
    t2.eFGp AS team2_eFGp,
    t2.TOVp AS team2_TOVp,
    t2.ORBp AS team2_ORBp,
    t2.FTR AS team2_FTR,
    t2.opp_eFGp AS team2_opp_eFGp,
    t2.opp_TOVp AS team2_opp_TOVp,
    t2.opp_ORBp AS team2_opp_ORBp,
    t2.opp_FTR AS team2_opp_FTR,
        FROM `{TEAM_STATS_TABLE}` t1
        JOIN `{TEAM_STATS_TABLE}` t2
        ON t1.Team = '{team1}' AND t2.Team = '{team2}' AND t1.Season = t2.Season
        WHERE t1.Season = {season}
      ))
    """
    query_job = client.query(query)
    result = [dict(row) for row in query_job]
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
