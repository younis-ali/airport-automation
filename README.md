# Airplane Mode App

## Overview

The **Airplane Mode** app is a Frappe-based custom application designed to manage flight ticket systems. The app includes functionalities for managing airlines, airplanes, airports, flights, and passengers. Additionally, it supports features like booking, add-ons, and document states.

## DocTypes

### 1. Airline

- **Fields:**
  - Founding Year (Int, Non-negative)
  - Customer Care Number (Data, Mandatory)
  - Headquarters (Data, Mandatory)

### 2. Airplane

- **Fields:**
  - Model (Data, Mandatory)
  - Airline (Link to Airline DocType, Mandatory)
  - Capacity (Int, Non-negative, Mandatory)

### 3. Airport

- **Fields:**
  - Code (Data, Mandatory)
  - City (Data, Mandatory)
  - Country (Data, Mandatory)

### 4. Flight Passenger

- **Fields:**
  - First Name (Data, Mandatory)
  - Last Name (Data)
  - Date Of Birth (Date, Mandatory)

- **Controller Logic:**
  - Full Name field is auto-set based on First Name and Last Name.
  - Title field is set to Full Name.

### 5. Airplane Ticket

- **Fields:**
  - Passenger (Link to Flight Passenger, Mandatory)
  - Source Airport (Link to Airport, Mandatory)
  - Destination Airport (Link to Airport, Mandatory)
  - Source Airport Code (Fetched, Read-only, Mandatory)
  - Destination Airport Code (Fetched, Read-only, Mandatory)
  - Flight (Link to Airplane Flight, Mandatory)
  - Departure Date (Date, Mandatory)
  - Departure Time (Time, Mandatory)
  - Duration of Flight (Duration, Mandatory)
  - Status (Select, Mandatory; Options: Booked, Checked-In, Boarded)
  - Seat (Data, Read-only)

- **Controller Logic:**
  - Auto-generate Seat field value (e.g., 89E, 21A).
  - Prevent submission unless status is 'Boarded'.

### 6. Airplane Flight

- **Fields:**
  - Airplane (Link to Airplane DocType, Mandatory)
  - Date of Departure (Date, Mandatory)
  - Time of Departure (Time, Mandatory)
  - Duration (Duration, Mandatory)
  - Status (Select; Options: Scheduled, Completed, Cancelled)

## Add-ons

### 1. Airplane Ticket Add-on Type

- **Fields:**
  - Description (Data)

### 2. Airplane Ticket Add-on Item

- **Fields:**
  - Item (Link to Airplane Ticket Add-on Type, Mandatory)
  - Amount (Currency, default 0)

- **Controller Logic:**
  - Calculate the total amount for the ticket including add-ons.
  - Ensure unique add-on items in the child table.

## Workspace

The app includes a custom workspace with shortcuts to manage Airlines, Passengers, and Airplanes.
#### License

mit