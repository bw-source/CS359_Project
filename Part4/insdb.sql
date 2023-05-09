/*******************************************************************************
   CS359 Project Part 2
   File: insbq.sql

   Notes:
   Measurement units is inches
   Date format is ISO 8601
********************************************************************************/
/*******************************************************************************
   Populate Tables
********************************************************************************/

/*******************************************************************************
    Populate Video Table
        videoCode: integer
        videoLength: integer
********************************************************************************/

INSERT INTO [Video] ([videoCode], [videoLength]) VALUES (567,92);
INSERT INTO [Video] ([videoCode], [videoLength]) VALUES (823,34);
INSERT INTO [Video] ([videoCode], [videoLength]) VALUES (231,134);
INSERT INTO [Video] ([videoCode], [videoLength]) VALUES (356,21);
INSERT INTO [Video] ([videoCode], [videoLength]) VALUES (321,14);

/***************************
    Populate Model Table
        modelNo: char(10)
        width: numeric (6,2)
        height: numeric (6,2)
        weight: numeric (6,2)
        depth: numeric (6,2)
        screenSize: numeric (6,2))  
********************************************************************************/

INSERT INTO [MODEL] ([modelNo], [width], [height], [weight], [depth], [screenSize]) VALUES ('ABC4K32', 27.90, 15.70, 20.50, 2.84, 32.00);
INSERT INTO [MODEL] ([modelNo], [width], [height], [weight], [depth], [screenSize]) VALUES ('ABC4K40', 34.69, 17.43, 24.30, 3.35, 40.00);
INSERT INTO [MODEL] ([modelNo], [width], [height], [weight], [depth], [screenSize]) VALUES ('ABC4K50', 44.20, 25.60, 29.30, 3.50, 50.00);
INSERT INTO [MODEL] ([modelNo], [width], [height], [weight], [depth], [screenSize]) VALUES ('ABC4K55', 48.80, 28.40, 39.20, 3.89, 55.00);
INSERT INTO [MODEL] ([modelNo], [width], [height], [weight], [depth], [screenSize]) VALUES ('ABC4K60', 53.27, 32.18, 48.23, 4.21, 60.00);

/*******************************************************************************
    Populate Site Table
       siteCode: integer
       type: varchar (16)
       address: varchar(100)
       phone: varchar(16)) 
********************************************************************************/

INSERT INTO [Site] ([siteCode], [type], [address], [phone]) VALUES (23, 'Bar', '34 N 56th St, Phoenix, AZ 85013', '480-555-9623');
INSERT INTO [Site] ([siteCode], [type], [address], [phone]) VALUES (14, 'Restaurant', '12543 N Victory Blvd, Van Nuys, CA 91404', '818-555-0945');
INSERT INTO [Site] ([siteCode], [type], [address], [phone]) VALUES (65, 'Restaurant', '6523 E. Katella Blvd, Anaheim, CA 92805', '714-555-5423');
INSERT INTO [Site] ([siteCode], [type], [address], [phone]) VALUES (46, 'Bar', '876 MacArthur Dr, Tempe, AZ 85284', '480-555-2765');
INSERT INTO [Site] ([siteCode], [type], [address], [phone]) VALUES (54, 'Bar', '2876 Sahara Blvd, Las Vegas, NV 89127', '702-555-8723' );


/*******************************************************************************
    Populate DigitalDisplay Table
        serialNo: char(10)
        schedulerSystem: char(10)
        modelNo: char(10))  
        Foreign key: modelNo references Model (modelNo) 
********************************************************************************/

INSERT INTO [DigitalDisplay] ([serialNo], [schedulerSystem], [modelNo]) VALUES ('1467367200', 'Smart', 'ABC4K32');
INSERT INTO [DigitalDisplay] ([serialNo], [schedulerSystem], [modelNo]) VALUES ('5265360807', 'Random', 'ABC4K50');
INSERT INTO [DigitalDisplay] ([serialNo], [schedulerSystem], [modelNo]) VALUES ('6083450383', 'Smart', 'ABC4K60');
INSERT INTO [DigitalDisplay] ([serialNo], [schedulerSystem], [modelNo]) VALUES ('9154677989', 'Virtue','ABC4K40');
INSERT INTO [DigitalDisplay] ([serialNo], [schedulerSystem], [modelNo]) VALUES ('1696599316', 'Random', 'ABC4K55');


/*******************************************************************************
    Populate Client Table 
        clientId: integer
        name: varchar (40)
        phone: varchar (16)
        address: varchar (100)
********************************************************************************/

