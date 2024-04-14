class User:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

# Sample user data
users = [
    User("Alice", 25, "New York"),
    User("Bob", 30, "Los Angeles"),
    User("Charlie", 28, "San Francisco"),
    User("David", 32, "Chicago"),
]

def match_users(user, candidates, age_range, location):
    matches = []
    for candidate in candidates:
        if (
            user.age - age_range <= candidate.age <= user.age + age_range
            and candidate.location == location
        ):
            matches.append(candidate)
    return matches

# Example usage
user1 = User("Emily", 27, "New York")
matched_users = match_users(user1, users, age_range=3, location="New York")
for match in matched_users:
    print(match.name)
