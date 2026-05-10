# Contribution Summary

## Role

Data analysis and spatial database modelling contributor.

## Main Contributions

- Cleaned and transformed multi-format data inputs, including CSV, TXT, JSON, and shapefile sources.
- Standardized demographic, business, facility, transport, education, and risk datasets into a shared SA2-level spatial analysis structure.
- Built PostGIS tables for point and multipolygon geometries, including SRID handling and geometry conversion.
- Implemented spatial joins using `ST_Contains` and `ST_Overlaps`.
- Designed SQL view chains for indicator calculation, z-score normalization, and composite score assembly.
- Extended the base resource model with additional public facility, risk, and economic-structure indicators.
- Produced static and interactive map outputs to communicate the spatial distribution of resource accessibility.
- Checked model behavior by correlating the final score with median income.

## Achievement Bullets

- Built a PostgreSQL/PostGIS spatial analytics pipeline integrating 10 demographic, business, transport, public facility, education, and risk datasets for SA2-level resource accessibility analysis.
- Designed 8 standardized accessibility indicators and combined them into a sigmoid-based composite score to compare resource coverage across Greater Sydney regions.
- Created 10 database tables, 27 SQL views, and spatial/attribute indexes to support repeatable geospatial joins, normalization, and scoring.
- Developed static and interactive geospatial visualizations with GeoPandas and Folium, including an exported choropleth map for final score exploration.
- Validated the extended scoring model against median income and identified a moderate positive correlation (`r = 0.504201`).

## Discussion Points

- Why per-capita and per-area normalization were needed before comparing regions.
- Why z-score normalization was used before combining indicators with different units.
- Why sigmoid was used to convert the final weighted sum into a bounded score.
- How `ST_Contains` differs from `ST_Overlaps` and why each was used for different geometry types.
- How spatial indexes improve repeated PostGIS join performance.
- What limitations remain in the model and what data would improve it.
