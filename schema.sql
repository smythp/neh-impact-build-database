CREATE TABLE grants (
       id INTEGER PRIMARY KEY,
       ApplicantType VARCHAR,
       Institution VARCHAR,
       OrganizationType VARCHAR,
       InstCity VARCHAR,
       InstState VARCHAR,
       InstPostalCode VARCHAR,
       InstCountry VARCHAR,
       CouncilDate INT,
       YearAwarded VARCHAR,
       ProjectTitle VARCHAR,
       Program VARCHAR,
       Division VARCHAR,
       ApprovedOutright REAL,
       ApprovedMatching REAL,
       AwardOutright REAL,
       AwardMatching REAL,
       OriginalAmount REAL,
       BeginGrant VARCHAR,
       EndGrant VARCHAR,
       ProjectDesc VARCHAR,
       ToSupport VARCHAR,
       PrimaryDiscipline VARCHAR,
       SupplementCount INT,
       ParticipantCount INT,
       DisciplineCount INT,
       ShortPostal INT,
       division_reclassification VARCHAR);

