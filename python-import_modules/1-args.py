import sys

argv = sys.argv[1:]

num_args = len(argv)

num_args_format = "{} arguments{}"
arg_format = "{}: {}"

if __name__ == "__main__":
    if num_args == 0:
        print(num_args_format.format(num_args, "."))
        print(".")
    else:
        print(num_args_format.format(num_args, ":" if num_args > 1 else ""))

        for i, arg in enumerate(argv, start=1):
            print(arg_format.format(i, arg))
