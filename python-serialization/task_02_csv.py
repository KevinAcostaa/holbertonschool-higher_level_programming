#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename: str):
    data = []
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_r = csv.DictReader(csv_file)
            for a in csv_r:
                data.append(a)
    except FileNotFoundError:
        return False

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    return True
