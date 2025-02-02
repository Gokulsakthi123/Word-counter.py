import string

def preprocess_text(text):
    """
    Preprocesses the input text by removing punctuation and converting to lowercase.

    Args:
        text (str): The input text.

    Returns:
        str: The preprocessed text.
    """

    # 1. Handle Empty or Whitespace-only Input:
    if not text or not text.strip():
        return ""  # Return an empty string if the input is invalid

    # 2. Remove Punctuation:
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Convert to Lowercase:
    text = text.lower()

    return text


def count_words(text):
    """
    Counts the number of words in a preprocessed text.

    Args:
        text (str): The preprocessed text.

    Returns:
        int: The number of words.
    """

    if not text:  # Check if the preprocessed text is empty
        return 0

    words = text.split()  # Split the string into a list of words
    return len(words)


def display_results(word_count):
    """
    Displays the word count to the user.

    Args:
        word_count (int): The number of words.
    """

    if word_count == 0:
        print("\nNo words were found in the input.")
    else:
        print(f"\nWord Count: {word_count}")


def get_user_input():
    """
    Prompts the user to enter text and handles the 'exit' command.

    Returns:
        str: The user's input text, or None if the user enters 'exit'.
    """

    while True:
        text = input("\nEnter your text (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            return None  # Signal to exit the program
        return text  # Return the input text


def main():
    """
    Main function to orchestrate the word counting process.
    """

    print("\nWelcome to the Word Counter Program!")
    print("====================================\n")  # Added a separator for clarity

    while True:
        user_input = get_user_input()

        if user_input is None:  # Check if the user wants to exit
            break

        preprocessed_text = preprocess_text(user_input)  # Preprocess the input
        word_count = count_words(preprocessed_text)  # Count the words
        display_results(word_count)  # Display the results


if _name_ == "_main_":
    main()