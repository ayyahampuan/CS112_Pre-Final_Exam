print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: Ayyah M. Ampuan")
def prime(res):
    if res < 2:
        return False
    for i in range(2, int(res ** 0.5) + 1):
        if res % i == 0:
            return False
    return True

while True:
    start_num = int(input("\nEnter a number (start): "))

    if start_num < 0:
        print("Enter a non-negative number.")
        continue

    if start_num == 0:
        print("Program terminated.")
        break

    end_num = int(input("Enter a number (end): "))

    if end_num <= start_num:
        print("Enter a number greater than number", start_num)
        continue

    print("Prime numbers between", start_num, "to", end_num, "are:")
    for res in range(start_num, end_num):
        if prime(res):
            print(res, end=' ')
