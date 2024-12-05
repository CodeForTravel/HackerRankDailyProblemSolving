# def merge_the_tools(string, k):
#     res = set()
#     for i in range(len(string)):
#         res.add(string[i])
#         if (i + 1) % k == 0:
#             print("".join(res))
#             res = set()


# def merge_the_tools(string, k):
#     for i in range(0, len(string), k):
#         string_set = set(string[i : i + k])
#         print("".join(string_set))


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # Create an empty list to store unique characters in order
        seen = []
        for char in string[i : i + k]:
            if char not in seen:
                seen.append(char)
        # Print the unique characters in the order they appeared
        print("".join(seen))


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
