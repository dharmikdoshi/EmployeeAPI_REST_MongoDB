Open the PostMan Collection and test all the APIs first.
1. For creating an employee - http://127.0.0.1:8000/employee use this link in postman, select request method as POST and use the raw json to enter your data.
2. For Getting all employees - http://127.0.0.1:8000/employee use this link and select request method as GET.
3. For deleting an employee - http://127.0.0.1:8000/employee/<id> add the id at the end of the link. and select request method as DELETE.
4. For updating an employee - http://127.0.0.1:8000/employee use this and select request method as PUT and enter all the details of the employee to be updated.


open the mongo db atlas cloud and generate your collection link and open it with mongo db compass. Update your database setting in settings.py