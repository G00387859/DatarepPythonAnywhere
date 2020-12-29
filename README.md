# DatarepPythonAnywhere
This project created and changed to a new repo during this project,https://github.com/G00387859/DATA-REPRESENTATION-AND-QUERY, https://github.com/G00387859/DATA-REPRESENTATION-AND-QUERYING because I had trouble updating https://github.com/G00387859/DATA-REPRESENTATION-AND-QUERYING so I created https://github.com/G00387859/DATA-REPRESENTATION-AND-QUERY and then I though that it would be a better project submission to have only the project code. so I create this one.<br/>
This contains the project.<br/> 	
In this project the objectivate to create a rest_server and repersent data from backend mysql table.<br/> 
The rest server uses flask<br/>
While the code runs on python anywhere I could not get the backend database to stay connected even when I applied the changes made in the optional lectures and reverted as did not make a difference. I guess I have to use the SQLALCHEMY, which I have not done for the submission. If the session on pythonanywhere fallover, and it will, the code is identical to the code in the project.<br/> I have added a doc that show it working called Pythonanywhere working. in the repo.<br/>
I have a login page which is simiular to a login page for w3 schools referenced in the code. I have added to the repo a document that shows the pythonanyhere working. https://github.com/G00387859/DatarepPythonAnywhere/blob/main/Pythonanywhere%20working.docx 
<br/>
*****
This project create a rest server connected to a backed mysql database. The rest server will do CRUD operations for a store or shop. The store will have a list of products. productName, productType, productPrice.<br/> The mySql primary key in a number incremented but the ProductName is a unique key. 
use datarepresentation;
    CREATE TABLE store (
    id int NOT NULL auto_increment,
    productType VARCHAR(100),
    productName varchar(100),
    productPrice float(4),
    PRIMARY KEY(id),
    UNIQUE KEY unique_productName (productName)
);
<br/>
The store will open not on index.html but on home.html where where the front page will show the shop. From here the product will be dispayed and and once login the staff member will be allowed to do CRUD operations.<br/>




