## AirBnB Clone - The Console

The console is the first segment of the AirBnB project wich is used to manage objects for the AirBnB website. The goal of this project is to eventually deploy our server a simple clone of the AirBnB Website.

### Functionalities of this command interpreter:
- Create a new object (ex: a new User or a new Place)
- Update attributes of an object
- Destroy an object
- Do operations on objects (count, compute stats, etc...)
- Retrieve an object from a file, a database etc...

### Class and Method Descriptions

+ BaseModel - class which contains all common attribute and methods of other classes, and other classes will be derived from this class.
    + ```def __init__(self, *args, **kwargs)``` - Initialization of the base model
    + ```def __str__(self)``` - String representation of the BaseModel class
    + ```def save(self)``` - Updates the attribute updated_at with the current datetime
	+ ```def to_dict(self)``` - returns a dictionary containing all keys/values of the instance
##### Classes inherited from Base Model:

1. User
2. State
3. Place
4. Amenitiy
5. City
6. Review

+ FileStorage - class which acts as a mediator between the console user and the storage.
    + ```def save(self)``` - Serializes an object
    + ```def reload(self)``` - Deserializes an object
    + ```def new(self, object)``` - adds the object to a dictionary container
    + ```def all(self)``` - returns the dictionary container of objects
