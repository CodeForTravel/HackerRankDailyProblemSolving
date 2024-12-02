import string


def print_rangoli(size):
    alphabet = string.ascii_lowercase
    # Create the rows for the top half and center
    lines = []
    for i in range(size):
        left = "-".join(alphabet[size - 1 : i : -1])
        center = alphabet[i]
        right = "-".join(alphabet[i + 1 : size])
        row = (left + "-" + center + "-" + right).strip("-")
        lines.append(row.center(4 * size - 3, "-"))

    # Combine top and bottom
    for line in lines[::-1]:
        print(line)

    for line in lines[1:size:1]:
        print(line)


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
