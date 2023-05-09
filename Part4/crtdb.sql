create table Video(
    videoCode   int NOT NULL,
    videoLength int
    PRIMARY KEY(videoCode)
);
create table Model(
    modelNO varchar(10) NOT NULL,
    width       numeric(6,2),
    height      numeric(6,2),
    weight      numeric (6,2),
    depth       numeric(6,2),
    screenSize  numeric(6,2),
    PRIMARY KEY(modelNo)
);
create table Site( 
    siteCode    int NOT NULL, 
    type        varchar(16), 
    address     varchar(100),
    phone       varchar(16),
    CONSTRAINT site_type CHECK (type = 'bar'or type ='restaurant')
    PRIMARY KEY(siteCode)
);
create table DigitalDisplay(
    serialNo        char(10) NOT NULL,
    schedulerSystem char(10),
    modelNo         char(10),
    CONSTRAINT ss CHECK (schedulerSystem = 'Random'or schedulerSystem ='Smart' or schedulerSystem ='Virtue')
    PRIMARY KEY(serialNo),
    FOREIGN KEY(modelNo) REFERENCES Model(modelNo)
);
create table Client(
    clientId    int NOT NULL,
    name        varchar(40),
    phone       varchar(16),
    address     varchar(100),
    PRIMARY KEY(clientId)
);
create table TechnicalSupport(
    empId   int NOT NULL,
    name    varchar(40),
    gender  char(1),
    PRIMARY KEY(empId)
);
create table Administrator(
    empId   int,
    name    varchar(40),
    gender  char(1),
    PRIMARY KEY(empId)
);
create table Salesman(
    empId   int,
    name    varchar(40),
    gender  char(1),
    PRIMARY KEY(empId)
);
create table AirtimePackage(
    packageId   int NOT NULL,
    class       varchar(16),
    startDate   date,
    lastDate    date,
    frequency   int,
    videoCode   int,
    CONSTRAINT at_class CHECK (class ='economy'or class='whole day' or class ='golden hours')
    PRIMARY KEY(packageId)
);
create table AdmWorkHours(
    empID   int NOT NULL,
    day     date NOT NULL,
    hours   numeric(4,2),
    PRIMARY KEY(empI,day),
    FOREIGN KEY(empId) REFERENCES Administrator(empId)
);  
create table Broadcasts(
        videoCode   int NOT NULL,
        siteCode    int NOT NULL,
        PRIMARY KEY(videoCode,siteCode),
        FOREIGN KEY(videoCode)  REFERENCES Video(videoCode),
        FOREIGN KEY(siteCode)   REFERENCES Site(siteCode)
);
create table Administraters(
    empId       int NOT NULL, 
    siteCode    int NOT NULL,
    PRIMARY KEY(empId,siteCode),
    FOREIGN KEY(empId)      REFERENCES Administrator(empId),
    FOREIGN KEY(siteCode)   REFERENCES Site(siteCode)
);
create table Speacializes(
    empId   int NOT NULL,
    modelNo char NOT NULL,
    PRIMARY KEY(empId,modelNo),
    FOREIGN KEY(empId)      REFERENCES TechnicalSupport(empId),
    FOREIGN KEY(modelNo)    REFERENCES Model(modelNo)
);
create table Purchases(
    clientId    int NOT NULL,
    empId       int NOT NULL,
    packageId   int NOT NULL,
    commisionRate   numeric(4,2),
    CONSTRAINT Pur_trans PRIMARY KEY(clientId,empId,packageId),
    FOREIGN KEY(empId)      REFERENCES Salesman(empId),
    FOREIGN KEY(packageId)  REFERENCES AirtimePackage(packageId)
);
create table Locates(
    serialNo    char(10) NOT NULL,
    siteCode    int NOT NULL,
    CONSTRAINT Loc PRIMARY KEY(serialNo,siteCode),
    FOREIGN KEY(serialNo)   REFERENCES DigitalDisplay(serialNo),
    FOREIGN KEY(siteCode)   REFERENCES Site(siteCode)
);
