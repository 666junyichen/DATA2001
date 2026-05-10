# Spatial Resource Accessibility Analysis

## Overview / 项目概览

| English | 中文 |
| --- | --- |
| This project builds a spatial data analysis workflow to estimate how well different Greater Sydney SA2 areas are served by selected public, commercial, transport, and social resources. | 本项目构建了一个空间数据分析流程，用于评估 Greater Sydney 不同 SA2 区域在公共设施、商业服务、交通资源和社会资源方面的覆盖程度。 |
| The workflow integrates tabular and geospatial open datasets, loads them into PostgreSQL/PostGIS, calculates standardized resource indicators, and visualizes the final score through static and interactive maps. | 项目整合表格数据与地理空间开放数据，导入 PostgreSQL/PostGIS，计算标准化资源指标，并通过静态地图和交互式地图展示综合评分结果。 |

## Project Scope / 项目范围

| English | 中文 |
| --- | --- |
| Region: Greater Sydney SA2 statistical areas. | 分析区域：Greater Sydney 的 SA2 统计区域。 |
| Data model: PostgreSQL tables and PostGIS geometries for points and multipolygons. | 数据模型：使用 PostgreSQL 表和 PostGIS 点/多面几何对象。 |
| Core indicators: retail businesses, healthcare businesses, public transport stops, polling places, and school catchments. | 核心指标：零售商业、医疗健康商业、公共交通站点、投票地点和学校学区。 |
| Extended indicators: public toilets, domestic assault hotspot areas, and non-employing construction businesses. | 扩展指标：公共厕所、家庭暴力热点区域和非雇佣型建筑业企业。 |
| Output: weighted spatial score, correlation check with median income, and an interactive Folium map. | 输出结果：空间综合评分、与收入中位数的相关性检查，以及 Folium 交互式地图。 |

## Method Summary / 方法摘要

| English | 中文 |
| --- | --- |
| Cleaned and transformed CSV, TXT, JSON, and shapefile inputs using pandas, GeoPandas, Shapely, and SQLAlchemy. | 使用 pandas、GeoPandas、Shapely 和 SQLAlchemy 清洗并转换 CSV、TXT、JSON 与 shapefile 数据。 |
| Converted latitude/longitude and polygon geometry into PostGIS-compatible `POINT` and `MULTIPOLYGON` columns. | 将经纬度和多边形数据转换为 PostGIS 可处理的 `POINT` 与 `MULTIPOLYGON` 几何列。 |
| Built SQL views for per-area indicators, normalized indicators using z-scores, and combined them with a sigmoid function. | 为各区域指标建立 SQL 视图，使用 z-score 标准化，并通过 sigmoid 函数组合成综合评分。 |
| Used spatial joins such as `ST_Contains` and `ST_Overlaps` to connect facilities and hotspot polygons to SA2 areas. | 使用 `ST_Contains` 和 `ST_Overlaps` 等空间连接方法，将设施点和热点多边形关联到 SA2 区域。 |

## Key Results / 关键结果

| English | 中文 |
| --- | --- |
| Integrated 10 source datasets into a spatial analysis workflow. | 将 10 个来源数据集整合进空间分析流程。 |
| Designed 8 resource-related indicators across base and extended scoring models. | 设计了 8 个资源相关指标，覆盖基础评分模型和扩展评分模型。 |
| Created 10 database tables and 27 SQL views for cleaning, scoring, and model assembly. | 创建了 10 张数据库表和 27 个 SQL 视图，用于清洗、评分和模型组合。 |
| Added spatial and attribute indexes to support repeated PostGIS joins and scoring queries. | 添加空间索引和属性索引，支持重复执行 PostGIS 空间连接与评分查询。 |
| The extended well-resourced score showed a positive correlation with median income (`r = 0.504201`). | 扩展后的资源充足度评分与收入中位数呈正相关（`r = 0.504201`）。 |

## Repository Contents / 仓库内容

| Path | English | 中文 |
| --- | --- | --- |
| `FINAL.ipynb` | Main notebook for data cleaning, database loading, scoring, extension indicators, correlation checks, and interactive mapping. | 主 notebook，包含数据清洗、数据库导入、评分、扩展指标、相关性检查和交互式地图。 |
| `V14_pandas.ipynb` | pandas/GeoPandas implementation draft for the scoring workflow. | 使用 pandas/GeoPandas 实现评分流程的草稿版本。 |
| `V15_toSQL.ipynb` | SQL-oriented implementation draft using PostgreSQL/PostGIS views. | 使用 PostgreSQL/PostGIS 视图实现评分流程的 SQL 版本草稿。 |
| `interactive_resource_accessibility_map.html` | Exported interactive map generated from the final spatial score. | 基于最终空间评分导出的交互式地图。 |
| `FINAL.pdf` | Rendered project output. | 渲染后的项目输出。 |
| `docs/` | Public documentation for methodology, contribution summary, metrics, and publishing notes. | 公开文档，包含方法、贡献总结、成果指标和发布建议。 |

## Tools / 使用工具

| English | 中文 |
| --- | --- |
| Python, pandas, GeoPandas, Shapely, SQLAlchemy, PostgreSQL, PostGIS, Folium, Matplotlib, Seaborn, Jupyter Notebook. | Python、pandas、GeoPandas、Shapely、SQLAlchemy、PostgreSQL、PostGIS、Folium、Matplotlib、Seaborn、Jupyter Notebook。 |

## Privacy Note / 隐私说明

| English | 中文 |
| --- | --- |
| This public version describes project methods and outputs without personal identifiers, institutional identifiers, database credentials, or private dataset files. | 此公开版本只描述项目方法与结果，不包含个人身份信息、机构身份信息、数据库凭据或私有数据文件。 |
