# Define the flask configuration settings.
APP_SECRET="<application_secret>"
API_PORT=<port_you_wish_api_to_use>
API_DEBUG=<true_or_false>
API_HOST="0.0.0.0"
API_LOG="<path_to_your_log_file>"

# Define the MongoDB credentials and configuration settings.
MONGO_USER="<MongoDB_username>"
MONGO_DB="hashdb"
MONGO_HOST="<IP_Address_of_MongoDB_host>"
MONGO_PORT=27017 <-----27017 is default port for MongoDB
MONGO_PASS="<MongoDB_password"

# Define the JWT secret.
JWT_SECRET="<auth_secret>"

# Set Enviornmental Variables
export HASH_MONGO_USER=$MONGO_USER
export HASH_JWT_SECRET=$JWT_SECRET
export HASH_MONGO_HOST=$MONGO_HOST
export HASH_APP_SECRET=$APP_SECRET
export HASH_API_PORT=$API_PORT
export HASH_API_DEBUG=$API_DEBUG
export HASH_MONGO_DB=$MONGO_DB
export HASH_API_HOST=$API_HOST
export HASH_MONGO_PORT=$MONGO_PORT
export HASH_MONGO_PASS=$MONGO_PASS
export HASH_API_LOG=$API_LOG
