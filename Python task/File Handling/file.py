def count_words(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            content = file.read()
            word_count = len(content.split())

        with open(output_file, "w") as file:
            file.write(f"Word Count: {word_count}")

        print(f"Word count has been written to {output_file}.")
    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = "input.txt"  # Path to your input file
output_file = "output.txt"  # Path to your output file

count_words(input_file, output_file)
