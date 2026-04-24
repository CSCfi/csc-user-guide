import sys

from navigation.traverser import NavTraverser


if __name__ == "__main__":
    traverser = NavTraverser(sys.argv[1])
    print("Checking", *(f"- {name}" for name in traverser.filenames), sep="\n", end="\n"*2)
    print(traverser.output if traverser.output else "No discrepancies.")
