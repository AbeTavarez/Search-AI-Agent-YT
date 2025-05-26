from langchain_core.tools import tool
import re 
import requests
from markdownify import markdownify


@tool
def visit_website(url: str) -> str:
    """Use this tool to visit URLs obtained from the search results and extract the main content of the webpages in markdown format.
    Arg: 
        url: The url link of the webpage to visit
    """
    
    # send request
    response = requests.get(url, timeout=20)
    
    # check if request was successful
    response.raise_for_status()
    
    # convert the HTML to markdown
    markdown_content = markdownify(response.text).strip()
    
    markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)
    
    return markdown_content

# print(visit_website.invoke("https://www.apple.com"))
