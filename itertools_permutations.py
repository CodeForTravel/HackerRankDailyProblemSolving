from itertools import permutations


def make_permutation(string, permutation_number):
    res = sorted(list(permutations(string, permutation_number)))
    for i in res:
        print("".join(i))


if __name__ == "__main__":
    # string, permutation_number = map(input().split())
    string, permutation_number = input().split()
    make_permutation(string, int(permutation_number))
