class Difference:
    def __init__(self, a):
        self.__elements = a

    def computedifference(self):
        sorted_elements = sorted(self.__elements)
        self.maximumdifference = abs(sorted_elements[-1] - sorted_elements[0])


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computedifference()

print(d.maximumdifference)
