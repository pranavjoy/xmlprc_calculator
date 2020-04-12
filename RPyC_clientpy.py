from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://35.222.202.92:3000")

if __name__ == '__main__':
    print("Welcome to the calculator")
    print("You can choose between add, diff, multiply and divide")
    while True:
        op = input("Choose a function: ").lower()
        if op == 'add' or op == 'diff' or op == 'multiply' or op == 'divide':
            numbers = input("Enter two numbers seperated by space: ")
            a = int(numbers.split(" ")[0])
            b = int(numbers.split(" ")[1])
            print(proxy.calculate(op, a, b))
        else:
            print("Not a valid operation")
