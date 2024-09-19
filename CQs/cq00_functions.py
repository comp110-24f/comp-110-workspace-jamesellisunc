"""My first challenge question in COMP110"""

__author__ = "730739772"


def mimic(message: str) -> str:
    """Will mimic the message back to you"""
    return message


def main() -> None:
    """Result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