INSERT INTO [Client] ([clientId], [name], [phone], [address]) VALUES (56, 'Roberto Martinez', '480-555-0978', '2765 W Mesa Blvd, Tempe, AZ 85284');
INSERT INTO [Client] ([clientId], [name], [phone], [address]) VALUES (51, 'Colby Butler', '505-555-4321', '654 Ocean Dr, Ventura, CA 93003');
INSERT INTO [Client] ([clientId], [name], [phone], [address]) VALUES (21, 'Morton Bush', '702-555-1543', '10231 Desert Vista Blvd 89128');
INSERT INTO [Client] ([clientId], [name], [phone], [address]) VALUES (12, 'Laura Hunnisett', '909-555-2765', '1532 Jackrabbit Ln, 92502');
INSERT INTO [Client] ([clientId], [name], [phone], [address]) VALUES (65, 'Randell Simonson', '480-555-2134', '654 Cactus Flower Dr, 85283');


/*******************************************************************************
    Populate TechnicalSupport Table
        empId: integer
        name: varchar (40)
        gender: char (1)
********************************************************************************/

INSERT INTO [TechnicalSupport] ([empId], [name], [gender]) VALUES (76, 'Allison Wright', 'F');
INSERT INTO [TechnicalSupport] ([empId], [name], [gender]) VALUES (22, 'Louise Joiner', 'F');
INSERT INTO [TechnicalSupport] ([empId], [name], [gender]) VALUES (89, 'Charnette San Nicolás', 'F');
INSERT INTO [TechnicalSupport] ([empId], [name], [gender]) VALUES (26, 'Arlo White', 'M');
INSERT INTO [TechnicalSupport] ([empId], [name], [gender]) VALUES (78, 'Ivan Alberto', 'M');



/*******************************************************************************
    Populate Administrator Table
        empId: integer 
        name: varchar (40)
        gender: char (1)
********************************************************************************/

INSERT INTO [Administrator] ([empId], [name], [gender]) VALUES (7, 'Irene Candelaria', 'F');
INSERT INTO [Administrator] ([empId], [name], [gender]) VALUES (43, 'Jannette Carter', 'F');
INSERT INTO [Administrator] ([empId], [name], [gender]) VALUES (11, 'Kailey Trueman', 'F');
INSERT INTO [Administrator] ([empId], [name], [gender]) VALUES (64, 'Cash Heath', 'M');
INSERT INTO [Administrator] ([empId], [name], [gender]) VALUES (24, 'Kaden Iñíguez', 'M');

/*******************************************************************************
    Populate Salesman Table
        empId: integer
        name: varchar (40)
        gender: char (1)
********************************************************************************/

INSERT INTO [Salesman] ([empId], [name], [gender]) VALUES (25, 'Frank Castenello', 'M');
INSERT INTO [Salesman] ([empId], [name], [gender]) VALUES (26, 'Merton Toledano', 'M');
INSERT INTO [Salesman] ([empId], [name], [gender]) VALUES (98, 'Tooru Ybarra', 'M');
INSERT INTO [Salesman] ([empId], [name], [gender]) VALUES (12, 'Lester Gutierrez', 'M');
INSERT INTO [Salesman] ([empId], [name], [gender]) VALUES (87, 'Ulyssa Yoshida', 'F');

/*******************************************************************************
    Populate AirtimePackage Table
        packageId: integer
        class: varchar (16)
        startDate: date 
        lastDate: date
        frequency: integer
        videoCode: integer
********************************************************************************/

INSERT INTO [AirtimePackage] ([packageId], [class], [startDate], [lastDate], [frequency], [videoCode]) VALUES ('3', 'Golden Hours', '2023-01-01', '2025-12-31', 60, 321);
INSERT INTO [AirtimePackage] ([packageId], [class], [startDate], [lastDate], [frequency], [videoCode]) VALUES ('1', 'Whole Day', '2022-04-15', '2025-1-1', 120, 823);
INSERT INTO [AirtimePackage] ([packageId], [class], [startDate], [lastDate], [frequency], [videoCode]) VALUES ('2', 'Golden Hours', '2022-12-01', '2025-11-31', 60, 567);
INSERT INTO [AirtimePackage] ([packageId], [class], [startDate], [lastDate], [frequency], [videoCode]) VALUES ('4', 'Economy', '2020-01-01', '2026-12-31', 180, 356);
INSERT INTO [AirtimePackage] ([packageId], [class], [startDate], [lastDate], [frequency], [videoCode]) VALUES ('5', 'Whole Day', '2021-01-01', '2024-12-31', 120, 231);

