# Hospital travel distance analysis for Ethiopia


## Donwload OSM data

Larger OSM datasets can be downloaded here:
https://download.geofabrik.de/

Select the .osm.pbf file of the country you want to study. 

## Prepare  OSRM
Navigate to the ./data folder where the .osm.pbf file is located and set up OSRM:

    docker run -t -dv "$PWD:/data" osrm/osrm-backend osrm-extract -p /opt/car.lua /data/ethiopia-latest.osm.pbf
    docker run -t -v "$PWD:/data" osrm/osrm-backend osrm-contract /data/ethiopia-latest.osm.pbf
    docker run -t -i -p 5000:5000 -v $PWD:/data osrm/osrm-backend osrm-routed --algorithm ch /data/ethiopia-latest.osrm
    docker run -p 9966:9966 osrm/osrm-frontend
    open 'http://127.0.0.1:9966'
    
## Facebook HRSL data
The 30m population high-resolution settlement layer for Ethiopia (in .geotiff format) can be downloaded [here](https://data.humdata.org/organization/facebook?q=ethiopia&ext_page_size=25).

## Hospital data
The dataset for the hospital dataset can be found [here](https://www.nature.com/articles/s41597-019-0142-2).



