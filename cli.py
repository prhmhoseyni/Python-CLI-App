import sys
from termcolor import colored
from python_cli_app import setup, utils
from python_cli_app.commands import cat, cd, cp, find, ls, mkdir, mv, rm, rmdir


def main():

    # Setup the parser
    parser = setup.setup_argparse()

    # Parse command line arguments
    args = parser.parse_args()

    # Log command
    utils.log_command()

    # Run command
    if args.ls:
        
        path = args.ls
        
        ls.run(path)

    elif args.cd:
    
        path = args.cd
        
        cd.run(path)

    elif args.mkdir:

        ...

    elif args.rmdir:

        ...

    elif args.rm:

        ...

    elif args.rm:

        ...

    elif args.cp:

        ...

    elif args.mv:

        source, destination = args.mv

        mv.run(source, destination)

    elif args.find:

        ...

    elif args.cat:

        ...

    else:

        print(colored("Command Not Found!", "red"))


if __name__ == "__main__":

    main()
