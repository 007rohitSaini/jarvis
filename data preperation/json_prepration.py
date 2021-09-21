import json

def write_json(new_data, filename='final_intends.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["intents"].append(new_data)
        file.seek(0)
        json.dump(file_data, file)


with open("intends.json", "r+") as input:
    y = json.load(input)
    for converstion in y["conversations"]:
        data = {
            "patterns": [converstion[0]],
            "responses": [converstion[1]]
        }
        write_json(data)