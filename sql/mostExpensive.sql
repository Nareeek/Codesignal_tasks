CREATE PROCEDURE mostExpensive()
BEGIN
    /* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT name 
    FROM (
        SELECT *, price * quantity as Amount 
        FROM Products 
    ) p 
    ORDER BY Amount DESC, name asc
    LIMIT 1;
END