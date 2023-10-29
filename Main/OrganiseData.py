import csv
import os

# Get the directory of the current script
script_directory = os.path.dirname(__file__)

# Define the input CSV file and output directory relative to the script's location
csv_file = os.path.join(script_directory, 'Data/train.csv')
output_directory = os.path.join(script_directory, 'OrganizedDataToxic')

# Create output directories if they don't exist
for label in ["0", "1"]:
    os.makedirs(os.path.join(output_directory, label), exist_ok=True)

# Read the CSV file and organize the messages
with open(csv_file, 'r', encoding='utf-8') as file:  # Specify 'utf-8' encoding
    reader = csv.DictReader(file)
    for row in reader:
        id = row['id']
        identity_hate = int(row['toxic'])
        comment_text = row['comment_text']

        # Create a subdirectory based on the "identity_hate" label
        subdirectory = os.path.join(output_directory, str(identity_hate))

        # Create a text file with the comment text
        with open(os.path.join(subdirectory, f"{id}.txt"), 'w', encoding='utf-8') as text_file:  # Specify 'utf-8' encoding
            text_file.write(comment_text)

print("Organized the messages into folders based on 'toxic' factor.")