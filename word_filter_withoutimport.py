def word_filter_counter(text, filter_words):
    # Convert the filter_words to lowercase for case-insensitive comparison
    filter_words_lower = [word.lower() for word in filter_words]

    # Initialize an empty dictionary to store word counts
    word_counts = {} #This will be the total amount as the answer so it will be the blank set at this time.

    # Split the text into words based on spaces
    words = text.split() #Split the text into each word 

    # Iterate through each word in the text
    for word in words:
        # Remove punctuation marks from the word
        word_cleaned = ''.join(char for char in word if char.isalnum()) #to clean the probability that it include the punctuation in the word.
        #using char.isalnum() in case that it match only the case of alphabet and numeric A-Z 0-9.

        # Convert the cleaned word to lowercase for case-insensitive comparison
        word_cleaned_lower = word_cleaned.lower() #to avoid the probability that have the problem with the 

        # Check if the cleaned word is in the filter_words list
        if word_cleaned_lower in filter_words_lower:
            # Update the word count in the dictionary
            word_counts[word_cleaned_lower] = word_counts.get(word_cleaned_lower, 0) + 1

    return word_counts

print(word_filter_counter("Hello world, hello!", ["hello"]))
print(word_filter_counter("The quick brown fox.", ["the"]))
print(word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]))  
print(word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"])) 