import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('foo', nargs='?', help="name of the employee")
    print(parser.parse_args().foo)