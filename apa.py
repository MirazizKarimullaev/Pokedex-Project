users = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
        {"name": "Charlie", "role": "admin"},
        {"name": "David",},
        {"name": "Eve", "role": "moderator"}
]
x= "no"
for user in users:
    try:
        if user["role"] == "admin":
            print(user["name"])
    except:
        x="sad"

