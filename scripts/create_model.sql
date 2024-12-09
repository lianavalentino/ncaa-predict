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
-- AND eFGp IS NOT NULL AND opp_eFGp IS NOT NULL# between in SQL is inclusive of end points
