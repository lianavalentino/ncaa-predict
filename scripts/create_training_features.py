from google.cloud import BigQuery
def create_training_features():
  client = bigquery.Client()
  query = """
  SELECT
  tg.Season,
  tg.team1,
  tg.team2,
  tg.team1Score,
  tg.team2Score,
  tg.team1Win,
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
  (SELECT * FROM`ncaambb-443717.march_madness.tourney_games` WHERE Season >=2010) AS tg
LEFT JOIN 
  `ncaambb-443717.march_madness.teams_data` AS t1
  ON tg.Season = t1.Season AND tg.Team1 = t1.Team
LEFT JOIN 
  `ncaambb-443717.march_madness.teams_data` AS t2
  ON tg.Season = t2.Season AND tg.Team2 = t2.Team
ORDER BY 
  tg.Season, tg.Team1, tg.Team2;
"""
    # Execute query and save to BigQuery
    query_job = client.query(query)
    query_job.result()  # Wait for the job to complete

    # Store the results in a new BigQuery table
    table_id = "march_madness.team_stats"

    
    # Save the features table
    client.load_table_from_query(query, table_id, schema=schema).result()

if __name__ == "__main__":
    calculate_and_store_features()
