import time
from typing import List
import unittest


def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  # noqa
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    if counter:
        compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, "".join(compressed), key=len)

def compress(self, chars: List[str]) -> int:
    walker, runner = 0, 0
    while runner < len(chars):
    
        chars[walker] = chars[runner]
        count = 1
        
        while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
            runner += 1
            count += 1
        
        if count > 1:
            for c in str(count):
                chars[walker+1] = c
                walker += 1
        
        runner += 1
        walker += 1
    
    return walker


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]
    testable_functions = [
        compress_string,
    ]

    def test_string_compression(self):
        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for test_string, expected in self.test_cases:
                    assert f(test_string) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
