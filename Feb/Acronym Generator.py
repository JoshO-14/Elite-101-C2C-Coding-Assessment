#C2C Acronym Generator for February Coding Challenge

u_p = input("Enter a phrase to print out the acronym: ")  # Collect user input

# List of words to ignore
excluded_words = {"and", "or", "the", "of", "in", "on", "a", "to", "for"}

# Split the phrase and filter out short words
words = [word for word in u_p.split() if word.lower() not in excluded_words]

# Extract first letters, join, and uppercase
acronym = "".join(word[0] for word in words).upper()

#display the phrase and acronym
print("Your phrase is:", u_p,"\nThe acronym is:", acronym)




