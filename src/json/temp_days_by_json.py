import json

with open('days_and_temp.json') as temp_file:
    data = json.load(temp_file)
    json_formatted_str = json.dumps(data, indent=2)
    print(json_formatted_str)

    '''
    in python when ever you want to access the json object properties use the brackets operator
    '''
    data_for_week_array = data["tempForWeek"]
    data_for_monday = data_for_week_array[0]

    print(data_for_monday["morning"])
    print(data_for_monday["afternoon"])
