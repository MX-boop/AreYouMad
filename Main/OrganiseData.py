import csv
import os

# Define the input CSV file and output directory
csv_file = 'Data/train.csv'
output_directory = 'OrganizedDataToxic'

# Create output directories if they don't exist
for label in ["0", "1"]:
    os.makedirs(os.path.join(output_directory, label), exist_ok=True)

# Read the CSV file and organize the messages
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        id = row['id']
        identity_hate = int(row['toxic'])
        comment_text = row['comment_text']

        # Create a subdirectory based on the "identity_hate" label
        subdirectory = os.path.join(output_directory, str(identity_hate))

        # Create a text file with the comment text
        with open(os.path.join(subdirectory, f"{id}.txt"), 'w') as text_file:
            text_file.write(comment_text)

print("Organized the messages into folders based on 'toxic' factor.")