import os
import logging
from covid19.utils import download_pop_data
from pathlib import Path

if __name__ == "__main__":

    # download OSM data (not there yet) and and setup osrm docker

    # download pop data
    pop_density_url = "https://data.humdata.org/dataset/80d0519e-0eaf-4c16-a16c-a10ca837a463/resource/fc271559-23ad-4d93-90f3-215d44ce0193/download/population_esp_2019-07-01_geotiff.zip"

    location = 'asturias'
    data_folder = Path('.') / 'data' / location

    download_pop_data(pop_density_url,data_folder, location)

    # create grid

    # put into geopandas

    # prepare hospital data

