def in_memory_database(queries):
    database = {}

    def set_or_inc(key, field, value):
        if key not in database:
            database[key] = {}

        if field not in database[key]:
            database[key][field] = 0

        database[key][field] += int(value)
        return str(database[key][field])

    def get(key, field):
        if key in database and field in database[key]:
            return str(database[key][field])
        else:
            return ""

    def delete(key, field):
        if key in database and field in database[key]:
            del database[key][field]
            if not database[key]:
                del database[key]
            return "true"
        else:
            return "false"

    output = []
    
    for query in queries:
        operation = query[0]

        if operation == "SET_OR_INC":
            key, field, value = query[1], query[2], query[3]
            result = set_or_inc(key, field, value)
            output.append(result)

        elif operation == "GET":
            key, field = query[1], query[2]
            result = get(key, field)
            output.append(result)

        elif operation == "DELETE":
            key, field = query[1], query[2]
            result = delete(key, field)
            output.append(result)

    return output

# Example usage:
queries = [
    ["SET_OR_INC", "A", "B", "5"],
    ["SET_OR_INC", "A", "B", "6"],
    ["GET", "A", "B"],
    ["GET", "A", "C"],
    ["DELETE", "A", "B"],
    ["DELETE", "A", "C"]
]

result = in_memory_database(queries)
print(result)
