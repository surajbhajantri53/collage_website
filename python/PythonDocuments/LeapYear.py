# List of kids (Modify this list as needed)
kids = ["John", "Emma", "Liam", "Olivia", "Noah", "Ava",
        "Sophia", "Mason", "Isabella", "Ethan", "Lucas", "Mia",
        "Charlotte", "James", "Benjamin", "Henry", "Amelia"]

# Dictionary to store class assignments
class_dict = {"Class A": [], "Class B": [], "Class C": []}

# Loop through the list and assign in a cyclic manner
for i in range(0, len(kids), 2):  # Step of 2 to take 2 kids at a time
    if (i // 2) % 3 == 0:
        class_dict["Class A"].extend(kids[i:i+2])  # Assign 2 kids to Class A
    elif (i // 2) % 3 == 1:
        class_dict["Class B"].extend(kids[i:i+2])  # Assign 2 kids to Class B
    else:
        class_dict["Class C"].extend(kids[i:i+2])  # Assign 2 kids to Class C

# Print the class assignments
for class_name, students in class_dict.items():
    print(class_name, ":", students)
