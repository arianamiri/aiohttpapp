FROM postgres:10

# this script will get run on container start up
# it sets up the concierge db and user
COPY ./init-concierge-db.sh /docker-entrypoint-initdb.d/init-concierge-db.sh
