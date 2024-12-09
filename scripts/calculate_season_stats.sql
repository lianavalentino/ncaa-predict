SELECT
  Season,
  team1 AS Team,
  -- Calculating season averages for team1's metrics
  AVG(team1_eFGp) AS eFGp,
  AVG(team1_TOVp) AS TOVp,
  AVG(team1_ORBp) AS ORBp,
  AVG(team1_FTr) AS FTr,
    AVG(team2_eFGp) AS opp_eFGp,
  AVG(team2_TOVp) AS opp_TOVp,
  AVG(team2_ORBp) AS opp_ORBp,
  AVG(team2_FTr) AS opp_FTr,
  SUM(team1Win)/COUNT(*) AS Wp
FROM 
  `ncaambb-443717.march_madness.games_ff`
GROUP BY
  Season, team1
ORDER BY Season,team1
