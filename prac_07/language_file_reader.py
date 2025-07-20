from programming_language import ProgrammingLanguage

def main():
    languages = []
    with open("languages.csv", "r", encoding="utf-8") as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            typing = parts[1]
            reflection = parts[2] == "True"
            year = int(parts[3])
            pointer_arithmetic = parts[4] == "True"
            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(language)

if __name__ == '__main__':
    main()
