# class A:
#     def __str__(self):
#         return "A"

# class B(A):
#     def __str__(self):
#         return "B"

# class C(B):
#     def __str__(self):
#         return "C"

# def main():
#     b = B()
#     a = A()
#     c = C()
#     print(a, b, c)

# main()







class A:
    def __str__(self):
        return "A"

class B(A):
    def __str__(self):
        return "B"

class C(B):
    def __str__(self):
        return "C"

def main():
    b = B()
    a = A()
    c = C()
    print(a, b, c)

main()