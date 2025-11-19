CREATE TABLE Dict_EncounterType (
	EncounterType_ID UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
	EncounterType_desc nvarchar(100)
);

INSERT INTO Dict_EncounterType (EncounterType_desc)
SELECT distinct [EncounterType]
  FROM [HospitalM].[dbo].[Encounters]

Select *
 from Dict_EncounterType

UPDATE e
SET [EncounterType] = EncounterType_ID
from [dbo].[Encounters] e
left join Dict_EncounterType de
ON e.EncounterType = de.EncounterType_desc