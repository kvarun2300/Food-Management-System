# Food-Management-System

Local Food Wastage Management System
## 1. Problem Statement

Food wastage is a critical global issue where large quantities of surplus food from households, restaurants, and grocery stores are discarded daily, while many individuals and communities face food insecurity. This imbalance highlights the need for an efficient system to redistribute excess food.

This project proposes the development of a Local Food Wastage Management System that enables:

Food providers (restaurants, individuals) to list surplus food.
Receivers (NGOs or individuals) to claim available food.
Storage of food availability and location data using SQL.
A Streamlit-based application for interaction, filtering, CRUD operations, and visualization.

## 2. Business Use Cases

The system addresses real-world challenges through the following use cases:

Food Redistribution: Connects surplus food providers with individuals or organizations in need.
Waste Reduction: Minimizes food wastage by ensuring timely redistribution.
Accessibility: Enables easy location-based search using geolocation features.
Data-Driven Decisions: Provides analytical insights into food wastage trends and demand patterns.

## 3. Approach
### 3.1 Data Preparation
Utilized structured datasets containing food donation records.
Cleaned and standardized data for consistency and accuracy.
Handled missing values and ensured uniform formatting.
### 3.2 Database Creation
Designed SQL tables for providers, receivers, food listings, and claims.
Established relationships using primary and foreign keys.
Implemented CRUD operations for dynamic data management.
### 3.3 Data Analysis
Performed SQL-based analysis to identify trends in food availability and demand.
Generated insights based on location, food type, and claim patterns.
Developed query-based reporting for decision-making.
### 3.4 Application Development

A Streamlit application was developed to:

Display outputs of 13+ SQL queries.
Provide filtering options (city, provider, food type, meal type).
Enable CRUD operations (Create, Read, Update, Delete).
Show contact details for direct communication between providers and receivers.
3.5 Deployment
The application is designed for deployment on platforms like Streamlit Cloud.
Ensures real-time accessibility and user interaction.

## 4. Data Flow and Architecture
### 4.1 Data Storage
SQL database stores structured data for:
Food providers
Receivers
Food listings
Claims
### 4.2 Processing Pipeline
Data is processed using SQL queries and Python (Pandas).
Analytical insights are generated from structured queries.
### 4.3 Application Layer
Streamlit acts as the front-end interface.
Enables user interaction, visualization, and database operations.

## 5. Dataset

The system uses four datasets:

Providers Dataset (providers.csv)
Contains provider details such as name, type, location, and contact.
Receivers Dataset (receivers.csv)
Includes information about individuals or organizations receiving food.
Food Listings Dataset (food_listings.csv)
Stores available food items, quantity, expiry date, and type.
Claims Dataset (claims.csv)
Tracks claims made by receivers along with status and timestamps.

## 6. Dataset Description
Providers Dataset
Provider_ID (Primary Key)
Name
Type (Restaurant, Grocery Store, etc.)
Address
City
Contact
Receivers Dataset
Receiver_ID (Primary Key)
Name
Type (NGO, Individual, etc.)
City
Contact
Food Listings Dataset
Food_ID (Primary Key)
Food_Name
Quantity
Expiry_Date
Provider_ID (Foreign Key)
Provider_Type
Location
Food_Type
Meal_Type
Claims Dataset
Claim_ID (Primary Key)
Food_ID (Foreign Key)
Receiver_ID (Foreign Key)
Status (Pending, Completed, Cancelled)
Timestamp

## 7. SQL Queries & Analysis

The system answers key analytical questions:

Food Providers & Receivers
Number of providers and receivers per city
Top contributing provider type
Provider contact details by city
Top receivers based on food claimed
Food Listings & Availability
Total food quantity available
City with highest listings
Most common food types
Claims & Distribution
Claims per food item
Provider with highest successful claims
Claim status distribution (Completed, Pending, Cancelled)
Analysis & Insights
Average food claimed per receiver
Most claimed meal type
Total food donated per provider

## 8. Results
✅ Application Features
Interactive Streamlit dashboard
Dynamic filtering by location, provider, and food type
Contact visibility for providers and receivers
Full CRUD functionality
Integration of all analytical queries
✅ Analytical Insights
Identification of top food contributors
Detection of high-demand locations
Understanding claim success rates
Recognition of food wastage patterns

## 9. Project Evaluation Metrics
Database Completeness: Proper structuring and relationships
Query Accuracy: Correct and meaningful SQL outputs
CRUD Functionality: Reliable data modification operations
User Experience: Intuitive and responsive UI design

## 10. Technical Stack
Programming Language: Python
Database: MySQL / SQL
Framework: Streamlit
Libraries: Pandas, NumPy
Domain: Data Analysis, Food Management

## 11. Deliverables
Data Preparation
Cleaned and structured datasets for analysis
SQL Analysis
Implementation of 13+ queries for insights
Application Development
Fully functional Streamlit app
Integrated visualization and filtering features

## 12. Conclusion

The Local Food Wastage Management System provides an efficient and scalable solution to reduce food wastage and address food insecurity. By combining SQL-based analytics with an interactive Streamlit interface, the system enables real-time food redistribution, enhances accessibility, and supports data-driven decision-making.

This project demonstrates the effective integration of data engineering, analytics, and application development to solve a real-world problem.
