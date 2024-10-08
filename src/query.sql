SELECT Linkedin_PersonalEmail.first_name,Linkedin_PersonalEmail.last_name,Linkedin_PersonalEmail.email,Linkedin_PersonalEmail.linkedin_url AS 'linkedin URL',
Linkedin_Company.name AS company, Linkedin_Company.linkedin_url AS 'company URL',Linkedin_Company.size,
Fund_Company.category AS Label, Fund_Company.project_url AS funding, Fund_Company.amount AS 'funding amount', Fund_Company.date AS 'last funding',
Linkedin_Job.title AS job, Linkedin_Job.linkedin_url AS 'job url',Events_GuestList.event_id,
Linkedin_PersonalEmail.role
FROM Linkedin_Company
LEFT JOIN Linkedin_PersonalEmail ON  Linkedin_Company.id = Linkedin_PersonalEmail.company_id
LEFT JOIN Fund_Company ON Linkedin_Company.name = Fund_Company.name
LEFT JOIN Linkedin_Job ON Linkedin_Company.id = Linkedin_Job.company_id
LEFT JOIN Events_GuestList ON Linkedin_Company.id = Events_GuestList.company_id;
