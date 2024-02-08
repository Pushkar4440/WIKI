# import necessary libraries 
from flask import Flask, render_template, request
import wikipediaapi
from get_wikipedia_pages import get_wikipedia_pages
from get_page_content import get_page_content

app = Flask(__name__) 
wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

# create HOME View 
@app.route("/", methods=["POST", "GET"]) 
def home(): 
    if request.method == "GET": 
        return render_template("index.html") 
    if request.method == "POST": 
        search = request.form["search"] 
	
        result = get_wikipedia_pages(search)
        content = []
        for i in result:
            
            for j in i:
                print(j)
                content.append(get_page_content(j))
                
            # print(str(i))
            
        # print("hello" + result)
        # for page_title in result:
        #     content.append(get_page_content(page_title))
        
        combined_result = zip(result[0], content)    
        return render_template("result.html", combined_result=combined_result)

@app.route("/result", methods=["GET"]) 
def result():
    return render_template("result.html")

if __name__ == '__main__': 
    app.run(debug=True)
