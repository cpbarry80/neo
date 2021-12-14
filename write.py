"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly,
    each output row corresponds to the information in a single
    close approach from the `results` stream and its associated
    near-Earth object.
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data
        should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    with open(filename, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for result in results:
            dict_appraoch = result.__dict__
            try:
                dict_appraoch["name"]
            except KeyError:
                dict_appraoch["name"] = ""
            try:
                dict_appraoch["potentially_hazardous"]
            except KeyError:
                dict_appraoch["potentially_hazardous"] = "False"
            else:
                dict_appraoch["potentially_hazardous"] = "True"
            dict_appraoch["designation"] = dict_appraoch.pop("_designation")
            dict_appraoch["velocity_km_s"] = dict_appraoch.pop("velocity")
            dict_appraoch["datetime_utc"] = dict_appraoch.pop("time")
            dict_appraoch["name"] = dict_appraoch.pop("neo")
            dict_appraoch["distance_au"] = dict_appraoch.pop("distance")
            writer.writerow(dict_appraoch)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly,
    the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data
    should be saved.
    """
    data = []
    for result in results:
        info = {**result.serialize(), **result.neo.serialize()}
        info["name"] = info["name"] if info["name"] is not None else ""
        if info["potentially_hazardous"]:
            info["potentially_hazardous"] = bool(1)
        else:
            info["potentially_hazardous"] = bool(0)
        data.append(
            {"datetime_utc": info["datetime_utc"],
                "distance_au": info["distance_au"],
                "velocity_km_s": info["velocity_km_s"],
                "neo": {
                    "designation": info["designation"],
                    "name": info["name"],
                    "diameter_km": info["diameter_km"],
                    "potentially_hazardous": info["potentially_hazardous"]
                    }})

    with open(filename, "w") as outfile:
        json.dump(data, outfile, indent="\t")
