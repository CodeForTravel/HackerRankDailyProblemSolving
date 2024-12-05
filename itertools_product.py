from itertools import product


def make_product(A, B):
    result = list(product(A, B))
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    A = map(int, input().split())
    B = map(int, input().split())
    make_product(A, B)
