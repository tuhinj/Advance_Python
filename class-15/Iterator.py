# 4

"tuhin"

["joy", "tuhin", "maynuddin"]

name=iter(['maliha','susmee','joy'])

# print(next(name))
# print(next(name))
# print(next(name))


# for num in [1, 2,3,4,5] range(1, 5):

class MyRange:
    def __init__(self, starting, ending):
            self.current = starting
            self.endign = ending

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.endign:
            num = self.current
            self.current += 1
            return self.current

range_of_nums = MyRange(1,5)

print(range_of_nums.current, range_of_nums.endign)

print(next(range_of_nums))



