def minion_game(string):
    vowels = {"A", "E", "I", "O", "U"}
    stuart = 0
    kevin = 0
    string_len = len(s)
    for i in range(string_len):
        if s[i] in vowels:
            kevin += string_len - i
        else:
            stuart += string_len - i

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)


# ##### =========================  Explanation =========================
# The current implementation of the Minion Game has a nested loop that generates all possible substrings, which leads to a time complexity of O(n²). This is inefficient for large strings.

# Optimized Approach:
# Instead of generating all substrings, count how many substrings start with each character.

# Kevin's score: Add the number of substrings starting with vowels.
# Stuart's score: Add the number of substrings starting with consonants.
# Each character at position i forms n - i substrings where n is the length of the string. Therefore, the scoring can be done in O(n).

# Optimized Code:
# python
# Copy code
# def minion_game(s):
#     vowels = {"A", "E", "I", "O", "U"}
#     stuart = 0
#     kevin = 0
#     string_len = len(s)

#     for i in range(string_len):
#         if s[i] in vowels:
#             kevin += string_len - i  # All substrings starting at index i
#         else:
#             stuart += string_len - i

#     if stuart > kevin:
#         print(f"Stuart {stuart}")
#     elif stuart < kevin:
#         print(f"Kevin {kevin}")
#     else:
#         print("Draw")

# if __name__ == "__main__":
#     s = input().strip()  # Ensure no extra spaces
#     minion_game(s)

# Explanation of Optimizations:
# Let me explain Substring Counting in detail with a clear breakdown of how it works and why it optimizes the solution.

# Core Idea of Substring Counting:
# For a string s of length n, if you are at position i, the number of substrings starting from s[i] is:

# Substrings starting at 𝑖 = 𝑛 − 𝑖

# Example: If s = "BANANA", n = 6.
# For i = 0 (B), substrings: BANANA, BANAN, BANA, BAN, BA, B → 6 substrings.
# For i = 1 (A), substrings: ANANA, ANAN, ANA, AN, A → 5 substrings.
# For i = 2 (N), substrings: NANA, NAN, NA, N → 4 substrings.
# Thus, the number of substrings starting at i is simply n - i.

# Step-by-Step Walkthrough:
# Consider s = "BANANA" (n = 6):

# Index (i)	Character	Substrings Count (n - i)	Player (Vowel/Consonant)
# 0	B	6	Stuart (consonant)
# 1	A	5	Kevin (vowel)
# 2	N	4	Stuart (consonant)
# 3	A	3	Kevin (vowel)
# 4	N	2	Stuart (consonant)
# 5	A	1	Kevin (vowel)
# Calculation:
# Kevin's Score (Vowels):

# Kevin scores when the character at i is a vowel.
# Sum substrings starting with vowels:
# A at index 1 → 5 points (n - 1)
# A at index 3 → 3 points (n - 3)
# A at index 5 → 1 point (n - 5)
# Kevin's Total: 5 + 3 + 1 = 9

# Stuart's Score (Consonants):

# Stuart scores when the character at i is a consonant.
# Sum substrings starting with consonants:
# B at index 0 → 6 points (n - 0)
# N at index 2 → 4 points (n - 2)
# N at index 4 → 2 points (n - 4)
# Stuart's Total: 6 + 4 + 2 = 12

# Conclusion:
# Stuart: 12 points
# Kevin: 9 points
# Result: "Stuart 12"

# Why This Works:
# Avoids Generating Substrings:
# Instead of generating every substring (which is time-consuming), we directly calculate how many substrings start at each position.
# Counts in Constant Time:
# Checking whether a character is a vowel/consonant is O(1).
# We loop through the string once, making it O(n).
# Time Complexity Analysis:
# Loop through the string: O(n)
# Check each character: O(1)
# Overall Time Complexity: O(n)

# Let me know if this clears it up!
