import wikipediaapi


def get_wikipedia_page(topic):
    wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
    # Fetch pages related to the input topic
    topic_page = wiki_wiki.page(topic)
    categorymembers = topic_page.categorymembers
    print(categorymembers)

# def get_wikipedia_pages(topic):
#     wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
 
#     page_py = wiki_wiki.page(topic)
 
#     if not page_py.exists():
#         print(f"Wikipedia page for '{topic}' does not exist.")
#         return []
 
#     links = page_py.links
 
#     related_pages = list(links.keys())[:10]
 
#     return related_pages

# def get_page_content(topic):
#     wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

#     page_py = wiki_wiki.page(topic)
    

#     if not page_py.exists():
#         print(f"Wikipedia page for '{topic}' does not exist.")
#         return ""

    
#     print(page_py.summary)
  

   # Display the contents of the top 10 related pages


def main():
    
    
    # Input the topic of your choice
    # topic = input("Enter the topic: ")
    get_wikipedia_page("Category:Cricket")
    # Get the top 10 related Wikipedia pages
    # related_pages = get_wikipedia_pages(topic)
    
       # Display the contents of the top 10 related pages
    # for page_title in related_pages:
    #     print(f"\nContent for '{page_title}':\n")
        
    #     get_page_content(page_title)

if __name__ == "__main__":
    main()
