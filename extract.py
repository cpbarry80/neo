"""Extract data on near-Earth objects.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided,
at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing,
     data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, "r") as f:
        reader = csv.DictReader(f)
        neos = []
        for line in reader:
            if not line["diameter"]:
                line["diameter"] = None
            else:
                line["diameter"] = float(line["diameter"])
            if not line["name"]:
                line["name"] = None
            line["pha"] = False if line["pha"] in ["N", ""] else True
            neo = NearEarthObject(
                pdes=line["pdes"],
                name=line["name"],
                diameter=line["diameter"],
                pha=line["pha"])
            neos.append(neo)
    return neos


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file w data.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, "r") as f:
        reader = json.load(f)
        reader = [dict(zip(reader["fields"], data)) for data in reader["data"]]
        close_approaches = []
        for line in reader:
            appraoch = CloseApproach(
                designation=line["des"],
                time=line["cd"],
                distance=line["dist"],
                velocity=line["v_rel"])
            close_approaches.append(appraoch)
    return close_approaches
