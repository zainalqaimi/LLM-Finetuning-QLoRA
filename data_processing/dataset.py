import os
import pandas as pd

def process_directories(root_dir):
    data = []  # List to store individual data points

    competition = root_dir.split("/")[-3]  # Get the second-to-last element


    for dir_name in os.listdir(root_dir):
        root_path = os.path.join(root_dir, dir_name)

        # Check if the item in the root directory is a directory (skip files)
        if os.path.isdir(root_path):
            description_dir = os.path.join(root_path, 'description')
            solutions_dir = os.path.join(root_path, 'solutions_python')

            # Check if both 'description' and 'solutions_python' subdirectories exist
            if os.path.exists(description_dir) and os.path.exists(solutions_dir):
                description_file = os.path.join(description_dir, 'description_annotated.txt')

                # Process 'description_annotated.txt'
                if os.path.exists(description_file):
                    with open(description_file, "r") as description_text_file:
                        description_content = description_text_file.read()

                    # Process each '.txt' file in 'solutions_python' directory
                    for solution_file in os.listdir(solutions_dir):
                        if solution_file.endswith(".txt"):
                            solution_file_path = os.path.join(solutions_dir, solution_file)
                            with open(solution_file_path, "r") as solution_text_file:
                                solution_content = solution_text_file.read()

                            # Append a data point as a tuple to the data list
                            data.append((competition, dir_name, description_content, solution_content))

    df = pd.DataFrame(data, columns=["Dataset", "Challenge Name", "Description", "Solution"])
    csv_file_name = f"{competition}_college.csv"
    # Write the DataFrame to the CSV file
    df.to_csv(csv_file_name, index=False)

    return df

# Example usage:
root_directory = "./description2code_current/hackerearth/problems_college/"
df = process_directories(root_directory)
print(df.info())
print(df.head())