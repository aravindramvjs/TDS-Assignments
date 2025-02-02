import json

data = [{"name":"Alice","age":72},{"name":"Bob","age":95},{"name":"Charlie","age":96},{"name":"David","age":52},{"name":"Emma","age":48},{"name":"Frank","age":79},{"name":"Grace","age":46},{"name":"Henry","age":34},{"name":"Ivy","age":51},{"name":"Jack","age":64},{"name":"Karen","age":89},{"name":"Liam","age":31},{"name":"Mary","age":74},{"name":"Nora","age":83},{"name":"Oscar","age":81},{"name":"Paul","age":93}]


sorted_data = sorted(data, key=lambda x: x["age"])
print(json.dumps(sorted_data, indent=4))

result_data = [
    {
        "name": "Liam",
        "age": 31
    },
    {
        "name": "Henry",
        "age": 34
    },
    {
        "name": "Grace",
        "age": 46
    },
    {
        "name": "Emma",
        "age": 48
    },
    {
        "name": "Ivy",
        "age": 51
    },
    {
        "name": "David",
        "age": 52
    },
    {
        "name": "Jack",
        "age": 64
    },
    {
        "name": "Alice",
        "age": 72
    },
    {
        "name": "Mary",
        "age": 74
    },
    {
        "name": "Frank",
        "age": 79
    },
    {
        "name": "Oscar",
        "age": 81
    },
    {
        "name": "Nora",
        "age": 83
    },
    {
        "name": "Karen",
        "age": 89
    },
    {
        "name": "Paul",
        "age": 93
    },
    {
        "name": "Bob",
        "age": 95
    },
    {
        "name": "Charlie",
        "age": 96
    }
]