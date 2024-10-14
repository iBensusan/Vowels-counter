# Function to count vowels in a string
def coun_vowels(text):
    vowels = set("aeiou")  # Using a set for faster checks
    return sum(1 for char in text.lower() if char in vowels)

# Input by user
text = input("Write here: ")

# Count and show the result
vowel_count = coun_vowels(text)
print(f"The number of vowels in the string is: {vowel_count}")