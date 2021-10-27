# Assignment_3
As a database you can use any SQL database( postgresql, mysql, sqlite)
Database should have at least one Table with name User, and columns: id, login, password, token
User Table should contain at least 3 records
# /login
Use as a baseline a code which was provided in a Week 6, Moodle
After successful login( if login and password matches with a record in User Table), as response route should return html text: token: <token value> and store that token in the User Table
If provided login and password does not exist in the User Table, as a response route should return html text: Could not found a user with login: <login>
# /protected
This route should receive as a parameter token value
Token value needs to be passed over URL, 
e.g. http://127.0.01:5000/protected?token=24230ifdsjfjdsklfj43943ut943
This route should return html text: Hello, token which is provided is correct, if as a parameter RIGHT token value is passed
This route should return html text: Hello, Could not verify the token, if as a parameter WRONG token value is passed
# Example
![image](https://user-images.githubusercontent.com/80098706/139100353-db7d1248-10cc-4ef1-84ca-f75ac5ce9c45.png)
# after login, table is updated
![image](https://user-images.githubusercontent.com/80098706/139100453-55973230-80c8-47b4-a47e-664801be1181.png)
![image](https://user-images.githubusercontent.com/80098706/139100911-e908213e-897b-489e-8416-2c0442c008de.png)
![image](https://user-images.githubusercontent.com/80098706/139101043-d79fef14-f306-4a28-87c1-c1bcd87a6892.png)
![image](https://user-images.githubusercontent.com/80098706/139100240-5ce6f2ca-984f-4c8a-a5a7-79569835f044.png)

  
