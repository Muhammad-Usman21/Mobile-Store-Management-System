


CREATE DATABASE DB_PROJECT

USE DB_PROJECT

DROP DATABASE DB_PROJECT




-------------------------------------------------------------------------------------------------------------------------------







CREATE TABLE Customers (

	--CustomerID int IDENTITY(1,1),
	CustomerID int NOT NULL,
	FirstName varchar(30) NOT NULL,
	LastName varchar(30) NOT NULL,
	CNIC varchar(20) NOT NULL,
	Email varchar(100) NOT NULL,
	PhoneNumber varchar(20),
	Street varchar(50),
	City varchar(30),
	Province varchar(30),
	PostalCode int,
	Gender char NOT NULL,
	DateOfBirth date NOT NULL,

	CONSTRAINT PKc_CustomerID PRIMARY KEY (CustomerID),
	CONSTRAINT UQc_CNIC UNIQUE (CNIC),
	CONSTRAINT UQc_Email UNIQUE (Email),
	CONSTRAINT UQc_PhoneNumber UNIQUE (PhoneNumber),

	CONSTRAINT CHKc_FullName CHECK (
		FirstName NOT LIKE '%[^A-Za-z]%' AND
		LastName  NOT LIKE '%[^A-Za-z]%'
	),

	CONSTRAINT CHKc_CNIC CHECK (
		LEN( CNIC ) = 15 AND 
		CNIC LIKE '[0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[1-2]'
	),

	CONSTRAINT CHKc_Email CHECK (
		Email LIKE '%_@_%._%'
	),

	CONSTRAINT CHKc_PhoneNumber CHECK (
		PhoneNumber is NULL OR
		PhoneNumber LIKE '+92 [0-9][0-9][0-9] [0-9][0-9][0-9][0-9][0-9][0-9][0-9]'  OR
		PhoneNumber LIKE '[0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9][0-9][0-9][0-9]' 
	),

	CONSTRAINT CHKc_PostalCode CHECK (
		PostalCode = CAST( PostalCode AS int )  AND 
		PostalCode >= 0 
	),

	CONSTRAINT CHKc_Gender CHECK ( 
		Gender = 'M' OR Gender = 'F'
	),

	CONSTRAINT CHKc_DateOfBirth CHECK ( 
		--ISDATE( DateOfBirth ) = 1  AND
		DateOfBirth <= DATEADD( YEAR, -18, GETDATE() ) AND
		DateOfBirth >= DATEADD( YEAR, -80, GETDATE() )  
	),

);


SELECT * FROM Customers
TRUNCATE TABLE Customers
DELETE FROM Customers
DROP TABLE Customers






-------------------------------------------------------------------------------------------------------------------------





CREATE TABLE EmployeePosition (
	
	PositionID int IDENTITY(1,1),
	Position varchar(50) NOT NULL,
	Salary money NOT NULL,

	CONSTRAINT PKep_PositionID PRIMARY KEY (PositionID),

	CONSTRAINT CHKep_Salary CHECK (
		Salary = CAST( Salary AS money )  AND 
		Salary >= 0 
	),

	CONSTRAINT CHKep_Position CHECK (
		Position NOT LIKE '%[^A-Za-z ]%'
	)

);


SELECT * FROM EmployeePosition
TRUNCATE TABLE EmployeePosition
DELETE FROM EmployeePosition
DROP TABLE EmployeePosition






CREATE PROCEDURE InsertionInEmplyeePosition
    @Position varchar(50), @Salary MONEY
AS
BEGIN
    SET NOCOUNT ON;
	INSERT INTO EmployeePosition ( Position, Salary ) 
	VALUES ( @Position, @Salary )
END

DROP PROCEDURE InsertionInEmplyeePosition



-- EXEC PROCEDURE InsertionInEmplyeePosition




------------------------------------------------------------------------------------------------------------------------









CREATE TABLE Employees (

	EmployeeID int IDENTITY(1,1),
	FirstName varchar(30) NOT NULL,
	LastName varchar(30) NOT NULL,
	CNIC varchar(20) NOT NULL, 
	Email varchar(100) NOT NULL,
	PhoneNumber varchar(20) NOT NULL,
	Street varchar(30) NOT NULL,
	City varchar(30) NOT NULL,
	Province varchar(30) NOT NULL,
	PostalCode int NOT NULL,
	Gender char NOT NULL,
	DateOfBirth date NOT NULL,
	HireDate date NOT NULL,
	RetireDate date,
	PositionID int,

	CONSTRAINT PKe_EmployeeID PRIMARY KEY (EmployeeID),
	CONSTRAINT UQe_CNIC UNIQUE (CNIC),
	CONSTRAINT UQe_Email UNIQUE (Email),
	CONSTRAINT UQe_PhoneNumber UNIQUE (PhoneNumber),
	CONSTRAINT FKe_PositionID FOREIGN KEY (PositionID) REFERENCES EmployeePosition (PositionID) ON DELETE CASCADE,

	CONSTRAINT CHKe_FullName CHECK (
		FirstName NOT LIKE '%[^A-Za-z]%' AND
		LastName  NOT LIKE '%[^A-Za-z]%'
	),

	CONSTRAINT CHKe_CNIC CHECK (
		LEN( CNIC ) = 15 AND 
		CNIC LIKE '[0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[1-2]'
	),

	CONSTRAINT CHKe_Email CHECK (
		Email LIKE '%_@_%._%'
	),

	CONSTRAINT CHKe_PhoneNumber CHECK (
		PhoneNumber is NULL OR
		PhoneNumber LIKE '+92 [0-9][0-9][0-9] [0-9][0-9][0-9][0-9][0-9][0-9][0-9]'  OR
		PhoneNumber LIKE '[0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9][0-9][0-9][0-9]' 
	),

	CONSTRAINT CHKe_PostalCode CHECK (
		PostalCode = CAST( PostalCode AS int )  AND 
		PostalCode >= 0 
	),

	CONSTRAINT CHKe_Gender CHECK ( 
		Gender = 'M' OR Gender = 'F'
	),

	CONSTRAINT CHKe_DateOfBirth CHECK ( 
		--ISDATE( CONVERT(date, DateOfBirth) ) = 1  AND
		DateOfBirth <= DATEADD( YEAR, -20, GETDATE() ) AND
		DateOfBirth >= DATEADD( YEAR, -60, GETDATE() )  
	),

	CONSTRAINT CHKe_HireDate CHECK (
		--ISDATE( CONVERT(date, HireDate) ) = 1 AND
		HireDate >= DATEADD( YEAR, 20, DateOfBirth ) AND
		HireDate <= GETDATE()
	),

	CONSTRAINT CHKe_RetireDate CHECK (
		RetireDate IS NULL OR 
		( --ISDATE( CONVERT(date, RetireDate) ) = 1  AND
		  RetireDate >= DATEADD( DAY, 1, HireDate )  AND
		  RetireDate <= GETDATE() 
		)
	),		

	CONSTRAINT CHKe_PositionID CHECK (
		( RetireDate IS NOT NULL AND 
		  PositionID IS NULL 
		) OR 
		( RetireDate IS NULL  AND 
		  PositionID IS NOT NULL  AND
		  dbo.IsValidPositionIDForEmployees(PositionID) = 1
		)
	),

);


