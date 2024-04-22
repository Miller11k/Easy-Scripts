import os

parent_directory = "Setup Scripts"

directories = [
    "01 Update And Upgrade",
    "02 Pre-Tasks",
    "03 Install and Delete Applications",
    "04 Configure Applications",
    "05 Post-Tasks",
    "06 End Step"
]

# Add the parent directory if needed
if(not os.path.exists(parent_directory)):
    os.mkdir(parent_directory)

# Add the proper directories as needed
for directory in directories:
    test_directory = os.path.join(parent_directory, directory)  # Prepend the parent directory to the directory
    if(not os.path.exists(test_directory)):
        os.mkdir(test_directory)
