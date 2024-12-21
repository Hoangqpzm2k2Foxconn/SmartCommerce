-- Database schema for managing money and online transactions in SQLite

-- Users Table: Stores customer and seller details
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Phone TEXT,
    Role TEXT CHECK (Role IN ('Customer', 'Seller')) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Transactions Table: Logs all money-related activities
CREATE TABLE Transactions (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER NOT NULL,
    Type TEXT CHECK (Type IN ('Add', 'Withdraw', 'Purchase')) NOT NULL,
    Amount REAL NOT NULL,
    Status TEXT CHECK (Status IN ('Pending', 'Completed', 'Failed')) DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Orders Table: Records purchase details
CREATE TABLE Orders (
    OrderID TEXT PRIMARY KEY,
    UserID INTEGER NOT NULL,
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    StoreName TEXT NOT NULL,
    ProductName TEXT NOT NULL,
    SellerUsername TEXT NOT NULL,
    Quantity INTEGER NOT NULL,
    UnitPrice REAL NOT NULL,
    Discount REAL DEFAULT 0.0,
    TotalAmount REAL GENERATED ALWAYS AS (Quantity * UnitPrice - Discount) STORED,
    RefundAmount REAL DEFAULT 0.0,
    Status TEXT CHECK (Status IN ('Pending', 'Confirmed', 'Cancelled')) DEFAULT 'Pending',
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Bank Transfers Table: Tracks money added to the system via bank transfer
CREATE TABLE BankTransfers (
    TransferID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER NOT NULL,
    BankAccount TEXT NOT NULL,
    Amount REAL NOT NULL,
    Status TEXT CHECK (Status IN ('Pending', 'Completed', 'Failed')) DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Indexes to optimize queries
CREATE INDEX idx_user_transactions ON Transactions(UserID);
CREATE INDEX idx_user_orders ON Orders(UserID);
