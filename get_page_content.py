import wikipediaapi

def get_page_content(topic):
    wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

    page_py = wiki_wiki.page(topic)
    

    if not page_py.exists():
        print(f"Wikipedia page for '{topic}' does not exist.")
        return ""

    
    return(page_py.summary)