SELECT * FROM Employees
TRUNCATE TABLE Employees
DELETE FROM Employees
DROP TABLE Employees



CREATE FUNCTION dbo.IsValidPositionIDForEmployees( @PositionID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @PositionID IN ( SELECT PositionID FROM EmployeePosition )
        SET @IsValid = 1;

    RETURN @IsValid;
END;
GO

DROP FUNCTION dbo.IsValidPositionIDForEmployees





-----------------------------------------------------------------------------------------------------------------------------










CREATE TABLE Orders (
	
	OrderID int IDENTITY(1,1),
	CustomerID int NOT NULL,
	EmployeeID int NOT NULL,
	OrderDate date NOT NULL,
	--TotalAmount money NOT NULL,
	PaymentMethod varchar(20),

	CONSTRAINT PKo_OrderID PRIMARY KEY (OrderID),
	CONSTRAINT FKo_CustomerID FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID) ON DELETE CASCADE,
	CONSTRAINT FKo_EmployeeID FOREIGN KEY (EmployeeID) REFERENCES Employees (EmployeeID) ON DELETE CASCADE,

	CONSTRAINT CHKo_CustomerID CHECK (
		dbo.IsValidCustomerIDForOrders(CustomerID) = 1
	),

	CONSTRAINT CHKo_EmployeeID CHECK (
		dbo.IsValidEmployeeIDForOrders(EmployeeID) = 1
	),

	CONSTRAINT CHKo_OrderDate CHECK (
		--ISDATE( OrderDate ) = 1  AND 
		OrderDate <= GETDATE()  AND
		dbo.IsValidOrderDateForOrders(OrderDate, EmployeeID) = 1
	),
	
	CONSTRAINT CHKo_PaymentMethod CHECK (
		PaymentMethod NOT LIKE '%[^A-Za-z ]%'
	),
);


SELECT * FROM Orders
TRUNCATE TABLE Orders
DELETE FROM Orders
DROP TABLE Orders




