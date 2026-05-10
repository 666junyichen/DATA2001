# Methodology

## Objective

The project estimates resource accessibility across Greater Sydney SA2 areas by combining demographic, business, transport, public facility, education, and risk-related spatial indicators.

## Data Pipeline

1. Load CSV, TXT, JSON, and shapefile inputs with pandas and GeoPandas.
2. Clean missing values and standardize numeric columns.
3. Convert coordinate columns and polygon geometries into PostGIS-compatible geometry fields.
4. Load cleaned datasets into PostgreSQL/PostGIS tables.
5. Build SQL views for each indicator and for the final composite score.
6. Visualize output through static maps and an exported Folium interactive map.

## Database Design

The workflow creates separate tables for:

- Income
- Population
- Businesses
- Polling places
- Transport stops
- School catchments
- SA2 boundaries
- Public toilets
- Crime hotspots
- Business employment size

Spatial fields use SRID 4326. Point datasets are stored as `POINT`; boundary and hotspot datasets are stored as `MULTIPOLYGON`.

## Spatial Operations

- `ST_Contains` links point facilities such as stops, polling places, and public toilets to SA2 regions.
- `ST_Overlaps` links polygon-based school catchments and hotspot areas to SA2 regions.
- GIST indexes support repeated geometry-based joins.
- Attribute indexes support joins on SA2 codes.

## Scoring Model

The base model uses five indicators:

- Retail businesses per 1,000 people
- Healthcare and social assistance businesses per 1,000 people
- Public transport stops per square kilometre
- Polling locations per square kilometre
- School catchment coverage relative to young population

The extended model adds three indicators:

- Public toilets per square kilometre
- Domestic assault hotspot area per square kilometre as a negative indicator
- Non-employing construction businesses per 1,000 people as a negative indicator

Each indicator is converted into a z-score. The composite score is calculated with a sigmoid function so the final score is represented between 0 and 1.

## Validation And Interpretation

The final notebook checks the relationship between the extended well-resourced score and median income. The observed correlation is `0.504201`, suggesting a moderate positive association between the modelled resource score and income level.

The analysis also notes important limitations:

- Some low-population regions are excluded from score calculation to avoid unstable per-capita rates.
- Some hotspot data represents only a specific crime category, so it should not be interpreted as total crime exposure.
- School catchment polygons may overlap or duplicate across school types.
- A broader resource model would need additional indicators and independent validation.
