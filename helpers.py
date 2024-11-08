def filter_json_data(data, fields):
    def filter_entry(entry, fields):
        if isinstance(entry, dict):
            return {
                key: filter_entry(entry[key], fields[key])
                for key in fields if key in entry
            }
        elif isinstance(entry, list):
            return [filter_entry(item, fields) for item in entry]
        else:
            return entry # Base case, end of dict/list depth

    for entry in data:
        yield filter_entry(entry, fields) # Creates the generator allowing for lazy evaluation of the JSON, better performance if data grows
