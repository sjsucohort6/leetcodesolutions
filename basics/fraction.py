
class Fraction():
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def gcd(self,m,n):
        """
        
        """
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n
    
    def gcd_rec(self,m,n):
        remainder = m%n

        if remainder == 0:
            return n

        return self.gcd_rec(n, remainder)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den*other_fraction.num
        new_den = self.den* other_fraction.den
        common = self.gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
    
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


    
def main():
    f = Fraction(1,4)
    f2 = Fraction(1,2)
    f3 = f + f2
    print(f3)

    print(f.gcd(20,30))
    print(f.gcd_rec(20,30))

if __name__ == "__main__":
    main()