# use this to convert Python objects into JSON strings
import json
# a Python object (dict):
x = {
  "name": "John",
    "age": 30,
    "city": "Los Angeles"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# parse JSON back into a Python dictionary:
z = json.loads(y)
print(z["name"])


# use indent() to format the output (only in dumps)
# json.dumps(x, indent=4)

# use separators to change the default separators (only in dumps)
# json.dumps(x, indent=4, separators=(". ", " = "))

# use sort_keys to sort the result alphabetically by key (only in dumps)
# json.dumps(x, indent=4, sort_keys=True)