use food;

SELECT 
    p.City,
    COUNT(DISTINCT p.Provider_ID) AS total_providers,
    COUNT(DISTINCT r.Receiver_ID) AS total_receivers
FROM providers p
LEFT JOIN receivers r 
    ON p.City = r.City
GROUP BY p.City
ORDER BY 2 DESC;

SELECT 
    City,
    COUNT(DISTINCT Provider_ID) AS total_providers
FROM providers
GROUP BY city
ORDER BY 2 DESC;

SELECT 
    City,
    COUNT(DISTINCT Receiver_ID) AS total_receivers
FROM receivers
GROUP BY city
ORDER BY 2 DESC;

SELECT 
    Provider_Type,
    SUM(Quantity) AS total_food_contributed
FROM food_listings
GROUP BY Provider_Type
ORDER BY total_food_contributed DESC;

-- 3.	What is the contact information of food providers in a specific city?

SELECT 
    Name,
    Type,
    Address,
    Contact
FROM providers
WHERE City = 'New Carol';  -- replace with required city

-- 4.	Which receivers have claimed the most food?

SELECT 
    r.Receiver_ID,
    r.Name,
    SUM(f.Quantity) AS total_food_claimed
FROM claims c
JOIN receivers r 
    ON c.Receiver_ID = r.Receiver_ID
JOIN food_listings f 
    ON c.Food_ID = f.Food_ID
WHERE c.Status = 'Completed'
GROUP BY r.Receiver_ID, r.Name
ORDER BY total_food_claimed DESC
LIMIT 1;

-- 5.	What is the total quantity of food available from all providers?

SELECT 
    SUM(Quantity) AS total_food_available
FROM food_listings;

-- 6.	Which city has the highest number of food listings?

SELECT 
    Location AS city,
    COUNT(Food_ID) AS total_listings
FROM food_listings
GROUP BY Location
ORDER BY total_listings DESC;

-- 7.	What are the most commonly available food types?

SELECT 
    Food_Type,
    COUNT(Food_ID) AS total_items
FROM food_listings
GROUP BY Food_Type
ORDER BY total_items DESC;

-- 8. How many food claims have been made for each food item?

SELECT 
    f.Food_ID,
    f.Food_Name,
    COUNT(c.Claim_ID) AS total_claims
FROM food_listings f
LEFT JOIN claims c 
    ON f.Food_ID = c.Food_ID
GROUP BY f.Food_ID, f.Food_Name
ORDER BY total_claims DESC;

SELECT 
    f.Food_ID,
    f.Food_Name,
    COUNT(c.Claim_ID) AS total_claims
FROM food_listings f
LEFT JOIN claims c 
    ON f.Food_ID = c.Food_ID
WHERE c.Status = 'Completed'
GROUP BY f.Food_ID, f.Food_Name
ORDER BY total_claims DESC;

-- 9. Which provider has had the highest number of successful food claims?

SELECT 
    p.Provider_ID,
    p.Name,
    COUNT(c.Claim_ID) AS successful_claims
FROM providers p
JOIN food_listings f 
    ON p.Provider_ID = f.Provider_ID
JOIN claims c 
    ON f.Food_ID = c.Food_ID
WHERE c.Status = 'Completed'
GROUP BY p.Provider_ID, p.Name
ORDER BY successful_claims DESC;

-- 10. What percentage of food claims are completed vs. pending vs. canceled?

SELECT 
    Status,
    COUNT(*) AS total_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims), 2) AS percentage
FROM claims
GROUP BY Status;

SELECT 
    Status,
    COUNT(*) AS total_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM claims
GROUP BY Status;

-- 11. What is the average quantity of food claimed per receiver?

SELECT 
    AVG(total_quantity) AS avg_food_per_receiver
FROM (
    SELECT 
        c.Receiver_ID,
        SUM(f.Quantity) AS total_quantity
    FROM claims c
    JOIN food_listings f 
        ON c.Food_ID = f.Food_ID
    WHERE c.Status = 'Completed'
    GROUP BY c.Receiver_ID
) t;

SELECT 
    r.Receiver_ID,
    r.Name,
    AVG(f.Quantity) AS avg_quantity_per_claim
FROM claims c
JOIN receivers r 
    ON c.Receiver_ID = r.Receiver_ID
JOIN food_listings f 
    ON c.Food_ID = f.Food_ID
WHERE c.Status = 'Completed'
GROUP BY r.Receiver_ID, r.Name;

-- 12. Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?

SELECT 
    f.Meal_Type,
    COUNT(c.Claim_ID) AS total_claims
FROM claims c
JOIN food_listings f 
    ON c.Food_ID = f.Food_ID
WHERE c.Status = 'Completed'
GROUP BY f.Meal_Type
ORDER BY total_claims DESC;

-- 13.	What is the total quantity of food donated by each provider?

SELECT 
    p.Provider_ID,
    p.Name,
    SUM(f.Quantity) AS total_food_donated
FROM providers p
JOIN food_listings f 
    ON p.Provider_ID = f.Provider_ID
GROUP BY p.Provider_ID, p.Name
ORDER BY total_food_donated DESC;