# HashAPI
RESTful API service using Python Flask.

## API Service Utilized by hash_cli

#### Description:
The hash_api Python(3.6) flask web service API connects the hash_cli Client to a MongoDB database.  MongoDB is currently the only supported database for this web application.  MongoDB also must have user authentication enabled.  

## Getting Started

#### Install MongoDB via homebrew
Install homebrew
```
install homebrew @ http://brew.sh/
```
Update homebrew
```
brew update
```
Install mongodb
```
brew install mongodb
```
Make Mongo Data Dir
```
mkdir -p /path/to/mongo/data/dir
```
Point Mongo To The Created data/dir, and register IP address(s)
```
edit mongod.conf:

systemLog:
  destination: file
  path: /path/to/mongo/log/file.log
  logAppend: true
storage:
  dbPath: /path/to/mongo/data/dir
net:
  bindIp: 127.0.0.1, <if using remote connection, add that here>
  port: 27017
security:
  authorization: enabled
```
Test Mongo Installation
```
mongo
exit
```
### Create Required Mongo Database and Add Application User
```
mongo
use hashdb
db.createUser(
   {
     user: "appuser",
     pwd: "apppassword",
     roles:
       [
         { role: "readWrite", db: "hashdb" },
       ]
   }
)
exit
```
Ensure Authentication is Enabled with Mongo Service File
```
sudo nano /lib/systemd/system/mongod.service
```
Check line 9 'ExecStart' and add --auth if not already there
```
ExecStart=/usr/bin/mongod --quite --auth --config /etc/mongod.config
```
Restart MongoDB for changes to take effect
```
sudo service mongod restart
[ok] Restarting database: mongod
```
Your MongoDB is now installed and using authentication.  Feel free to
test this out in your preferred GUI

### HashAPI Installation:
1. Update Enviornmental Variables shell script that HashAPI will use to run.  
Modify the set-env-vars.sh shell script included in this repository.
2. Build & run the HashAPI docker command by using the below, and inserting your values:
```
FLASK_PATH=<path_to_repository> && \
DOCKER_IMAGE=hash_api:0.1-develop && \
docker build -t $DOCKER_IMAGE $FLASK_PATH && \
  cd $FLASK_PATH && \
  source ~/path/to/set-env-vars.sh && \
  docker run -p $API_PORT:$API_PORT \
  -e HASH_MONGO_USER=$HASH_MONGO_USER \
  -e HASH_JWT_SECRET=$HASH_JWT_SECRET \
  -e HASH_MONGO_HOST=$HASH_MONGO_HOST \
  -e HASH_APP_SECRET=$HASH_APP_SECRET \
  -e HASH_API_PORT=$HASH_API_PORT \
  -e HASH_API_DEBUG=$HASH_API_DEBUG \
  -e HASH_MONGO_DB=$HASH_MONGO_DB \
  -e HASH_API_HOST=$HASH_API_HOST \
  -e HASH_MONGO_PORT=$HASH_MONGO_PORT \
  -e HASH_MONGO_PASS=$HASH_MONGO_PASS \
  -t $DOCKER_IMAGE
```
5. Create new authenticated user using instructions below.
6. Utilize the hash_cli tool (using your authenticated user credentials)
   to use specified endpoints below.

#### HashAPI Setup
Create a HashAPI user using your REST client of choice.

## HashAPI Endpoints

**Registers A New User for HashAPI**

http://127.0.0.1:8000/api/v1/users/create
* methods = POST
* POST parameters:
```
{
  "username": "exampleName",
  "password": "examplePassword"
}
```

**Authenticates an Existing User to use HashAPI**
**Returns access_token and refresh_token**
http://127.0.0.1:8000/api/v1/user/auth
- methods = POST
- POST parameters = 'username','password'
```
{
  "username": "exampleName",
  "password": "examplePassword"
}
```

**Store Hash Value of File Contents**
http://127.0.0.1:8000/api/v1/events/create
- methods = POST
- POST parameters = 'abspath', 'filename', 'hashvalue'
#### This method is best utilized with hash_cli

**Refreshes access_token and refresh_token**
http://127.0.0.1:8000/api/v1/token/refresh
- methods = POST
- Bearer refresh_token required

**Logs User Out of HashAPI**
http://127.0.0.1:8000/api/v1/user/logout
- methods = DELETE
- Bearer access_token required
