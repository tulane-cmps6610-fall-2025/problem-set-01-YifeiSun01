"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if a == 0:
        return b
    if b == 0:
        return a
    x = min(a, b)
    y = max(a, b)
    return foo(y, y % x)

def longest_run(mylist, key):
    best = 0 
    cur = 0  
    for x in myarray:
        if x == key:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return best


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    # returns a Result for subarray mylist[lo:hi], half-open
    def rec(lo, hi):
        # empty segment
        if lo >= hi:
            return Result(0, 0, 0, True)
        # single element
        if hi - lo == 1:
            if mylist[lo] == key:
                return Result(1, 1, 1, True)
            else:
                return Result(0, 0, 0, False)

        mid = (lo + hi) // 2
        L = rec(lo, mid)
        R = rec(mid, hi)

        # combine
        is_entire = L.is_entire_range and R.is_entire_range
        left_size  = L.left_size  + R.left_size  if L.is_entire_range else L.left_size
        right_size = R.right_size + L.right_size if R.is_entire_range else R.right_size
        longest    = max(L.longest_size, R.longest_size, L.right_size + R.left_size)

        return Result(left_size, right_size, longest, is_entire)

    return rec(0, len(mylist)).longest_size

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


