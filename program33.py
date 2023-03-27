class Math:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


m = Math()
print(m.add(1, 2)) 
print(m.add(1, 2, 3))
