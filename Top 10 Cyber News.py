import requests
import json

# NewsAPI endpoint and API key
endpoint = "https://newsapi.org/v2/top-headlines"
api_key = "<API Key>" # Replace with your own API key

# Parameters for the API request
params = {
    "q": "cyber security",
    "category": "technology",
    "language": "en",
    "pageSize": 10,
    "apiKey": api_key
}

# Send the API request
response = requests.get(endpoint, params=params)

# Parse the response as JSON
print(json.loads(response.text))
data = json.loads(response.text)

# Check if the request was successful
if data["status"] == "ok":
    # Create a list of news articles
    articles = []

    for i, article in enumerate(data["articles"]):
        if i == 10:
            break

        articles.append(f'{i+1}. {article["title"]} ({article["url"]})')

    # Create a file to store the news list
    with open("cyber_news.txt", "w") as f:
        # Write the news list to the file
        f.write("\n".join(articles))

    # Print the news list to the console
    print("\n".join(articles))

else:
    print("Error: could not retrieve news articles")
    print(f"API Error Code: {data['code']}")
    print(f"API Error Message: {data['message']}")
