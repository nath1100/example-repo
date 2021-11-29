def foo(text: str="") -> str:
    """
    This is an example function that takes a
    string, performs meaningless operations,
    and then returns a string.
    """
    
    # Here is a comment

    if text == "":
        new_string = "empty string"
    new_string = text[::-1]
    some_dict = {
        "w": 3,
        "a": 4,
        "z": 2,
        "p": 3,
        "e": 1,
        "p": 1
    }
    new_string.replace(max(some_dict), "@")
    return new_string

def main() -> None:
    print(foo("this is some text that goes into this function to do useless things"))

if __name__ == "__main__":
    main()