CREATE FUNCTION dbo.IsValidCustomerIDForOrders( @CustomerID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @CustomerID IN ( SELECT CustomerID FROM Customers )
        SET @IsValid = 1;

    RETURN @IsValid;

END;
GO

DROP FUNCTION dbo.IsValidCustomerIDForOrders




CREATE FUNCTION dbo.IsValidEmployeeIDForOrders( @EmployeeID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @EmployeeID IN ( SELECT EmployeeID FROM Employees )
        SET @IsValid = 1;

    RETURN @IsValid;

END;
GO

DROP FUNCTION dbo.IsValidEmployeeIDForOrders




CREATE FUNCTION dbo.IsValidOrderDateForOrders( @OrderDate DATE, @EmployeeID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	DECLARE @HireDate DATE = ( SELECT HireDate FROM Employees AS e WHERE e.EmployeeID = @EmployeeID );
	DECLARE @RetireDate DATE = ( SELECT RetireDate FROM Employees AS e WHERE e.EmployeeID = @EmployeeID );

	IF ( @OrderDate >= @HireDate  AND  @RetireDate IS NOT NULL  AND  @OrderDate <= @RetireDate ) OR
	   ( @OrderDate >= @HireDate  AND  @RetireDate IS NULL )
        SET @IsValid = 1;

/*
	IF ( @OrderDate >= ( SELECT HireDate FROM Employees AS e WHERE e.EmployeeID = @EmployeeID )    AND
	   ( SELECT RetireDate FROM Employees AS e WHERE e.EmployeeID = @EmployeeID ) IS NOT NULL    AND
	   @OrderDate <= ( SELECT RetireDate FROM Employees AS e WHERE e.EmployeeID = @EmployeeID ) )         
	   OR
	   ( @OrderDate >= ( SELECT HireDate FROM Employees AS e WHERE e.EmployeeID = @EmployeeID )    AND
	   ( SELECT RetireDate FROM Employees AS e WHERE e.EmployeeID = @EmployeeID ) IS NULL  )

        SET @IsValid = 1;
*/

    RETURN @IsValid;

END;
GO

DROP FUNCTION dbo.IsValidOrderDateForOrders







----------------------------------------------------------------------------------------------------------------------







CREATE TABLE Products (
	
	ProductID int IDENTITY(1,1),
	Brand varchar(30) NOT NULL,
	ModelNumber varchar(50) NOT NULL,
	UnitPrice money NOT NULL,
	StockQuantity int NOT NULL,
	OS varchar(20),
	Storage varchar(20),
	RAM varchar(20),
	Battery varchar(20),
	Camera varchar(20),
	Display varchar(20),
	Processor varchar(20),
	Warranty varchar(20),
	Descriptionn varchar(100),
	

	CONSTRAINT PKp_ProductID PRIMARY KEY (ProductID),

	CONSTRAINT CHKp_UnitPrice CHECK (
		UnitPrice = CAST( UnitPrice AS money )  AND 
		UnitPrice >= 0 
	),

	CONSTRAINT CHKp_StockQuantity CHECK (
		StockQuantity = CAST( StockQuantity AS int ) AND
		StockQuantity >= 0
	),

);


SELECT * FROM Products
TRUNCATE TABLE Products
DELETE FROM Products
DROP TABLE Products






-----------------------------------------------------------------------------------------------------------------













CREATE TABLE Suppliers (

	SupplierID int IDENTITY(1,1),
	FirstName varchar(30) NOT NULL,
	LastName varchar(30) NOT NULL,
	CNIC varchar(20) NOT NULL,
	Email varchar(50) NOT NULL,
	PhoneNumber varchar(20) NOT NULL,
	Street varchar(50) NOT NULL,
	City varchar(50) NOT NULL,
	Province varchar(50) NOT NULL,
	Country varchar(50) NOT NULL,
	PostalCode int NOT NULL,
	Gender char NOT NULL,
	DateOfBirth date NOT NULL,

	CONSTRAINT PKs_SupplierID PRIMARY KEY (SupplierID),
	CONSTRAINT UQs_CNIC UNIQUE (CNIC),
	CONSTRAINT UQs_Email UNIQUE (Email),
	CONSTRAINT UQs_PhoneNumber UNIQUE (PhoneNumber),

	CONSTRAINT CHKs_FullName CHECK (
		FirstName NOT LIKE '%[^A-Za-z]%' AND
		LastName  NOT LIKE '%[^A-Za-z]%'
	),

	CONSTRAINT CHKs_CNIC CHECK (
		LEN( CNIC ) = 15 AND 
		CNIC LIKE '[0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[1-2]'
	),

	CONSTRAINT CHKs_Email CHECK (
		Email LIKE '%_@_%._%'
	),

	CONSTRAINT CHKs_PhoneNumber CHECK (
		PhoneNumber is NULL OR
		PhoneNumber LIKE '+[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
	),

	CONSTRAINT CHKs_PostalCode CHECK (
		PostalCode = CAST( PostalCode AS int )  AND 
		PostalCode >= 0 
	),

	CONSTRAINT CHKs_Gender CHECK ( 
		Gender = 'M' OR Gender = 'F'
	),

	CONSTRAINT CHKs_DateOfBirth CHECK ( 
		--ISDATE( DateOfBirth ) = 1  AND
		DateOfBirth <= DATEADD( YEAR, -20, GETDATE() ) AND
		DateOfBirth >= DATEADD( YEAR, -50, GETDATE() )  
	),

);


SELECT * FROM Suppliers
TRUNCATE TABLE Suppliers
DELETE FROM Suppliers
DROP TABLE Suppliers





---------------------------------------------------------------------------------------------------------------------









CREATE TABLE Shipments (
	
	ShipmentID int IDENTITY(1,1),
	SupplierID int NOT NULL,
	ShipmentDate date NOT NULL,
	ShippingMethod varchar(50) NOT NULL,
	Statuss varchar(20) NOT NULL,
	ArrivalDate date,

	CONSTRAINT PKs_ShipmentID PRIMARY KEY (ShipmentID),
	CONSTRAINT FKs_SupplierID FOREIGN KEY (SupplierID) REFERENCES Suppliers (SupplierID) ON DELETE CASCADE,

	CONSTRAINT CHKs_SupplierID CHECK (
		dbo.IsValidSupplierIDForShipments(SupplierID) = 1
	),

	CONSTRAINT CHKs_ShipmentDate CHECK (
		ShipmentDate <= GETDATE()
	),

	CONSTRAINT CHKs_ArrivalDate CHECK (
		ArrivalDate >= ShipmentDate AND
		ArrivalDate <= DATEADD( DAY, 28, ShipmentDate )
	),

);


SELECT * FROM Shipments
TRUNCATE TABLE Shipments
DELETE FROM Shipments
DROP TABLE Shipments





CREATE FUNCTION dbo.IsValidSupplierIDForShipments( @SupplierID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @SupplierID IN ( SELECT SupplierID FROM Suppliers )
        SET @IsValid = 1;

    RETURN @IsValid;
END;
GO

DROP FUNCTION dbo.IsValidSupplierIDForShipments











-------------------------------------------------------------------------------------------------------------------









CREATE TABLE ShipmentDetails (
	
	ShipmentDetailID int IDENTITY(1,1),
	ShipmentID int NOT NULL,
	ProductID int NOT NULL,
	QuantityReceived int NOT NULL,
	CostPerUnit money NOT NULL,

	CONSTRAINT PK_ShipmentDetailID PRIMARY KEY (ShipmentDetailID),
	CONSTRAINT FK_ShipmentID FOREIGN KEY (ShipmentID) REFERENCES Shipments (ShipmentID) ON DELETE CASCADE,
	CONSTRAINT FK_ProductID FOREIGN KEY (ProductID) REFERENCES Products (ProductID) ON DELETE CASCADE,

	CONSTRAINT CHKsd_ProductID CHECK (
		dbo.IsValidProductIDForShipmentDetails(ProductID) = 1
	),

	CONSTRAINT CHKsd_ShipmentID CHECK (
		dbo.IsValidShipmentIDForShipmentDetails(ShipmentID) = 1
	),

	CONSTRAINT CHKsd_QuantityReceived CHECK (
		QuantityReceived = CAST( QuantityReceived AS int )  AND 
		QuantityReceived > 0 
	),

	CONSTRAINT CHKsd_CostPerUnit CHECK (
		CostPerUnit = CAST( CostPerUnit AS money )  AND 
		CostPerUnit >= 0 
	),
);


SELECT * FROM ShipmentDetails
TRUNCATE TABLE ShipmentDetails
DELETE FROM ShipmentDetails
DROP TABLE ShipmentDetails





CREATE FUNCTION dbo.IsValidShipmentIDForShipmentDetails( @ShipmentID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @ShipmentID IN ( SELECT ShipmentID FROM Shipments )
        SET @IsValid = 1;

    RETURN @IsValid;
END;
GO

DROP FUNCTION dbo.IsValidShipmentIDForShipmentDetails




CREATE FUNCTION dbo.IsValidProductIDForShipmentDetails( @ProductID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @ProductID IN ( SELECT ProductID FROM Products )
        SET @IsValid = 1;

    RETURN @IsValid;
END;
GO

DROP FUNCTION dbo.IsValidProductIDForShipmentDetails












----------------------------------------------------------------------------------------------------------------------







CREATE TABLE OrderDetails (
	
	OrderDetailID int IDENTITY(1,1),
	OrderID int NOT NULL,
	ProductID int NOT NULL,
	Quantity int NOT NULL,
	UnitPrice money NOT NULL,
	Discount int NOT NULL,
	--TotalPrice money NOT NULL,

	CONSTRAINT PKod_OrderDetailID PRIMARY KEY (OrderDetailID),
	CONSTRAINT FKod_OrderID FOREIGN KEY (OrderID) REFERENCES Orders (OrderID) ON DELETE CASCADE,
	CONSTRAINT FKod_ProductID FOREIGN KEY (ProductID) REFERENCES Products (ProductID) ON DELETE CASCADE,

	CONSTRAINT CHKod_ProductID CHECK (
		dbo.IsValidProductIDForOrderDetails(ProductID) = 1
	),

	CONSTRAINT CHKod_OrderID CHECK (
		dbo.IsValidOrderIDForOrderDetails(OrderID) = 1
	),

	CONSTRAINT CHKod_Quantity CHECK (
		-- dbo.IsValidQuantityForOrderDetails(Quantity, ProductID, OrderID) = 1  AND
		Quantity = CAST( Quantity AS int )  AND 
		Quantity > 0
	),

	CONSTRAINT CHKod_UnitPrice CHECK (
		UnitPrice = CAST( UnitPrice AS money )  AND 
		UnitPrice >= 0 
	),

	CONSTRAINT CHKod_Discount CHECK (
		Discount = CAST( Discount AS int )  AND 
		Discount >= 0 
	),
);



SELECT * FROM OrderDetails
TRUNCATE TABLE OrderDetails
DELETE FROM OrderDetails
DROP TABLE OrderDetails






CREATE FUNCTION dbo.IsValidProductIDForOrderDetails( @ProductID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @ProductID IN ( SELECT ProductID FROM Products )
        SET @IsValid = 1;

    RETURN @IsValid;
END;
GO

DROP FUNCTION dbo.IsValidProductIDForOrderDetails





CREATE FUNCTION dbo.IsValidOrderIDForOrderDetails( @OrderID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @OrderID IN ( SELECT OrderID FROM Orders )
        SET @IsValid = 1;

    RETURN @IsValid;
END;
GO

DROP FUNCTION dbo.IsValidOrderIDForOrderDetails





CREATE FUNCTION dbo.IsValidQuantityForOrderDetails( @Quantity INT, @ProductID INT, @OrderID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	DECLARE @StockQuantity INT = ( SELECT StockQuantity FROM Products AS p WHERE p.ProductID = @ProductID  );

	IF @Quantity <= @StockQuantity
        SET @IsValid = 1;

	--IF @Quantity > @StockQuantity
	--BEGIN
		--EXEC DeleteAnOrder @OrderIDToDelete = @OrderID
	--END

    RETURN @IsValid;
END;
GO


DROP FUNCTION dbo.IsValidQuantityForOrderDetails





/*

CREATE PROCEDURE DeleteAnOrder
    @OrderIDToDelete INT
AS
BEGIN
    SET NOCOUNT ON;
    DELETE FROM Orders WHERE OrderID = @OrderIDToDelete
END


DROP PROCEDURE DeleteAnOrder

*/






------------------------------------------------------------------------------------------------------------------------




CREATE TABLE RepairServices (
	
	RepairID int IDENTITY(1,1),
	-- RepairID int NOT NULL,
	ServiceName varchar(50) NOT NULL,
	Descriptionn varchar(250) NOT NULL,
	Cost money NOT NULL,

	CONSTRAINT PKrs_RepairID PRIMARY KEY (RepairID),

	CONSTRAINT CHKrs_Cost CHECK (
		Cost = CAST( Cost AS money )  AND 
		Cost >= 0 
	),
);



SELECT * FROM RepairServices
TRUNCATE TABLE RepairServices
DELETE FROM RepairServices
DROP TABLE RepairServices



CREATE PROCEDURE InsertionInRepairServices
    @ServiceName VARCHAR(50), @Descriptionn VARCHAR(250), @Cost MONEY
AS
BEGIN
    SET NOCOUNT ON;
	INSERT INTO RepairServices( ServiceName, Descriptionn, Cost ) 
	VALUES ( @ServiceName, @Descriptionn, @Cost )
END

DROP PROCEDURE InsertionInRepairServices



--EXEC PROCEDURE InsertionInRepairServices





------------------------------------------------------------------------------------------------------------





CREATE TABLE OrderRepairs (

	OrderRepairID int IDENTITY(1,1),
	-- OrderRepairID int NOT NULL,
	OrderID int NOT NULL,
	RepairID int NOT NULL,
	-- Quantity int NOT NULL, 
	Notes varchar(100),
	
	CONSTRAINT PKor_OrderRepairID PRIMARY KEY (OrderRepairID),
	CONSTRAINT PKor_OrderID FOREIGN KEY (OrderID) REFERENCES Orders (OrderID) ON DELETE CASCADE, 
	CONSTRAINT PKor_RepairID FOREIGN KEY (RepairID) REFERENCES RepairServices (RepairID) ON DELETE CASCADE, 
/*
	CONSTRAINT CHKor_Quantity CHECK (
		Quantity = CAST( Quantity AS int )  AND 
		Quantity > 0
	),
*/
	CONSTRAINT CHKor_OrderID CHECK (
		dbo.IsValidOrderIDForOrderRepairs(OrderID) = 1
	),

	CONSTRAINT CHKor_RepairID CHECK (
		dbo.IsValidRepairIDForOrderRepairs(RepairID) = 1
	),

);




SELECT * FROM OrderRepairs
TRUNCATE TABLE OrderRepairs
DELETE FROM OrderRepairs
DROP TABLE OrderRepairs



CREATE FUNCTION dbo.IsValidRepairIDForOrderRepairs( @RepairID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @RepairID IN ( SELECT RepairID FROM RepairServices )
        SET @IsValid = 1;

    RETURN @IsValid;
END;
GO

DROP FUNCTION dbo.IsValidRepairIDForOrderRepairs





CREATE FUNCTION dbo.IsValidOrderIDForOrderRepairs( @OrderID INT )
RETURNS BIT
AS
BEGIN
    DECLARE @IsValid BIT = 0;

	IF @OrderID IN ( SELECT OrderID FROM Orders )
        SET @IsValid = 1;

    RETURN @IsValid;
END;
GO

DROP FUNCTION dbo.IsValidOrderIDForOrderRepairs








-------------------------------------------------------------------------------------------------------------------








SELECT
	O.OrderID,
	O.OrderDate,
	O.PaymentMethod,
	C.CustomerID,
	C.FirstName AS CustomerFirstName,
	C.LastName AS CustomerLastName,
	C.CNIC AS CustomerCNIC,
	C.Email AS CustomerEmail,
	C.PhoneNumber AS CustomerPhoneNumber,
	C.Street AS CustomerStreet,
	C.City AS CustomerCity,
	C.Province AS CustomerProvince,
	C.PostalCode AS CustomerPostalCode,
	C.Gender AS CustomerGender,
	C.DateOfBirth AS CustomerDateOfBirth,
	E.EmployeeID,
	E.FirstName AS EmployeeFirstName,
	E.LastName AS EmployeeLastName,
	E.CNIC AS EmployeeCNIC,
	E.Email AS EmployeeEmail,
	E.PhoneNumber AS EmployeePhoneNumber,
	E.Street AS EmployeeStreet,
	E.City AS EmployeeCity,
	E.Province AS EmployeeProvince,
	E.PostalCode AS EmployeePostalCode,
	E.Gender AS EmployeeGender,
	E.DateOfBirth AS EmployeeDateOfBirth,
	E.HireDate AS EmployeeHireDate,
	E.RetireDate AS EmployeeRetireDate,
	EP.PositionID,
	EP.Position AS EmployeePosition,
	EP.Salary AS EmployeeSalary
FROM
	Orders O
	INNER JOIN Customers C ON O.CustomerID = C.CustomerID
	INNER JOIN Employees E ON O.EmployeeID = E.EmployeeID
	LEFT JOIN EmployeePosition EP ON E.PositionID = EP.PositionID






CREATE TABLE Orders_Denormalized (

	--OrderID int IDENTITY(1,1),
	OrderID int NOT NULL,
	--CustomerID int NOT NULL,
	--EmployeeID int NOT NULL,
	OrderDate date NOT NULL,
	--TotalAmount money NOT NULL,
	PaymentMethod varchar(20),

	--CustomerID int IDENTITY(1,1),
	CustomerID int NOT NULL,
	CustomerFirstName varchar(30) NOT NULL,
	CustomerLastName varchar(30) NOT NULL,
	CustomerCNIC varchar(20) NOT NULL,
	CustomerEmail varchar(100) NOT NULL,
	CustomerPhoneNumber varchar(20),
	CustomerStreet varchar(50),
	CustomerCity varchar(30),
	CustomerProvince varchar(30),
	CustomerPostalCode int,
	CustomerGender char NOT NULL,
	CustomerDateOfBirth date NOT NULL,

	--EmployeeID int IDENTITY(1,1),
	EmployeeID int NOT NULL,
	EmployeeFirstName varchar(30) NOT NULL,
	EmployeeLastName varchar(30) NOT NULL,
	EmployeeCNIC varchar(20) NOT NULL, 
	EmployeeEmail varchar(100) NOT NULL,
	EmployeePhoneNumber varchar(20) NOT NULL,
	EmployeeStreet varchar(30) NOT NULL,
	EmployeeCity varchar(30) NOT NULL,
	EmployeeProvince varchar(30) NOT NULL,
	EmployeePostalCode int NOT NULL,
	EmployeeGender char NOT NULL,
	EmployeeDateOfBirth date NOT NULL,
	EmployeeHireDate date NOT NULL,
	EmployeeRetireDate date,
	--EmployeePositionID int,


	--PositionID int IDENTITY(1,1),
	PositionID int ,
	EmployeePosition varchar(50),
	EmployeeSalary money,


	CONSTRAINT PKodn_OrderID PRIMARY KEY (OrderID),

);



SELECT * FROM Orders_Denormalized
TRUNCATE TABLE Orders_Denormalized
DELETE FROM Orders_Denormalized
DROP TABLE Orders_Denormalized









-----------------------------------------------------------------------------------------------------------------------






CREATE TRIGGER trg_AddStockQuantityInProducts
ON ShipmentDetails
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON

    DECLARE @ProductID INT, 
			@QuantityReceived INT, 
			@CostPerUnit MONEY

    SELECT @ProductID = ProductID,
		   @QuantityReceived = QuantityReceived,
           @CostPerUnit = CostPerUnit
    FROM inserted 

    UPDATE Products 
    SET StockQuantity = StockQuantity + @QuantityReceived,
        UnitPrice = @CostPerUnit + ( @CostPerUnit/10 ) 
    WHERE ProductID = @ProductID;

END


DROP TRIGGER trg_AddStockQuantityInProducts






CREATE TRIGGER trg_SubtractStockQuantityInProducts
ON OrderDetails
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON

    DECLARE @ProductID INT, 
			@Quantity INT,
			@StockQuantity INT

    SELECT @ProductID = ProductID,
		   @Quantity = Quantity
    FROM inserted 

	SELECT @StockQuantity = StockQuantity
	FROM Products 
    WHERE ProductID = @ProductID

    UPDATE Products 
    SET StockQuantity = @StockQuantity - @Quantity
    WHERE ProductID = @ProductID;

END


DROP TRIGGER trg_SubtractStockQuantityInProducts



CREATE TRIGGER trg_DeleteAnOrderRecordOrInsertion
ON OrderDetails
INSTEAD OF INSERT
AS
BEGIN
    SET NOCOUNT ON

    DECLARE @OrderID INT, @ProductID INT, @Quantity INT, @Discount INT,
			@StockQuantity INT, @UnitPrice MONEY

    SELECT @OrderID = OrderID, @ProductID = ProductID,
		   @Quantity = Quantity, @Discount = Discount
    FROM inserted 

	SELECT @StockQuantity = StockQuantity,
		   @UnitPrice = UnitPrice
	FROM Products
	WHERE ProductID = @ProductID

	SET @UnitPrice = @UnitPrice - ( ( @UnitPrice * @Discount ) / 100 )

	IF @Quantity <= @StockQuantity
	BEGIN
		INSERT INTO OrderDetails ( OrderID, ProductID, Quantity, UnitPrice, Discount )
		--SELECT OrderID, ProductID, Quantity, UnitPrice, Discount FROM inserted
		VALUES ( @OrderID, @ProductID, @Quantity, @UnitPrice, @Discount )
	END
/*
	ELSE 
	BEGIN 
		DELETE FROM Orders 
		WHERE OrderID = @OrderID
	END
*/
END


DROP TRIGGER trg_DeleteAnOrderRecordOrInsertion




------------------------------------------------------------------------------------------------------




CREATE PROCEDURE MonthlyCountOfOrders
    @StartDate DATE, @EndDate DATE
AS
BEGIN
    SET NOCOUNT ON;

	SELECT
		YEAR(OrderDate) AS [Order Year],
		MONTH(OrderDate) AS [Order Month],
		COUNT(OrderID) AS [Total Orders]
	FROM
		Orders_Denormalized
	WHERE
		OrderDate >= @StartDate AND 
		OrderDate < @EndDate
	GROUP BY
		YEAR(OrderDate), MONTH(OrderDate)
	ORDER BY
		YEAR(OrderDate), MONTH(OrderDate)

END

DROP PROCEDURE MonthlyCountOfOrders


EXEC MonthlyCountOfOrders '2020-02-04', '2024-12-03'










CREATE PROCEDURE SelectingTheTopEmployeesWithTheMostOrders
    @StartDate DATE, @EndDate DATE
AS
BEGIN
    SET NOCOUNT ON;

    SELECT TOP 3
        EmployeeID AS [Employee ID],
		CONCAT ( EmployeeFirstName, ' ', EmployeeLastName ) AS [Employee's Name],
		CASE WHEN EmployeePosition IS NULL 
		THEN 'Retired' ELSE EmployeePosition END
		AS [Employee's Position],
        COUNT(OrderID) AS [Orders Count]
    FROM
        Orders_Denormalized
    WHERE
        OrderDate >= @StartDate AND 
        OrderDate < @EndDate
    GROUP BY
        EmployeeID,
		CONCAT ( EmployeeFirstName, ' ', EmployeeLastName ),
		EmployeePosition
    ORDER BY
        COUNT( DISTINCT OrderID) DESC,
		EmployeeID

END

DROP PROCEDURE SelectingTheTopEmployeesWithTheMostOrders


EXEC SelectingTheTopEmployeesWithTheMostOrders '2020-02-04', '2024-6-03'











	

CREATE PROCEDURE CountTotalOrdersAndSalesForEachEmployee
    @StartDate DATE, @EndDate DATE
AS
BEGIN
    SET NOCOUNT ON;

	SELECT
		e.EmployeeID AS [Employee ID],
		CONCAT ( e.FirstName, ' ', e.LastName ) AS [Employee's Name],
		CASE WHEN ep.Position IS NULL 
		THEN 'Retired' ELSE ep.Position END
		AS [Employee Position],
		COUNT( DISTINCT o.OrderID) AS [Number of Orders],
		CONCAT( 'Rs. ', SUM( od.UnitPrice * od.Quantity ) ) AS [Total Sales Amount]
	FROM
		Employees e
	LEFT JOIN
		EmployeePosition ep ON e.PositionID = ep.PositionID
	JOIN
		Orders o ON e.EmployeeID = o.EmployeeID
	JOIN
		OrderDetails od ON o.OrderID = od.OrderID
	WHERE
		OrderDate >= @StartDate AND 
		OrderDate < @EndDate
	GROUP BY
		e.EmployeeID,
		CONCAT ( e.FirstName, ' ', e.LastName ),
		ep.Position
	ORDER BY
		SUM(od.UnitPrice * od.Quantity) DESC,
		e.EmployeeID


END

DROP PROCEDURE CountTotalOrdersAndSalesForEachEmployee


EXEC CountTotalOrdersAndSalesForEachEmployee '2020-02-04', '2024-06-03'









CREATE PROCEDURE TopFiveMostSellingProducts
    @StartDate DATE, @EndDate DATE
AS
BEGIN
    SET NOCOUNT ON;

	SELECT TOP 5
		p.ProductID AS [Product ID],
		p.Brand AS [Brand Name],
		p.ModelNumber AS [Model Number],
		CONCAT ( 'Rs. ', p.UnitPrice ) AS [Price],
		SUM(od.Quantity) AS [Total Quantity Sold]
	FROM
		Products p
		JOIN OrderDetails od 
		ON p.ProductID = od.ProductID
		JOIN Orders o 
		ON o.OrderID = od.OrderID
	WHERE 
		o.OrderDate >= @StartDate AND 
		o.OrderDate < @EndDate
	GROUP BY
		p.ProductID, p.Brand, p.ModelNumber, p.UnitPrice
	ORDER BY
		SUM(od.Quantity) DESC,
		p.ProductID

END

DROP PROCEDURE TopFiveMostSellingProducts


EXEC TopFiveMostSellingProducts '2021-02-04', '2024-06-03'










CREATE PROCEDURE TopCustomersSpending
    @number INT, @StartDate DATE, @EndDate DATE
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        [Customer ID],
        [Customer Name],
        [Quantity],
        [Total Spending]
    FROM
        (
            SELECT
                c.CustomerID AS [Customer ID],
                c.FirstName + ' ' + c.LastName AS [Customer Name],
                COUNT(od.Quantity) AS [Quantity],
                CONCAT('Rs. ', SUM(od.UnitPrice * od.Quantity)) AS [Total Spending],
                ROW_NUMBER() OVER (ORDER BY SUM(od.UnitPrice * od.Quantity) DESC) AS RowNum
            FROM
                Customers c
                JOIN Orders o ON c.CustomerID = o.CustomerID
                JOIN OrderDetails od ON o.OrderID = od.OrderID
            WHERE
                o.OrderDate >= @StartDate AND
                o.OrderDate < @EndDate
            GROUP BY
                c.CustomerID, c.FirstName, c.LastName
        ) AS RankedCustomers
    WHERE
        RowNum <= @number
    ORDER BY
        [Total Spending] DESC, [Quantity] DESC, [Customer ID]

END


DROP PROCEDURE TopCustomersSpending


EXEC TopCustomersSpending    12, '2021-02-04', '2024-06-03'









CREATE PROCEDURE ProductNotOrderInGivenInterval
    @StartDate DATE, @EndDate DATE
AS
BEGIN
    SET NOCOUNT ON;


	SELECT
		p.ProductID AS [Product ID],
		p.Brand AS [Brand Name],
		p.ModelNumber AS [Model Number],
		CONCAT ( 'Rs. ', p.UnitPrice ) AS [Price]
	FROM
		Products p
	WHERE
		p.ProductID NOT IN (
			SELECT DISTINCT
				od.ProductID
			FROM
				Orders o
				JOIN OrderDetails od ON o.OrderID = od.OrderID
			WHERE
                o.OrderDate >= @StartDate AND
                o.OrderDate < @EndDate
		)
	ORDER BY 
		p.Brand ASC,
		P.ModelNumber ASC

END


DROP PROCEDURE ProductNotOrderInGivenInterval


EXEC ProductNotOrderInGivenInterval '2023-02-04', '2024-06-03'










CREATE PROCEDURE SuppliersWithMaximumAndMinimumShipments
    @StartDate DATE, @EndDate DATE
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        s.SupplierID AS [Supplier ID],
        s.FirstName + ' ' + s.LastName AS [Supplier Name],
        COUNT(sh.ShipmentID) AS [Total Shipments],
        SUM(sd.CostPerUnit * sd.QuantityReceived) AS [Total Shipments Cost]
    FROM
        Suppliers s
        JOIN Shipments sh ON s.SupplierID = sh.SupplierID
        JOIN ShipmentDetails sd ON sh.ShipmentID = sd.ShipmentID
    WHERE
        sh.ShipmentDate >= @StartDate AND
        sh.ShipmentDate < @EndDate
    GROUP BY
        s.SupplierID, s.FirstName, s.LastName
    HAVING
        COUNT(sh.ShipmentID) = (
			SELECT MAX(ShipmentCount) 
			FROM (
				SELECT COUNT(sh.ShipmentID) AS ShipmentCount
					FROM Suppliers s
                    JOIN Shipments sh ON s.SupplierID = sh.SupplierID
                    JOIN ShipmentDetails sd ON sh.ShipmentID = sd.ShipmentID
                    WHERE sh.ShipmentDate >= @StartDate AND sh.ShipmentDate < @EndDate
                    GROUP BY s.SupplierID
				) AS Counts
		)
        OR
        COUNT(sh.ShipmentID) = (
			SELECT MIN(ShipmentCount) 
			FROM (
				SELECT COUNT(sh.ShipmentID) AS ShipmentCount
                FROM Suppliers s
                JOIN Shipments sh ON s.SupplierID = sh.SupplierID
                JOIN ShipmentDetails sd ON sh.ShipmentID = sd.ShipmentID
                WHERE sh.ShipmentDate >= @StartDate AND sh.ShipmentDate < @EndDate
                GROUP BY s.SupplierID
            ) AS Counts
		)
    ORDER BY
        COUNT(sh.ShipmentID) DESC,
		SUM(sd.CostPerUnit * sd.QuantityReceived) DESC

END


DROP PROCEDURE SuppliersWithMaximumAndMinimumShipments


EXEC SuppliersWithMaximumAndMinimumShipments '2023-02-04', '2024-06-03'










CREATE VIEW CountOfRepairServicesOrdersByEmployees AS

SELECT
    e.EmployeeID AS [Employee ID],
    e.FirstName + ' ' + e.LastName AS [Employee Name],
	CASE WHEN ep.Position IS NULL 
	THEN 'Retired' ELSE ep.Position END
	AS [Employee Position],    
	COUNT( DISTINCT orp.OrderID ) AS [Number of Orders in Repair Serives]  
FROM
    Employees e
LEFT JOIN
    EmployeePosition ep ON e.PositionID = ep.PositionID
JOIN
    Orders o ON e.EmployeeID = o.EmployeeID
JOIN
    OrderRepairs orp ON o.OrderID = orp.OrderID
GROUP BY
    e.EmployeeID, e.FirstName, e.LastName, ep.Position


DROP VIEW CountOfRepairServicesOrdersByEmployees 

SELECT * FROM CountOfRepairServicesOrdersByEmployees 










CREATE VIEW SupplierShipmentCounts AS
SELECT
    s.SupplierID AS [Supplier ID],
    s.FirstName + ' ' + s.LastName AS [Supplier Name],
	sh.ShipmentDate AS [Shipment Date],
    COUNT(sh.ShipmentID) AS [Total Shipments],
    SUM(sd.CostPerUnit * sd.QuantityReceived) AS [Total Shipments Cost]
FROM
    Suppliers s
    JOIN Shipments sh ON s.SupplierID = sh.SupplierID
    JOIN ShipmentDetails sd ON sh.ShipmentID = sd.ShipmentID
GROUP BY
    s.SupplierID, s.FirstName, s.LastName, sh.ShipmentDate


DROP VIEW SupplierShipmentCounts

SELECT * FROM SupplierShipmentCounts











CREATE PROCEDURE SuppliersWithMaxAndMinShipments
    @StartDate DATE, @EndDate DATE
AS
BEGIN
    SET NOCOUNT ON;

    SELECT *
    FROM SupplierShipmentCounts
    WHERE [Shipment Date] >= @StartDate
        AND [Shipment Date] < @EndDate
        AND (
            [Total Shipments] = (
                SELECT MAX([Total Shipments])
                FROM SupplierShipmentCounts
            )
            OR
            [Total Shipments] = (
                SELECT MIN([Total Shipments])
                FROM SupplierShipmentCounts
            )
        );
END;



DROP PROCEDURE SuppliersWithMaxAndMinShipments


EXEC SuppliersWithMaxAndMinShipments '2023-02-04', '2024-06-03'











CREATE PROCEDURE CalculateProfitOnProducts
    @StartDate DATE, @EndDate DATE
AS
BEGIN
    SET NOCOUNT ON;

	SELECT
		CONCAT( 'Rs. ', SUM (od.Quantity * od.UnitPrice) ) AS Revenue,
		CONCAT( 'Rs. ', SUM ((p.UnitPrice - (p.UnitPrice/10)) * od.Quantity) ) AS Expenses,
		CONCAT( 'Rs. ', SUM ( (od.Quantity * od.UnitPrice) - ((p.UnitPrice - (p.UnitPrice/10)) * od.Quantity) ) ) AS Profit
	FROM
		Orders AS o
	JOIN
		OrderDetails AS od ON o.OrderID = od.OrderID
	JOIN
		Products AS p ON od.ProductID = p.ProductID
	WHERE 
		OrderDate >= @StartDate AND 
		OrderDate < @EndDate
		
END


DROP PROCEDURE CalculateProfitOnProducts


EXEC CalculateProfitOnProducts '2023-02-04', '2023-02-05'









CREATE TABLE AuditTable (

    TableName VARCHAR(50), 
	Operation VARCHAR(50),
    ModifiedBy VARCHAR(50), 
    ModifiedDate DATETIME

);


SELECT * FROM AuditTable



CREATE TRIGGER trg_AuditInsertionShipment
ON ShipmentDetails
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO AuditTable
	VALUES( 'ShipmentDetails', 'Insertion', SUSER_SNAME(), GETDATE() )

END


DROP TRIGGER trg_AuditInsertionShipment




CREATE TRIGGER trg_AuditDeletionShipment
ON ShipmentDetails
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO AuditTable
	VALUES( 'ShipmentDetails', 'Deletion', SUSER_SNAME(), GETDATE() )

END


DROP TRIGGER trg_AuditDeletionShipment




CREATE TRIGGER trg_AuditUpdationShipment
ON ShipmentDetails
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO AuditTable
	VALUES( 'ShipmentDetails', 'Updation', SUSER_SNAME(), GETDATE() )

END


DROP TRIGGER trg_AuditUpdationShipment




CREATE TRIGGER trg_AuditInsertionOrders
ON OrderDetails
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO AuditTable
	VALUES( 'OrderDetails', 'Insertion', SUSER_SNAME(), GETDATE() )

END


DROP TRIGGER trg_AuditInsertionOrders



CREATE TRIGGER trg_AuditDeletionOrders
ON OrderDetails
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO AuditTable
	VALUES( 'OrderDetails', 'Deletion', SUSER_SNAME(), GETDATE() )

END


DROP TRIGGER trg_AuditDeletionOrders



CREATE TRIGGER trg_AuditUpdationOrders
ON OrderDetails
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO AuditTable
	VALUES( 'OrderDetails', 'Updation', SUSER_SNAME(), GETDATE() )

END


DROP TRIGGER trg_AuditUpdationOrders







CREATE TRIGGER trg_AuditInsertionOrdersR
ON OrderRepairs
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO AuditTable
	VALUES( 'OrderRepairs', 'Insertion', SUSER_SNAME(), GETDATE() )

END


DROP TRIGGER trg_AuditInsertionOrdersR



CREATE TRIGGER trg_AuditDeletionOrdersR
ON OrderRepairs
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO AuditTable
	VALUES( 'OrderRepairs', 'Deletion', SUSER_SNAME(), GETDATE() )

END


DROP TRIGGER trg_AuditDeletionOrdersR



CREATE TRIGGER trg_AuditUpdationOrdersR
ON OrderRepairs
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO AuditTable
	VALUES( 'OrderRepairs', 'Updation', SUSER_SNAME(), GETDATE() )

END


DROP TRIGGER trg_AuditUpdationOrdersR














SELECT * FROM Shipments
SELECT * FROM Products

SELECT * FROM AuditTable

SELECT * FROM ShipmentDetails


INSERT INTO ShipmentDetails (ShipmentID, ProductID, QuantityReceived, CostPerUnit)
VALUES 
( 248, 662, 560, 10322.50),
( 249,663, 258, 8345.75),
( 250, 664,137, 34220.99),
( 251, 665,1000, 9954.99),
( 252, 661, 100, 5345.00),
( 253,667, 200, 2433.50),
( 254, 668,20, 1232.00)


UPDATE TABLE ShipmentDetails
SET CostPerUnit = 70700
WHERE ProductID = 667 


DELETE FROM ShipmentDetails
WHERE ShipmentDetailID = 20612









SELECT * FROM Orders
SELECT * FROM Products

SELECT * FROM AuditTable

SELECT * FROM OrderDetails


INSERT INTO Orders


INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice, Discount)
VALUES 
( 2, 662, 2, 10322.50, 3),
( 3,663, 2, 8345.75, 2),
( 4, 664,1, 34220.99, 0),
( 4, 665,1, 9954.99, 0),
( 5, 661,2, 5345.00, 1),
( 6,667, 2, 2433.50, 0),
( 5, 668,3, 1232.00, 2)


UPDATE TABLE OrderDetails
SET Quantity = 3
WHERE OrderDetailID = 447446


DELETE FROM OrderDetails
WHERE OrderDetailID = 447447






/*

CREATE PROCEDURE InsertionIntoOrdersAndOrderDetails
    @CustomerID INT, @EmployeeID INT, @OrderDate INT, @PaymentMethod INT,
	@ProductID INT, @Quantity INT, @UnitPrice INT, @Discount INT
AS
BEGIN
    --SET NOCOUNT ON;

    DECLARE @StockQuantity INT, @OrderID INT

	SELECT @StockQuantity = StockQuantity
	FROM Products 
	WHERE ProductID = @ProductID
	
	IF @Quantity <= @StockQuantity
	BEGIN

		INSERT INTO Orders ( CustomerID, EmployeeID, OrderDate, PaymentMethod ) 
		VALUES ( @CustomerID, @EmployeeID, @OrderDate, @PaymentMethod )

		SELECT @OrderID = OrderID FROM inserted

		INSERT INTO OrderDetails ( OrderID, ProductID, Quantity, UnitPrice, Discount )
		VALUES ( @OrderID, @ProductID, @Quantity, @UnitPrice, @Discount )
		
END


DROP PROCEDURE InsertionIntoOrdersAndOrderDetails

*/



---------------------------------------------------------------------------------------------------------------------

DROP TABLE OrderDetails
DROP TABLE Orders
DROP TABLE Employees
DROP TABLE EmployeePosition
DROP TABLE Customers
DROP TABLE ShipmentDetails
DROP TABLE Shipment
DROP TABLE Suppliers
DROP TABLE Products



