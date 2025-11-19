
# Hospital-Patient-Records
🏥 Analysis of Massachusetts General Hospital patients' information.

## Summary

Analysis refers to 1000 patients of Massachusetts General Hospital from 2011-2022, including data on patient demographics, insurance coverage, and medical encounters & procedures.

## Scope

### 🗄️ Data Layer
- **SQL Server and SSMS**
  - Database querying
  - Data extraction and transformation
  - Schema design and optimization
 - **🐍 Python scripting**


### 📊 Visualization Layer
- **Power BI**
  - Power Query (ETL processes)
  - M language (custom transformations)
  - Data modeling (relationships, measures, calculated columns)
  - Interactive dashboards and reports

## Purpose of Analysis

The purpose of this analysis is to build a KPI dashboard that enables hospital executives to track key operational metrics and address essential strategic questions, such as patient flow, resource utilization, and financial performance.

## ⚙️ Backend

 1. 🗄️ **SQL :**
	 -[ database creation query](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/scripts/SQL_01_Creating%20Hospital%20db.sql)
		 
| Table | Description/csv file|
| ----------- | ----------- |
| Encounters | [encounters.csv](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/data/encounters.csv) |
| Patients | [patients.csv](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/data/patients.csv) |
| Payers | [payers.csv](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/data/payers.csv) |
| Procedure | [procedures.csv](https://github.com/emilialoz/Hospital-Patient-Records/blob/main/data/procedures.csv) |
| _hospitallogs | stores logs related to scheduled jobs and other database operations. It supports monitoring, error handling, and auditing of system activities |

🔑 **Primary keys and foreign keys** <br>
<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>Table</th>
      <th>Primary key</th>
      <th>Foreign key</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Patients</td>
      <td><code>ID</code></td>
      <td>—</td>
    </tr>
    <tr>
      <td>Encounters</td>
      <td><code>EncounterID</code></td>
      <td>
        <code>PatientID</code> → Patients(ID)<br>
        <code>PayerID</code> → Payers(ID)
      </td>
    </tr>
    <tr>
      <td>Procedures</td>
      <td>—</td>
      <td>
        <code>PATIENT</code> → Patients(ID)<br>
        <code>ENCOUNTER</code> → Encounters(EncounterID)
      </td>
    </tr>
    <tr>
      <td>Payers</td>
      <td><code>ID</code></td>
      <td>—</td>
    </tr>
  </tbody>
</table>

<br>
- 🐍 <b>Python scripting</b> to load data to SQL tables <br>
<br>
<table>
  <tr>
    <th colspan="3"><b>Justification for Python Scripting Selection</b></th>
  </tr>
  <tr>
    <td colspan="3" style="text-align:left">Alternative approaches were considered but ultimately rejected based on practical limitations</td>
  </tr>
  <tr>
    <td colspan ="1" style="text-align:left">:red_circle: Insert Query</td>
    <td colspan="2" style="text-align:left">Rejected due to the large volume of data and the significant amount of manual work required.  
    This approach was deemed inefficient and error-prone for production-scale scenarios.</td>
  </tr>
 <tr>
    <td colspan ="1" style="text-align:left">:red_circle: Import/Export Wizard (SSMS)</td>
    <td colspan="2" style="text-align:left">Rejected due to frequent inconsistencies in data types between CSV files and the declared column types in target tables.  
  These mismatches resulted in recurring import errors and unreliable data loading.  
  Observations are based on prior experience with commercial projects.</td>
  </tr>
  <tr>
    <td colspan ="1" style="text-align:left; background-color: #D6EEEE">✅ Selected Tool: Python Scripting (SSMS)</td>
    <td colspan= "2" style="text-align:left; background-color: #D6EEEE">Solution ensures reliable, automated handling of large datasets, minimizes manual intervention, and provides robust error control compared to the alternatives.</td>
  </tr>
</table>





