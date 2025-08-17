# Words Calculator:

# Ask the user for the file path
path = input("Enter the file path: ")

# Replace backslashes with forward slashes to avoid escape sequence issues (\t, \n, etc.)
path = path.replace('\\', "/")

# Remove extra quotes in case the user pastes the path wrapped in "..."
path = path.replace('"', "")

try:
    # Try opening the file in read mode
    with open(path, 'r') as file:
        # Read the entire file into a string
        txt = file.read()
        
        # Split text into words (default splits on whitespace)
        txt2 = txt.split()
        
        # Print the word count
        print(f"Word Count: {len(txt2)}")
        print("-------------------\n")
        
        # Print the full text content
        print("Text:\n-------------------")
        print(txt)

# Handle error if file is not found at the given path
except FileNotFoundError:
    print("❌ File not found. Please check the path and try again.")

# Catch any other unexpected errors
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
