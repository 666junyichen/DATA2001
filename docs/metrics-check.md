# Metrics Check

This file records project metrics that are supported by the current notebooks and report artifacts.

## Supported Metrics

| Metric | Value | Evidence |
| --- | ---: | --- |
| Source datasets integrated | 10 | Income, population, polling places, businesses, stops, catchments, SA2 boundaries, public toilets, crime hotspots, employment-size businesses |
| Database tables designed | 10 | `CREATE TABLE` statements in `FINAL.ipynb` |
| SQL views designed | 27 | `CREATE VIEW` statements in `FINAL.ipynb` |
| Base indicators | 5 | Retail, healthcare, stops, polling places, schools |
| Extended indicators | 3 | Public toilets, crime hotspot area, non-employing construction businesses |
| Total indicators in extended model | 8 | Base indicators plus extended indicators |
| Polling rows removed for missing location fields | 140 | Cleaning note in notebook |
| Final score and median income correlation | `0.504201` | Correlation output in `FINAL.ipynb` |
| Crime score and median income correlation | `0.215537` | Report artifact text |
| Public toilet score and median income correlation | `0.039932` | Report artifact text |
| Retail score and median income correlation | `0.007101` | Report artifact text |
| Healthcare score and median income correlation | `-0.014701` | Report artifact text |
| Polling score and median income correlation | `-0.007786` | Report artifact text |

## Strong Achievement Numbers

- 10 datasets integrated
- 8 indicators engineered
- 10 database tables designed
- 27 SQL views created
- 1 exported interactive map
- `0.504201` final score correlation with median income

## Notes

- These metrics describe the project workflow and model artifacts, not private personal information.
- The database connection in the notebook references a credential file name, but no actual credential values should be committed.
- If raw data files are added later, check licensing and privacy constraints before publishing them.
