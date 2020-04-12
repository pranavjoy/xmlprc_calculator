from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(('localhost', 3000), logRequests=True)


def calculate(op, a, b):
    if op == 'add':
        return a + b
    elif op == 'diff':
        return a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        return a / b
    else:
        return "Not a valid operation"


server.register_function(calculate)


if __name__ == '__main__':
    try:
        print("Serving...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting server")