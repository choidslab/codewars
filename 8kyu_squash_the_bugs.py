def find_longest(string):
    spl = string.split(" ")
    print(spl)
    longest = 0
    i = 0

    while (i > len(spl)):

        if (len(spl(i)) > longest):
            longest = len(spl[i])

    return longest


print(find_longest("Basic tests"))