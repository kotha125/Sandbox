import wikipedia

# Keep looping until blank input
while True:
    title = input("Enter page title: ").strip()
    if not title:
        print("Thank you.")
        break

    try:
        page = wikipedia.page(title, autosuggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)

    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)

    except wikipedia.exceptions.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')
