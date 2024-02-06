#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    f_names = sorted(name for name in names if not name.startswith("__"))
    for nam in f_names:
        print(nam)
