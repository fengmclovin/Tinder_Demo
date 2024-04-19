## Tinder Swipe Function Algorithm

### Input:
- `profiles`: List of user profiles, each containing information such as name, age, bio, etc.

### Output:
- `matches`: List of profiles that the user has swiped right on (i.e., liked).

### Algorithm Steps:
1. Initialize an empty list `matches` to store the liked profiles.
2. Loop through each profile in the `profiles` list:
   - Display the profile information to the user (name, age, bio, etc.).
   - Prompt the user for input (swipe direction).
   - If the user swipes right:
     - Add the profile to the `matches` list.
     - Display a message confirming the like.
   - If the user swipes left:
     - Display a message indicating the pass.
3. Once all profiles have been swiped, return the `matches` list containing liked profiles.

### Python Implementation:
```python
def tinder_swipe(profiles):
    matches = []
    for profile in profiles:
        display_profile(profile)
        swipe_direction = get_user_input()
        if swipe_direction == 'right':
            matches.append(profile)
            print("You liked this profile.")
        else:
            print("You passed on this profile.")
    return matches

def display_profile(profile):
    # Display profile information to the user
    print(f"Name: {profile['name']}")
    print(f"Age: {profile['age']}")
    print(f"Bio: {profile['bio']}")
    # Display other relevant information

def get_user_input():
    # Get user input for swipe direction (right/left)
    return input("Swipe right to like, left to pass: ").lower()

# Example Usage
profiles = [
    {"name": "Alice", "age": 25, "bio": "Looking for a meaningful connection."},
    {"name": "Bob", "age": 28, "bio": "Enjoys hiking and trying new foods."},
    # Add more profiles as needed
]

liked_profiles = tinder_swipe(profiles)
print("Liked Profiles:")
for profile in liked_profiles:
    print(profile["name"])
