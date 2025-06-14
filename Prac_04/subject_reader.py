def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read subject data from file and return as a list of [code, lecturer, students]."""
    subject_list = []
    with open(FILENAME) as input_file:
        for line in input_file:
            parts = line.strip().split(',')  # ['CP1401', 'Ada Lovelace', '192']
            parts[2] = int(parts[2])  # convert number of students from str to int
            subject_list.append(parts)
    return subject_list


def display_subject_details(subjects):
    """Print each subject's details in a formatted sentence."""
    for subject in subjects:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")


main()