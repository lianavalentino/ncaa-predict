from flask import Flask, request, jsonify
from google.cloud import bigquery

app = Flask(__name__)

# Define project details
PROJECT_ID = "ncaambb-443717"
DATASET_ID = "bracketology"
TEAM_STATS_TABLE = f"{PROJECT_ID}.{DATASET_ID}.four_factors"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    season = data['season']
    team1 = data['team1']
    team2 = data['team2']

    # Query BigQuery to get the trained model's predictions
    client = bigquery.Client()
    query = f"""
    SELECT
      predicted_label,
      probabilities
    FROM ML.PREDICT(MODEL `bracketology.ncaa_model_updated`,
      (
    SELECT
    t1.*,
    t2.team as opponent,
    t2.eFGp AS opp_eFGp,
    t2.TOVp AS opp_TOVp,
    t2.ORBp AS opp_ORBp,
    t2.FTR AS opp_FTR,
    t2.def_eFGp AS opp_def_eFGp,
    t2.def_TOVp AS opp_def_TOVp,
    t2.def_ORBp AS opp_def_ORBp,
    t2.def_FTR AS opp_def_FTR,
        FROM `{TEAM_STATS_TABLE}` t1
        JOIN `{TEAM_STATS_TABLE}` t2
        ON t1.team = '{team1}' AND t2.team = '{team2}' AND t1.season = t2.season
        WHERE t1.season = {season}
      ))
    """
    query_job = client.query(query)
    result = [dict(row) for row in query_job]
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
