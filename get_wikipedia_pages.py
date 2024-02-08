import wikipediaapi

def get_wikipedia_pages(topic):
    wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
    # Fetch pages related to the input topic
    topic_page = wiki_wiki.page("Category:"+topic)
    categorymembers = topic_page.categorymembers
    
     
    # Rank pages based on the length of their content
    # ranked_pages = sorted(categorymembers.values(), key=lambda x: len(x.text), reverse=True)
    # ranked_pages = categorymembers.values()
    pages = []
    for c in categorymembers.values():
        pages.append(c.title)
    # Get titles of top 10 pages
    top_titles = [pages[:10]]
    return top_titles

  

# def get_wikipedia_pages(topic):
#     wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
    
#     related_pages = wiki_wiki.page("Category:"+topic)[:10]
    
    

 
    # page_py = wiki_wiki.page(topic)
 
    # if not page_py.exists():
    #     print(f"Wikipedia page for '{topic}' does not exist.")
    #     return []
 
    # links = page_py.links
 
    # related_pages = list(links.keys())
 
    return related_pages
