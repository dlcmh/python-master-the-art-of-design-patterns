class Point:
    # self is a reference to the object the method is being invoked on
    def reset(self):
        self.x = 0
        self.y = 0

# Alternative #1 - Call method on object
p = Point()
p.reset()
print(p.x, p.y) # 0 0

# Alternative #2 - Invoke function on the class, and pass the object as the
# self argument
q = Point()
Point.reset(q)
print(q.x, q.y) # 0 0
