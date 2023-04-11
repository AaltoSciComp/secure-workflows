import csv
from faker import Faker

# Create a Faker instance
fake = Faker()

# Number of individuals to generate
num_individuals = 100

# Define output CSV file
output_file = 'fake_individuals.csv'

with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Row', 'Name', 'Surname']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Generate and write 100 individuals
    for i in range(num_individuals):
        writer.writerow({
            'Row': i + 1,
            'Name': fake.first_name(),
            'Surname': fake.last_name(),
        })

print(f"{num_individuals} fake individuals saved in {output_file}")

