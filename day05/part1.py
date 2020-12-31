data = open("input.txt").read().split("\n")

nice = 0


def naughty_or_nice(kid):
    vowel_count = 0
    for l in ["a", "e", "i", "o", "u"]:
        tmp_count = kid.count(l)
        vowel_count += tmp_count
    if vowel_count >= 3:
        double = False
        for n, letter in enumerate(kid):
            if n == len(kid) - 1:
                break
            elif letter == kid[n + 1]:
                double = True
                break
    else:
        return False
    if double == True:
        for lett in ["ab", "cd", "pq", "xy"]:
            if lett in row:
                return False
    else:
        return False
    return True

for row in data:
    if naughty_or_nice(row) == True:
        nice += 1

print(nice)
""" 
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements. """

#438 too high
#174 too low