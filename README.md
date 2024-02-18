Rental Platform Clone

Overview

This project aims to replicate functionalities of a popular rental platform like AirBnB. It defines classes for User, Place, State, City, Amenity, and Review which inherit from the BaseModel class. Instances of these classes are serialized and stored in a JSON file, and can be deserialized back into instances when needed. Additionally, a command-line interface (CLI) is provided for easy interaction with the application.

System Requirements

Python 3.4.3 or later is required to run this application.

Usage

The application can be used in two modes: interactive and non-interactive.

Interactive Mode

To launch the interactive mode, execute:

$ ./console.py

You'll see the prompt:

(hbnb) 

Here, you can enter commands and get corresponding outputs. For example:


(hbnb) all

["[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}"]
Non-interactive Mode
You can run the application in non-interactive mode using commands from the command line:


$ echo "all" | ./console.py

["[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}"]
Or by passing a file containing commands:

$ cat commands.txt

all User

$ cat commands.txt | ./console.py

["[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}"]
Storage

Instances of classes are saved in JSON format to the file.json file in the root directory. Any modifications made to the objects are automatically saved to this file, providing persistence across sessions.

Testing

A comprehensive testing suite is included using Python's unittest module. To run the entire suite:

$ python3 -m unittest discover tests
............................................................
----------------------------------------------------------------------
Ran 60 tests in 0.017s

OK
Individual tests can be run as well:



$ python3 -m unittest tests/test_models/test_base_model.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.003s
OK
