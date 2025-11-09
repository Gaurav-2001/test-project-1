import random

# 1. Define the input and output filenames
input_file = "dataset.jsonl"
output_file = "dataset_shuffled.jsonl"

# 2. Read all lines (records) from the file
try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 3. Shuffle the list of lines randomly
    random.shuffle(lines)
    
    # 4. Write the shuffled lines to the new output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
        
    print(f"Successfully shuffled {len(lines)} records.")
    print(f"Shuffled data saved to: {output_file}")

except FileNotFoundError:
    print(f"Error: The input file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")