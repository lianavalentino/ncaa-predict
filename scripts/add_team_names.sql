# prompt: Join these data sources

WITH games AS (
  SELECT
  teams.TeamName AS WTeam,
  reg_season.Season,
  reg_season.DayNum,
  reg_season.WTeamID,
  reg_season.WScore,
  reg_season.LTeamID,
  reg_season.LScore,
  reg_season.WLoc,
  reg_season.NumOT,
  reg_season.WFGM,
  reg_season.WFGA,
  reg_season.WFGM3,
  reg_season.WFGA3,
  reg_season.WFTM,
  reg_season.WFTA,
  reg_season.WOR,
  reg_season.WDR,
  reg_season.WAst,
  reg_season.WTO,
  reg_season.WStl,
  reg_season.WBlk,
  reg_season.WPF,
  reg_season.LFGM,
  reg_season.LFGA,
  reg_season.LFGM3,
  reg_season.LFGA3,
  reg_season.LFTM,
  reg_season.LFTA,
  reg_season.LOR,
  reg_season.LDR,
  reg_season.LAst,
  reg_season.LTO,
  reg_season.LStl,
  reg_season.LBlk,
  reg_season.LPF
FROM
  `ncaambb-443717.march_madness.reg_season` AS reg_season
LEFT JOIN
  `ncaambb-443717.march_madness.teams` AS teams
ON
  teams.TeamID = reg_season.WTeamID)
SELECT
  games.Season,
  games.DayNum,
  games.WTeamID,
  games.WTeam,
  games.WScore,
  games.LTeamID,
  teams.TeamName AS LTeam,
  games.LScore,
  games.WLoc,
  games.NumOT,
  games.WFGM,
  games.WFGA,
  games.WFGM3,
  games.WFGA3,
  games.WFTM,
  games.WFTA,
  games.WOR,
  games.WDR,
  games.WAst,
  games.WTO,
  games.WStl,
  games.WBlk,
  games.WPF,
  games.LFGM,
  games.LFGA,
  games.LFGM3,
  games.LFGA3,
  games.LFTM,
  games.LFTA,
  games.LOR,
  games.LDR,
  games.LAst,
  games.LTO,
  games.LStl,
  games.LBlk,
  games.LPF
FROM
  games
LEFT JOIN
  `ncaambb-443717.march_madness.teams` AS teams
ON
  teams.TeamID = games.LTeamID
