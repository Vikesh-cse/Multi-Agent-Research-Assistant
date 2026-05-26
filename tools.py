from langchain_groq import ChatGroq
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
from dotenv import load_dotenv
from rich import print

load_dotenv()

tavily  = TavilyClient()

@tool
def web_search(query : str) -> str :
    """Search the web for resent and reliable information . Return Titles , URL and snippets ."""
    results = tavily.search(query=query,max_results=5)
    
    output  = []
    for r in results['results']:
       output.append(
            f"""Title: {r['title']} \n URL: {r['url']}\n Snippet :{r['content'][:300]}\r"""
        )
       
    return "/n-----/n".join(output)




@tool
def scrape_url(url: str) -> str:
    """
    Scrape and return clean text content from a given URL for deeper reading.
    """
    try:
        resp = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
            
        return soup.get_text(
            separator=" ",
            strip=True
        )[:3000]

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
       
   
    