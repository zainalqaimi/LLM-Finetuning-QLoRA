import os
import pandas as pd
import ast

df = pd.read_csv("code_problems_dataset.csv")

dir1 = "./description2code_current/codeforces/_tags.txt"
dir2 = "./description2code_current/hackerearth/_tags.txt"

with open(dir1, "r") as tags_file:
    tags_content = tags_file.read().splitlines()
    tags_list1 = [ast.literal_eval(tag) for tag in tags_content]

with open(dir2, "r") as tags_file:
    tags_content = tags_file.read().splitlines()
    tags_list2 = [ast.literal_eval(tag) for tag in tags_content]

tags_list = tags_list1 + tags_list2
# print(tags_list[:5])
# Create a dictionary to map Challenge Names to tags
tags_dict = {}
for tag_entry in tags_list:
    for key, value in tag_entry.items():
        tags_dict[key] = value

# Add a 'tags' column to the combined_df based on the Challenge Name
df['tags'] = df['Challenge Name'].map(tags_dict)
# print(df.info())
# print(df.head(10))
print(tags_dict)
# df.to_csv("code_problems_dataset.csv")