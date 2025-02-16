def longest_word(sentence):
    words = sentence.split()
    longest = ""
    max_length = 0
    
    for word in words:
        if len(word) > max_length:
            longest = word
            max_length = len(word)
    
    return longest

# Example usage
sentence = "I went to school and found a lunchbox in the lost and found"
print(sentence)
print(longest_word(sentence))  