/*******************************************************************************
    Populate AdmWorkHours Table
        empId: integer
        day: date
        hours: numeric (4,2)  
        Foreign key: empId references Administrator (empId)  
********************************************************************************/

INSERT INTO [AdmWorkHours] ([empId], [day], [hours]) VALUES (7, '2023-02-14', 8.75);
INSERT INTO [AdmWorkHours] ([empId], [day], [hours]) VALUES (26, '2022-12-23', 9.75);
INSERT INTO [AdmWorkHours] ([empId], [day], [hours]) VALUES (87, '2023-12-12', 7.00);
INSERT INTO [AdmWorkHours] ([empId], [day], [hours]) VALUES (43, '2022-11-23', 10.25);
INSERT INTO [AdmWorkHours] ([empId], [day], [hours]) VALUES (11, '2023-03-01', 8.25);

/*******************************************************************************
    Populate Broadcasts Table
        videoCode: integer
        siteCode: integer  
        Foreign key: videoCode references Video (videoCode)  
        Foreign key: siteCode references Site (siteCode)  
********************************************************************************/

INSERT INTO [Broadcasts] ([videoCode], [siteCode]) VALUES (823, 23);
INSERT INTO [Broadcasts] ([videoCode], [siteCode]) VALUES (321, 14);
INSERT INTO [Broadcasts] ([videoCode], [siteCode]) VALUES (356, 65);
INSERT INTO [Broadcasts] ([videoCode], [siteCode]) VALUES (567, 54);
INSERT INTO [Broadcasts] ([videoCode], [siteCode]) VALUES (231, 46);


/*******************************************************************************
    Populate Administers Table
        empId: integer
        siteCode: integer
        Foreign key: empId references Administrator (empId)  
        Foreign key: siteCode references Site (siteCode) 
********************************************************************************/

INSERT INTO [Administers] ([empId], [siteCode]) VALUES (7, 23);
INSERT INTO [Administers] ([empId], [siteCode]) VALUES (64, 54);
INSERT INTO [Administers] ([empId], [siteCode]) VALUES (24, 14);
INSERT INTO [Administers] ([empId], [siteCode]) VALUES (43, 65);
INSERT INTO [Administers] ([empId], [siteCode]) VALUES (11, 46);


/*******************************************************************************
    Populate Specializes Table
        empId: integer
        modelNo: char(10)
        Foreign key: empId references TechnicalSupport (empId)  
        Foreign key: modelNo references Model (modelNo)  
********************************************************************************/

INSERT INTO [Specializes] ([empId], [modelNo]) VALUES (76, 'ABC4K32');
INSERT INTO [Specializes] ([empId], [modelNo]) VALUES (22, 'ABC4K32');
INSERT INTO [Specializes] ([empId], [modelNo]) VALUES (78, 'ABC4K50');
INSERT INTO [Specializes] ([empId], [modelNo]) VALUES (89, 'ABC4K55');
INSERT INTO [Specializes] ([empId], [modelNo]) VALUES (26, 'ABC4K50');

/*******************************************************************************
    Populate Purchases Table
        clientId: integer
        empId: integer
        packageId: integer 
        commissionRate: numeric (4,2)
        Foreign key: clientId references Client (clientId)  
********************************************************************************/

INSERT INTO [Purchases] ([clientId], [empId], [packageId], [commissionRate]) VALUES (56, 25, 1, 6.25);
INSERT INTO [Purchases] ([clientId], [empId], [packageId], [commissionRate]) VALUES (51, 25, 4, 7);
INSERT INTO [Purchases] ([clientId], [empId], [packageId], [commissionRate]) VALUES (12, 87, 3, 5.75);
INSERT INTO [Purchases] ([clientId], [empId], [packageId], [commissionRate]) VALUES (65, 12, 1, 3.5);
INSERT INTO [Purchases] ([clientId], [empId], [packageId], [commissionRate]) VALUES (21, 98, 2, 10.5);


/*******************************************************************************
    Populate Locates Table
        serialNo: char (10)
        siteCode: integer
        Foreign key: serialNo references DigitalDisplay (serialNo)  
        Foreign key: siteCode references Site (siteCode)  
********************************************************************************/

INSERT INTO [Locates] ([serialNo], [siteCode]) VALUES ('1467367200', 23);
INSERT INTO [Locates] ([serialNo], [siteCode]) VALUES ('5265360807', 54);
INSERT INTO [Locates] ([serialNo], [siteCode]) VALUES ('1696599316', 65);
INSERT INTO [Locates] ([serialNo], [siteCode]) VALUES ('6083450383', 46);
INSERT INTO [Locates] ([serialNo], [siteCode]) VALUES ('9154677989', 14);