"""
Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]
"""

def reverse_seq(n):
    result = [x for x in range(n, 0, -1)]
    return result

if __name__ == "__main__":
    input_data = int(input())
    print(reverse_seq(input_data))