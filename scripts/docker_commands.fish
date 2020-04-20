
# for some reason, I had to use OSRM-contract instead of the usual routine. Also, we use algorithm "ch"

docker run -t -dv "$PWD:/data" osrm/osrm-backend osrm-extract -p /opt/car.lua /data/ethiopia-latest.osm.pbf

docker run -t -v "$PWD:/data" osrm/osrm-backend osrm-contract /data/ethiopia-latest.osm.pbf

docker run -t -i -p 5000:5000 -v $PWD:/data osrm/osrm-backend osrm-routed --algorithm ch /data/ethiopia-latest.osrm

docker run -p 9966:9966 osrm/osrm-frontend

open 'http://127.0.0.1:9966'
