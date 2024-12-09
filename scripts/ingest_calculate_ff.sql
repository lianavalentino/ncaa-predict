CREATE OR REPLACE TABLE `march_madness.games_ff` AS
  (
SELECT 
  -- Original fields
  Season,
  DayNum,
  team1ID,
  team1,
  team1Score,
  team2ID,
  team2,
  team2Score,
  team1Loc,
  NumOT,
  
  -- Team1 stats
  team1FGM,
  team1FGA,
  team1FGM3,
  team1FGA3,
  team1FTM,
  team1FTA,
  team1OR,
  team1DR,
  team1Ast,
  team1TO,
  team1Stl,
  team1Blk,
  team1PF,
  
  -- Team2 stats
  team2FGM,
  team2FGA,
  team2FGM3,
  team2FGA3,
  team2FTM,
  team2FTA,
  team2OR,
  team2DR,
  team2Ast,
  team2TO,
  team2Stl,
  team2Blk,
  team2PF,

  -- Calculated fields for team1
  SAFE_DIVIDE(team1FGM + 0.5 * team1FGM3, team1FGA) AS team1_eFGp,
  SAFE_DIVIDE(team1TO, team1FGA + 0.44 * team1FTA + team1TO) AS team1_TOVp,
  SAFE_DIVIDE(team1OR, team1OR + team2DR) AS team1_ORBp,
  SAFE_DIVIDE(team1FTM, team1FGA) AS team1_FTr,

  -- Calculated fields for team2
  SAFE_DIVIDE(team2FGM + 0.5 * team2FGM3, team2FGA) AS team2_eFGp,
  SAFE_DIVIDE(team2TO, team2FGA + 0.44 * team2FTA + team2TO) AS team2_TOVp,
  SAFE_DIVIDE(team2OR, team2OR + team1DR) AS team2_ORBp,
  SAFE_DIVIDE(team2FTM, team2FGA) AS team2_FTr,
  CASE WHEN team1Score > team2score THEN 1 ELSE 0 END AS team1Win

FROM (
  SELECT 
    Season,
    DayNum,
    WTeamID AS team1ID,
    WTeam AS team1,
    WScore AS team1Score,
    LTeamID AS team2ID,
    LTeam AS team2,
    LScore AS team2Score,
    WLoc AS team1Loc,
    NumOT,
    WFGM AS team1FGM,
    WFGA AS team1FGA,
    WFGM3 AS team1FGM3,
    WFGA3 AS team1FGA3,
    WFTM AS team1FTM,
    WFTA AS team1FTA,
    WOR AS team1OR,
    WDR AS team1DR,
    WAst AS team1Ast,
    WTO AS team1TO,
    WStl AS team1Stl,
    WBlk AS team1Blk,
    WPF AS team1PF,
    LFGM AS team2FGM,
    LFGA AS team2FGA,
    LFGM3 AS team2FGM3,
    LFGA3 AS team2FGA3,
    LFTM AS team2FTM,
    LFTA AS team2FTA,
    LOR AS team2OR,
    LDR AS team2DR,
    LAst AS team2Ast,
    LTO AS team2TO,
    LStl AS team2Stl,
    LBlk AS team2Blk,
    LPF AS team2PF
  FROM `ncaambb-443717.march_madness.box_score`

  UNION ALL

  SELECT 
    Season,
    DayNum,
    LTeamID AS team1ID,
    LTeam AS team1,
    LScore AS team1Score,
    WTeamID AS team2ID,
    WTeam AS team2,
    WScore AS team2Score,
    CASE 
      WHEN WLoc = 'H' THEN 'A'
      WHEN WLoc = 'A' THEN 'H'
      ELSE WLoc
    END AS team1Loc,
    NumOT,
    LFGM AS team1FGM,
    LFGA AS team1FGA,
    LFGM3 AS team1FGM3,
    LFGA3 AS team1FGA3,
    LFTM AS team1FTM,
    LFTA AS team1FTA,
    LOR AS team1OR,
    LDR AS team1DR,
    LAst AS team1Ast,
    LTO AS team1TO,
    LStl AS team1Stl,
    LBlk AS team1Blk,
    LPF AS team1PF,
    WFGM AS team2FGM,
    WFGA AS team2FGA,
    WFGM3 AS team2FGM3,
    WFGA3 AS team2FGA3,
    WFTM AS team2FTM,
    WFTA AS team2FTA,
    WOR AS team2OR,
    WDR AS team2DR,
    WAst AS team2Ast,
    WTO AS team2TO,
    WStl AS team2Stl,
    WBlk AS team2Blk,
    WPF AS team2PF
  FROM `ncaambb-443717.march_madness.games_ff`
)
  )
