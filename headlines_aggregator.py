import requests  # Import the requests library to make HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML content

# Define the headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

def get_cnn_headlines():
    # URL of the CNN homepage
    url = "https://www.cnn.com"
    
    try:
        # Send a GET request to the URL with the specified headers
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Initialize an empty list to store headlines
        headlines = []
        
        # Find all headline elements on the page with the specified class
        for item in soup.find_all('h3', class_='cd__headline'):
            # Extract the text from each headline and add it to the list
            headlines.append(item.get_text(strip=True))
        
        return headlines  # Return the list of CNN headlines
    except requests.exceptions.RequestException as e:
        print(f"Error fetching CNN headlines: {e}")
        return []

def get_bbc_headlines():
    # URL of the BBC News homepage
    url = "https://www.bbc.com/news"
    
    try:
        # Send a GET request to the URL with the specified headers
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Initialize an empty list to store headlines
        headlines = []
        
        # Find all headline elements on the page (no specific class used)
        for item in soup.find_all('h3'):
            # Extract the text from each headline and add it to the list
            headlines.append(item.get_text(strip=True))
        
        return headlines  # Return the list of BBC headlines
    except requests.exceptions.RequestException as e:
        print(f"Error fetching BBC headlines: {e}")
        return []

def get_reuters_headlines():
    # URL of the Reuters homepage
    url = "https://www.reuters.com"
    
    try:
        # Send a GET request to the URL with the specified headers
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Initialize an empty list to store headlines
        headlines = []
        
        # Find all headline elements on the page with the specified class
        for item in soup.find_all('h3', class_='MediaStoryHeadlines'):
            # Extract the text from each headline and add it to the list
            headlines.append(item.get_text(strip=True))
        
        return headlines  # Return the list of Reuters headlines
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Reuters headlines: {e}")
        return []

def aggregate_headlines():
    # Create a dictionary to hold headlines from different sources
    all_headlines = {
        "CNN": get_cnn_headlines(),  # Get CNN headlines
        "BBC": get_bbc_headlines(),  # Get BBC headlines
        "Reuters": get_reuters_headlines()  # Get Reuters headlines
    }
    
    return all_headlines  # Return the dictionary of all headlines

if __name__ == "__main__":
    # Call the aggregate_headlines function to get headlines from all sources
    headlines = aggregate_headlines()
    
    # Print the headlines for each news source
    for source, news_headlines in headlines.items():
        print(f"\n{source} Headlines:")  # Print the source name
        for headline in news_headlines:
            print(f"- {headline}")  # Print each headline
