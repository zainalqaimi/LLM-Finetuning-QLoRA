import pandas as pd

def convert_to_format(row):
    description = str(row['Description'])
    solution = str(row['Solution'])
    prompt = """Below is an instruction that describes a task paired with input that provides further context. Write a response that appropriately completes the request."""
    instruction = """ Given the following coding challenge, your job is to write the solution in the Python coding language. Take a deep breath and think about the problem step-by-step. """

    if len(description.strip()) == 0:  #  prompt + 2 new lines + ###instruction + new line + input + new line + ###response
        text = prompt + "\n\n### Instruction:\n" + instruction + "\n### Response:\n" + solution
    else:
        text = prompt + "\n\n### Instruction:\n" + instruction + "\n\n### Input:\n" + description + "\n" + "\n### Response:\n" + solution
    
    # we need 4 columns for auto train, instruction, input, output, text
    return pd.Series([instruction, description, solution, text])

df = pd.read_csv("code_problems_dataset.csv")

new_df = df[['Description', 'Solution']].apply(convert_to_format, axis=1)
new_df.columns = ['instruction', 'input', 'output', 'text']

print(new_df['text'][0])

new_df.to_csv('code_alpaca_dataset.csv', index=False)


