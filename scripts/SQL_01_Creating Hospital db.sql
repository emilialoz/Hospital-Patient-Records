--CREATE DATABASE HospitalM;

-- Create Payers table
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Payers' AND xtype='U')
BEGIN 
CREATE TABLE Payers (
    Id CHAR(36) PRIMARY KEY,
    NAME VARCHAR(100),
    ADDRESS VARCHAR(255),
    CITY VARCHAR(100),
    STATE_HEADQUARTERED CHAR(2),
    ZIP VARCHAR(10),
    PHONE VARCHAR(20)
    )
END
ELSE
BEGIN
PRINT 'Table [Payers] already exists'
END;

-- Create Patients table
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Patients' AND xtype='U')
BEGIN 
CREATE TABLE Patients (
    Id CHAR(36) PRIMARY KEY,
    BIRTHDATE DATE,
    DEATHDATE DATE,
    PREFIX VARCHAR(10),
    FIRST VARCHAR(100),
    LAST VARCHAR(100),
    SUFFIX VARCHAR(10),
    MAIDEN VARCHAR(100),
    MARITAL CHAR(1),
    RACE VARCHAR(50),
    ETHNICITY VARCHAR(50),
    GENDER CHAR(1),
    BIRTHPLACE VARCHAR(255),
    ADDRESS VARCHAR(255),
    CITY VARCHAR(100),
    STATE VARCHAR(100),
    COUNTY VARCHAR(100),
    ZIP VARCHAR(10),
    LAT VARCHAR(255),
    LON VARCHAR(255)
    )
END
ELSE
BEGIN
PRINT 'Table [Patients] already exists'
END;

-- Create Procedures table
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Procedures' AND xtype='U')
BEGIN 
CREATE TABLE Procedures (
    START datetime,
    STOP datetime,
    PATIENT CHAR(36),
    ENCOUNTER CHAR(36),
    CODE VARCHAR(20),
    DESCRIPTION VARCHAR(255),
    BASE_COST INT,
    REASONCODE VARCHAR(20),
    REASONDESCRIPTION VARCHAR(255)
);
END
ELSE
BEGIN
PRINT 'Table [Procedures] already exists'
END


-- Create Encounters table
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Encounters' AND xtype='U')
BEGIN 
CREATE TABLE Encounters (
    EncounterID VARCHAR(max),
    PatientID CHAR(36) NOT NULL,
    ProviderID CHAR(36) NOT NULL,
    EncounterDate DATETIME2 NOT NULL,
    DischargeDate DATETIME2 NULL,
    EncounterType VARCHAR(50),
    DiagnosisCode VARCHAR(10),
    ProcedureCode VARCHAR(10),
    PayerID CHAR(36),
    TotalCost DECIMAL(12,2),
    Status VARCHAR(20),
    Notes VARCHAR(MAX)
);
END
ELSE
BEGIN
PRINT 'Table [Encounters] already exists'
END

-- Create _hospitallogs table
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='_hospitallogs' AND xtype='U')
BEGIN 
CREATE TABLE _hospitallogs (
    [Date] TIMESTAMP,
    EventType VARCHAR(50) NOT NULL,
    EventResult VARCHAR(50) NOT NULL,
    Notes VARCHAR(MAX)
);
END
ELSE
BEGIN
PRINT 'Table [_hospitallogs] already exists'
END


