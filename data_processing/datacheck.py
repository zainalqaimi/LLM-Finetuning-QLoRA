import pandas as pd

# Read the three CSV files into DataFrames
# codeforces_df = pd.read_csv("codeforces.csv")
# hackerearth_df = pd.read_csv("hackerearth.csv")
# hackerearth_college_df = pd.read_csv("hackerearth_college.csv")

# # Concatenate the three DataFrames vertically (along rows)
# combined_df = pd.concat([codeforces_df, hackerearth_df, hackerearth_college_df], ignore_index=True)

# # Now, combined_df contains all the rows from the three DataFrames
# combined_df.to_csv("code_problems_dataset.csv", index=False)
# print(combined_df.info())


# Assuming you have already created and populated the combined_df DataFrame

# Function to count tokens in a text
def count_tokens(text):
    # Split the text into words (tokens) using whitespace as the delimiter
    words = text.split()
    # Return the count of tokens
    return len(words)

# Apply the count_tokens function to 'Description Content' and 'Solution Content' columns
df = pd.read_csv("code_problems_dataset.csv")
df['Description Tokens'] = df['Description'].apply(count_tokens)
df['Solution Tokens'] = df['Solution'].apply(count_tokens)

# Calculate the total number of tokens for description and solution
total_description_tokens = df['Description Tokens'].sum()
total_solution_tokens = df['Solution Tokens'].sum()

# Print the total counts
print(f"Total Description Tokens: {total_description_tokens}")
print(f"Total Solution Tokens: {total_solution_tokens}")
