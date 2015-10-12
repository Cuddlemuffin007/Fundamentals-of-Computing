"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    shifted = shift(line)
    shifted.append(0)
    merged = [0]*len(line)
    merged_idx = 0
    shifted_idx = 0
    while shifted_idx < (len(shifted)-1):
        if shifted[shifted_idx] == shifted[shifted_idx+1]:
            merged[merged_idx] = shifted[shifted_idx]*2
            shifted_idx += 2
        elif shifted[shifted_idx] != shifted[shifted_idx+1]:
            merged[merged_idx] = shifted[shifted_idx]
            shifted_idx += 1
        merged_idx += 1     
    return merged
    
def shift(line):
    """
    Function that shifts a line (list) to the left
    """
    result = [0]*len(line)
    result_idx = 0
    for idx in range(len(line)):
        if line[idx] != 0:
            result[result_idx] = line[idx]
            result_idx += 1
    return result
#Tests for merge
"""
def test_merge():
    """
    Test code for merge function
    """
    test1 = [2, 0, 2, 4] #should return [4, 4, 0, 0]
    test2 = [0, 0, 2, 2] #should return [4, 0, 0, 0]
    test3 = [2, 2, 0, 0] #should return [4, 0, 0, 0]
    test4 = [2, 2, 2, 2, 2] #should return [4, 4, 2, 0, 0]
    test5 = [8, 16, 16, 8] #should return [8, 32, 8, 0]

    print "Testing shift - Computed:", shift(test1), "Expected:", str([2, 2, 4, 0])
    print "Testing merge - Computed:", merge(test1), "Expected:", str([4, 4, 0, 0])
    print "Testing shift - Computed:", shift(test2), "Expected:", str([2, 2, 0, 0])
    print "Testing merge - Computed:", merge(test2), "Expected:", str([4, 0, 0, 0])
    print "Testing shift - Computed:", shift(test3), "Expected:", str([2, 2, 0, 0])
    print "Testing merge - Computed:", merge(test3), "Expected:", str([4, 0, 0, 0])
    print "Testing shift - Computed:", shift(test4), "Expected:", str([2, 2, 2, 2, 2])
    print "Testing merge - Computed:", merge(test4), "Expected:", str([4, 4, 2, 0, 0])
    print "Testing shift - Computed:", shift(test5), "Expected:", str([8, 16, 16, 8])
    print "Testing merge - Computed:", merge(test5), "Expected:", str([8, 32, 8, 0])
    
test_merge()
"""