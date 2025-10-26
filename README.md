# Articulate Rating & Review


### Installation Setup:

#### Dockerized Automatic Installation with mariaDB setup (Preferred):
* Clone the repository.
* Ensure you have docker installed.
* run docker-compose up -d
* **it will install everything and will run the server**
* mariaDb + server + superuser will be created automatically.

#### Manual Installation:
* Clone the repository.
* create python virtual env >= 3.12.8
* activate virtual env
* install requirements.txt
* migrations
* create superuser
* collect static files
* run server
* **In this you have to manually set up the database and create a superuser**
