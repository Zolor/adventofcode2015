data = open("input.txt").read().split("\n")

total = 0

for gift in data:
    l, w, h = gift.split("x")
    total += 2*(int(l)*int(w)) + 2*(int(w)*int(h)) + 2*(int(h)*int(l))
    smallest_side = []
    smallest_side = min([int(l)*int(w),int(w)*int(h),int(h)*int(l)])
    total += smallest_side

print(total)