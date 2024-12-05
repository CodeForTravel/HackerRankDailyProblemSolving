from collections import Counter


def shoe_purchase(number_of_shoe, shoe_sizes):
    sell = 0
    shoe_sizes_counter = Counter(shoe_sizes)
    shoe_purchase_operation = int(input())
    for i in range(shoe_purchase_operation):
        size, price = map(int, input().split())
        if shoe_sizes_counter.get(size):
            sell += price
            shoe_sizes_counter[size] -= 1
    print(sell)


if __name__ == "__main__":
    number_of_shoe = int(input())
    shoe_sizes = map(int, input().split())

    shoe_purchase(number_of_shoe, shoe_sizes)
