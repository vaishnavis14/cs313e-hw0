import sys

def all_substrings (s):
    result = []
    # define size of window
    wnd = len(s)

    # generate all substrings
    while (wnd > 0):
        index = 0
        while (index + wnd) <= len(s):
            sub_string = s[index:index+wnd]
            result.append(sub_tring)
            index += 1
        # decrease the size of the window
        wnd = wnd - 1
        
    return result
    
def test_cases():
    # test the function longest_subsequence
    assert longest_subsequence("a", "a") == ["a"]
    assert longest_subsequence("abcd", "bc") == ["bc"]
    assert longest_subsequence("abcd", "xyz") == []
    assert longest_subsequence("abcdefg", "ujcdkj") == ["cd"]
    assert longest_subsequence("lmnopq", "lmkjkjopkm") == ["lm", "op"]

    # test the function of all_substrings
    assert all_substrings("a") == ["a"]
    assert all_substrings("abc") == ["a", "b", "c", "ab", "bc", "abc"]

    # return the test cases
    return "all test cases passed"

def longest_subsequence(s1, s2):

    
def main():
    num_pairs = sys.stdin.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int(num_pairs)
    print(num_pairs)

    for i in range(num_pairs):
        st1 = sys.stdin.readline().strip().upper()
        st2 = sys.stdin.readline().strip().upper()
        print(st1, st2)

        long_sub = longest_subsequence(st1, st2)

if __name__ == "__main__":
    main()
