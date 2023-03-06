create table Video(
    videoCode   int,
    videoLength int,
    PRIMARY KEY(videoCode)
);

create table Model(
    modelNo char(10),
    width       numeric(6,2),
    height      numeric(6,2),
    weight      numeric (6,2),
    depth       numeric(6,2),
    screenSize  numeric(6,2),
    PRIMARY KEY(modelNo)
);

create table Site(
    siteCode    int, 
    type        varchar(16),
    address     varchar(100),
    phone       varchar(16),
    PRIMARY KEY(siteCode)
);

create table DigitalDisplay(
    serialNo        char(10),
    schedulerSystem char(10),
    modelNo         char(10),
    FOREIGN KEY(modelNo) REFERENCES Model(modelNo),
    PRIMARY KEY(serialNo)
);

create table Client(
    clientId    int,
    name        varchar(40),
    phone       varchar(16),
    address     varchar(100),
    PRIMARY KEY(clientId)
);

create table TechnicalSupport(
    empId   int,
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
    packageId   int,
    class       varchar(16),
    startDate   date,
    lastDate    date,
    frequency   int,
    videoCode   int,
    PRIMARY KEY(packageId)
);

create table AdmWorkHours(
    empId   int,
    day     date,
    hours   numeric(4,2),
    FOREIGN KEY(empId) REFERENCES Administrator(empId),
    PRIMARY KEY(empId, day)
);

create table Broadcasts(
        videoCode   int,
        siteCode    int,
        FOREIGN KEY(videoCode)  REFERENCES Video(videoCode),
        FOREIGN KEY(siteCode)   REFERENCES Site(siteCode),
        PRIMARY KEY(videoCode, siteCode)
);

create table Administers(
    empId       int,
    siteCode    int,
    FOREIGN KEY(empId)      REFERENCES Administrator(empId),
    FOREIGN KEY(siteCode)   REFERENCES Site(siteCode),
    PRIMARY KEY(empId, siteCode)
);

create table Specializes(
    empId   int,
    modelNo char(10),
    FOREIGN KEY(empId)      REFERENCES TechnicalSupport(empId),
    FOREIGN KEY(modelNo)    REFERENCES Model(modelNo),
    PRIMARY KEY(empId, modelNo)
);

create table Purchases(
    clientId    int,
    empId       int,
    packageId   int,
    commissionRate   numeric(4,2),
    FOREIGN KEY(clientId)   REFERENCES Client(clientId),
    FOREIGN KEY(empId)      REFERENCES Salesman(empId),
    FOREIGN KEY(packageId)  REFERENCES AirtimePackage(packageId),
    PRIMARY KEY(clientId, empId, packageId)
);

create table Locates(
    serialNo    char(10),
    siteCode    int,
    FOREIGN KEY(serialNo)   REFERENCES DigitalDisplay(serialNo),
    FOREIGN KEY(siteCode)   REFERENCES Site(siteCode),
    PRIMARY KEY(serialNo, siteCode)
);