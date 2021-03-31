import sys
from tools import TerminalColors

if len(sys.argv) != 2:
    print(f"{TerminalColors.TerminalColors.FAIL}Error! "
        f"Wrong amount of arguments detected!{TerminalColors.TerminalColors.ENDC}")
    print(f"{TerminalColors.TerminalColors.WARNING}usage : {TerminalColors.TerminalColors.ENDC}"
        f"{TerminalColors.TerminalColors.OKGREEN}python computor.py "
        f"\"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\"{TerminalColors.TerminalColors.ENDC}")
    exit()
argument = sys.argv[1]

print(argument)
