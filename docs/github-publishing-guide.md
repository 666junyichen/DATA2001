# GitHub Publishing Guide

## Recommended Repository Name

Recommended:

```text
spatial-resource-accessibility-analysis
```

Why this works:

- It describes the project outcome rather than the original context.
- It is readable on GitHub and suitable for a resume project link.
- It highlights the strongest technical theme: spatial analytics and resource accessibility.

Other acceptable options:

```text
greater-sydney-resource-accessibility
postgis-spatial-accessibility-score
urban-resource-accessibility-mapping
```

Avoid names that expose private or context-specific identifiers.

## Files Suitable For Public GitHub

Suitable to keep:

- `README.md`
- `项目说明.md`
- `docs/`
- `FINAL.ipynb`
- `V14_pandas.ipynb`
- `V15_toSQL.ipynb`
- `interactive_resource_accessibility_map.html`
- `FINAL.pdf`

Review before publishing:

- The Word report artifact in the repository root: its filename and content may contain context-specific wording. Convert useful content into docs instead of relying on the raw document.
- `FINAL.pdf`: review visually before publishing because PDF exports can preserve old headers or notebook output.
- Notebook outputs: check for database usernames, hostnames, file paths, or private identifiers.
- HTML map: check whether popups contain only area names/codes and scores.

Do not publish:

- `Credentials.json`
- Database passwords or host details
- Personal identifiers
- Institution identifiers
- Student identifiers
- Raw data files with restricted licences
- Filenames that expose course codes, group IDs, or other context-specific identifiers
- Report exports that contain course codes or group labels

## Suggested Public Repo Structure

```text
.
├── README.md
├── 项目说明.md
├── FINAL.ipynb
├── V14_pandas.ipynb
├── V15_toSQL.ipynb
├── interactive_resource_accessibility_map.html
├── FINAL.pdf
├── REPORT.pdf
├── docs/
│   ├── README.md
│   ├── methodology.md
│   ├── contribution-summary.md
│   ├── metrics-check.md
│   └── github-publishing-guide.md
├── notebooks/
│   └── README.md
├── reports/
│   └── README.md
└── visualizations/
    └── README.md
```

## Suggested GitHub Description

```text
PostGIS and GeoPandas workflow for scoring and mapping spatial resource accessibility across Greater Sydney SA2 regions.
```

## Suggested Topics

```text
postgis
geopandas
spatial-analysis
urban-analytics
folium
postgresql
data-visualization
geospatial
```
