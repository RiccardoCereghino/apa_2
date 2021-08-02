from typing import Iterator


def file_reader(file_name: str) -> Iterator[int]:
    """Generates an iterator per line from a file encoded in utf8, specified with file_name"""
    for line in open(file_name, "r", encoding="utf8"):
        yield int(line)


if __name__ == '__main__':
    results = []
    c = 0
    for n in file_reader("result_rick.txt"):
        results.append(n)
        if n == 4:
            c += 1

    print("MIN")
    print(min(results))
    print("MAX")
    print(max(results))
    print("Counter")
    print(c)
    print("Prob")
    print(c/100000)

