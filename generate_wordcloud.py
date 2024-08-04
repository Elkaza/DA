import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# List of words to include in the word cloud with specific formatting
words = [
    "Agile", "Scrum", "Lean", "Kanban", "Waterfall", "DevOps",
    "TOGAF", "ITIL", "COBIT", "Prince2", "SAFE", "AgilePM",
    "JIRA", "Confluence", "Trello", "Slack", "GitHub", "GitLab",
    "Cloud Computing", "Big Data", "AI", "IoT", "Blockchain", "Cybersecurity",
    "Digital Transformation", "Industry 4.0", "Smart Factory", "Digitalization",
    "Change Management", "Strategy", "Innovation", "Process Engineering",
    "Data Analytics", "Machine Learning", "Robotic Process Automation",
    "ERP Systems", "CRM Systems", "Business Intelligence", "Enterprise Architecture",
    "API Management", "Microservices", "Containerization", "Kubernetes", "Docker",
    "Continuous Integration", "Continuous Delivery", "Automation", "IT Governance",
    "Risk Management", "Compliance", "Business Continuity", "Disaster Recovery"
]

# Create a dictionary with the words and their relative frequencies
word_freq = {word: 1 for word in words}
word_freq["Digital Transformation"] = 5  # Increase frequency for larger size
word_freq["Change"] = 5  # Increase frequency for larger size

# Define the colors for specific words
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    if word in ["Digital Transformation", "Change"]:
        return "red" if word == "Digital Transformation" else "blue"
    return "black"

# Create the word cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    color_func=color_func,
    stopwords=STOPWORDS
).generate_from_frequencies(word_freq)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title(' Methods, Frameworks, and Technologies')
plt.savefig('wordcloud.png')
plt.show()
