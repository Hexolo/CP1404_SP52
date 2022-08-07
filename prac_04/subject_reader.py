"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject(data)


def display_subject(data):
    for line in data:
        print(f"{line[0]:2} is taught by {line[1]:2} and has {line[2]:2}")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        list.append(subject_details, parts)
    input_file.close()
    return subject_details


main()
