def longest_substring_without_repeating(s):
    # Dictionary to store the most recent index of each character
    char_index = {}
    max_len = 0  # Length of the longest substring found
    start = 0    # Starting index of current substring
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            # If s[end] is already in the substring and its index is within the current substring
            start = char_index[s[end]] + 1
        
        # Update the index of the current character
        char_index[s[end]] = end
        
        # Calculate the length of the current substring
        current_len = end - start + 1
        
        # Update max_len if we found a longer substring
        if current_len > max_len:
            max_len = current_len
    
    # Return the length of the longest substring without repeating characters
    return max_len

# Example usage:
input_str = "abcabcbb"
print("Length of the longest substring without repeating characters:", longest_substring_without_repeating(input_str))  # Output: 3
