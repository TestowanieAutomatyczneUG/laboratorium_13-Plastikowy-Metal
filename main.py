class FizzBuzz:
    def game(self, num):
        if not isinstance(num, int):
            raise ValueError('Wrong type of argument')
        if ((num % 15) == 0):
            return "FizzBuzz"
        elif ((num % 3) == 0):
            return "Fizz"
        elif ((num % 5) == 0):
            return "Buzz"
        else:
            return "Not fizz not buzz not fizzbuzz"
