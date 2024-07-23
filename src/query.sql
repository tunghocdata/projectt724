SELECT DISTINCT
    lc.name AS company_name, 
    lj.title AS job_title, 
    lc.size AS company_size, 
    fc.amount AS funding_amount, 
    fc.date AS funding_date
FROM 
    linkedin_company lc
INNER JOIN 
    linkedin_job lj ON lc.id = lj.company_id
INNER JOIN 
    fund_company fc ON lc.linkedin_url = fc.linkedin_url
WHERE 
    lj.title LIKE '%Engineer%'
    AND fc.amount > 0
ORDER BY
lc.name ASC;
