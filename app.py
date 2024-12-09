from flask import Flask, request, jsonify
from google.cloud import bigquery

app = Flask(__name__)

# Define project details
PROJECT_ID = "ncaambb-443717"
DATASET_ID = "march_madness"
TEAM_STATS_TABLE = f"{PROJECT_ID}.{DATASET_ID}.teams_data"


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
          t1.Season,
          t1.Team AS team1,
          t2.Team AS team2,
          -- Team1 stats
          t1.eFGp AS team1_eFGp,
          t1.TOVp AS team1_TOVp,
          t1.ORBp AS team1_ORBp,
          t1.FTr AS team1_FTr,
          t1.opp_eFGp AS team1_opp_eFGp,
          t1.opp_TOVp AS team1_opp_TOVp,
          t1.opp_ORBp AS team1_opp_ORBp,
          t1.opp_FTr AS team1_opp_FTr,
          t1.Wp AS team1_Wp,
          -- Team2 stats
          t2.eFGp AS team2_eFGp,
          t2.TOVp AS team2_TOVp,
          t2.ORBp AS team2_ORBp,
          t2.FTr AS team2_FTr,
          t2.opp_eFGp AS team2_opp_eFGp,
          t2.opp_TOVp AS team2_opp_TOVp,
          t2.opp_ORBp AS team2_opp_ORBp,
          t2.opp_FTr AS team2_opp_FTr,
          t2.Wp AS team2_Wp
        FROM 
          `ncaambb-443717.march_madness.teams_data` AS t1
          JOIN `ncaambb-443717.march_madness.teams_data` AS t2
          ON t1.Team = '{team1}' AND t2.Team = '{team2}' AND t1.Season = t2.Season
        WHERE t1.Season = {season}
        
      ))
    """
    query_job = client.query(query)
    result = [dict(row) for row in query_job]
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
