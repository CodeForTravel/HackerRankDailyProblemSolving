def make_desing_pattern(n, m):
    welcome_text = "WELCOME"
    k = 1

    # printing upper part
    for i in range(int(n / 2)):
        number_of_upper_dash = int((m - k * 3) / 2)
        for x in range(number_of_upper_dash):
            print("-", end="")

        for y in range(k):
            print(".|.", end="")

        for z in range(number_of_upper_dash):
            if z < number_of_upper_dash - 1:
                print("-", end="")
            else:
                print("-")
        k = k + 2

    # printing welcome
    number_of_middle_dash = int((m - len(welcome_text)) / 2)
    for l in range(number_of_middle_dash):
        print("-", end="")
    print(welcome_text, end="")
    for j in range(number_of_middle_dash):
        if j < number_of_middle_dash - 1:
            print("-", end="")
        else:
            print("-")

    # printing upper part
    for i in range(int(n / 2)):
        k = k - 2
        number_of_lower_dash = int((m - k * 3) / 2)
        for x in range(number_of_lower_dash):
            print("-", end="")

        for y in range(k):
            print(".|.", end="")

        for z in range(number_of_lower_dash):
            if z < number_of_lower_dash - 1:
                print("-", end="")
            else:
                print("-")


if __name__ == "__main__":
    n, m = map(int, input().split())
    make_desing_pattern(n, m)


# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---


# ----------WELCOME----------


# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------
