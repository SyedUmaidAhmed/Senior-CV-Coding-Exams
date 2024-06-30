def letter_combinations(digits: str):
    # Return an empty list if the input string is empty
    if not digits:
        return []
    
    # Mapping of digits to corresponding letters
    phone_mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Function to backtrack and generate combinations
    def backtrack(index, path):
        # If the path is the same length as digits, we have a complete combination
        if index == len(digits):
            combinations.append("".join(path))
            return
        
        # Get the letters corresponding to the current digit
        possible_letters = phone_mapping[digits[index]]
        
        # Loop through the letters and recursively build the combinations
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    combinations = []
    backtrack(0, [])
    return combinations

# Example usage:
input_digits = "23"
print(letter_combinations(input_digits))
