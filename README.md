# Hospital-Patient-Records
Analysis of Massachusetts General Hospital patients' information

## Summary

Analysis refers to 1000 patients of Massachusetts General Hospital from 2011-2022, including data on patient demographics, insurance coverage, and medical encounters & procedures.

## Scope

### Data Layer
- **SQL**
  - Database querying
  - Data extraction and transformation
  - Schema design and optimization

### Visualization Layer
- **Power BI**
  - Power Query (ETL processes)
  - M language (custom transformations)
  - Data modeling (relationships, measures, calculated columns)
  - Interactive dashboards and reports

## Purpose of Analysis

The purpose of this analysis is to build a KPI dashboard that enables hospital executives to track key operational metrics and address essential strategic questions, such as patient flow, resource utilization, and financial performance.

## Backend

 1. SQL:
	 -[ database creation query](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/scripts/SQL_01_Creating%20Hospital%20db.sql),
		 - 
| Table | Description/csv file|
| ----------- | ----------- |
| Encounters | [encounters.csv](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/data/encounters.csv) |
| Patients | [patients.csv](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/data/patients.csv) |
| Payers | [payers.csv](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/data/payers.csv) |
| Procedure | [procedures.csv](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/data/procedures.csv) |
| _hospitallogs | stores logs related to scheduled jobs and other database operations. It supports monitoring, error handling, and auditing of system activities |
