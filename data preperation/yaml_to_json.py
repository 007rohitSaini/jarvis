import yaml
import json


with open("./archive/ai.yml", "r") as infile, open("./intends.json", "w") as outfile:
    yaml = yaml.safe_load(infile)
    json.dump(yaml, outfile)
        