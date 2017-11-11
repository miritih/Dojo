[![CircleCI](https://circleci.com/gh/mwenda-eric/Dojo.svg?style=svg)](https://circleci.com/gh/mwenda-eric/Dojo)
[![Test Coverage](https://api.codeclimate.com/v1/badges/87d50f8e61a23165de11/test_coverage)](https://codeclimate.com/github/mwenda-eric/Dojo/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/87d50f8e61a23165de11/maintainability)](https://codeclimate.com/github/mwenda-eric/Dojo/maintainability)
# Dojo
Office space allocation CLI application. 
## Istalation
To install this project, follow these steps:
* Create your working environment. example: `virtualenv env` 
* Git clone this project `git clone https://github.com/mwenda-eric/dojo.git`
* `cd dojo`
* Install project dependencies `pip install -r requirements.txt`
* Finally run `python app.py`
### Tests
Run `nosetests tests --with-coverage --cover-xml`
### Usage
    ```
    create_room <type_room> <room_name>...
    add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
    reallocate_person <person_name> <new_room_name>
    print_allocations [-o=filename]
    print_unallocated [-o=filename]
    print_room <room_name>
    load_people
    q
    ```
###### 1. create_room
Creates a new room with
###### 2. add_person
Adds a person and randomly assigns them to aroom
###### 3. reallocate_person
reallocates person to a diffrent room
###### 4. print_allocations
prints all allocations. providing option `-o` writes outputs to a file
###### 5. print_unallocated
prints all unallocations. providing option `-o` writes outputs to a file
###### 6. print_room
prints all rooms and their members 
###### 7 load_people
loads poeple from a file
###### 8. q
quits application

#### credits
* eric mwenda




Tests

Run tests with nosetests

License: CocoaPods