# From 50 days of Python Challenge book
import pandas as pd

data = {'year': [2009, 2002, 2009, 2010, 2009],
        'Title': ['Brothers', 'Spider-Man', 'WatchMen', 'Inception', 'Avatar'],
        'genre': ['Drama', 'Sci-fi', 'Drama', 'Sci-fi', 'Fantasy']}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
# print(df.to_string(index=False))

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
dfs = pd.read_html(url)
# print(dfs[1][['Type', 'Mutability']])
