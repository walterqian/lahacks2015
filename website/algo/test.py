import currency
import match

def main():
    x = match.User(1,0,0,0)
    y = match.User(2,0,0,0)
    z = match.User(3,0,0,0)
        
    x.regular = 25
    y.regular = 25
    z.regular = 25
        
    x.nextUser = y
    y.nextUser = z
    z.prevUser = y
    y.prevUser = x

    currency.priceSaved(z)

    print x.savings
    print y.savings
    print z.savings

if __name__ == '__main__':
   main()

