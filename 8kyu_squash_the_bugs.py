def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i = 0

    while (i < len(spl)):
        if (len(spl[i]) >= longest):
            longest = len(spl[i])
        i += 1

    return longest


# print(find_longest("Basic tests"))
print(find_longest("The quick white fox jumped around the massive dog"))
print(find_longest("Take me to tinseltown with you"))
print(find_longest("Sausage chops"))
print(find_longest("Wind your body and wiggle your belly"))
print(find_longest("Lets all go on holiday"))
