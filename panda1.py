class Test():
    def main():
        a="test"
        print(a)
class B(Test):
    pass
class C(B):
    pass
obj = D(C)
D.main()