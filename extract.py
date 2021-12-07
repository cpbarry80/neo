"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach



def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path) as f:
        reader = csv.reader(f)
        for line in reader:
            designation = line[3]
            name = line[4]
            diameter = line[15]
            hazardous = ''
            new_inst  = NearEarthObject(designation=designation, name=name, diameter=diameter, hazardous=hazardous)
            neos.append(new_inst)
    return neos


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, "r") as f:
        reader = json.load(f)
        reader = [dict(zip(reader["fields"], data)) for data in reader["data"]]
        approaches = []
        for line in reader:
            try:
                designation=line["des"],
                diameter=line["h"]
                time=line["cd"],
                distance=line["dist"],
                velocity=line["v_rel"]
                approach = CloseApproach(designation=designation, calendar_date=time, distance=distance, velocity=velocity)
            except Exception as e:
                print(e)
            else:
                approaches.append(approach)    
    return approaches


load_approaches()