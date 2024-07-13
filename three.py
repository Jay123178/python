def longest_substring_without_repeating(s):
   
    char_index = {}
    max_len = 0 
    start = 0   
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
           
            start = char_index[s[end]] + 1
     
        char_index[s[end]] = end
     
        current_len = end - start + 1
        
      
        if current_len > max_len:
            max_len = current_len
   
    return max_len

input_str = "abcabcbb"
print("Length of the longest substring without repeating characters:", longest_substring_without_repeating(input_str))  # Output: 3
