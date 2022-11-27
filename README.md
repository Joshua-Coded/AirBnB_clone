# AirBnB clone Project 

Project Description 

Here, We'll be cloning the console part of the AirBnB clone Project.

We'll be writing a command interpreter to manage our AirBnb objects.

We'll need to 
- put in place a parent class (called BaseModel) to take care of the 
initialization, serialization and deserialization of your future instances 
- create a simple flow of serialization/deserialization: Instance < - >
Dictionary < - > json string < - > file
- create all clases used for AirBnB(User,  State, City, Place...) that
inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittest to validate all our classes and storage engine.

Our command interpreter would be able to:


    - Create a new object(ex: a new User or a new Place)


    - Retrieve an object from a file, a database etc...


    - Do operations on objects(count, compute stats, etc...)


    - Update attributes of an object


    - Destroy an object 
