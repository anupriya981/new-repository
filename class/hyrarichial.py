class A:
    def insta(self):
        print('insta')
class B:
    def fb(self):
        print('fb')
class C(A,B):
    def titwer(self):
        print('twiter')
tottal=C()
tottal.insta()
tottal.fb()
tottal.titwer()
