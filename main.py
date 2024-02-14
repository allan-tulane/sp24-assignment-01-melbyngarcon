"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  # Base cases: the first two numbers of the Fibonacci sequence are 0 and 1, respectively.
  if x == 0:
      return 0
  elif x == 1:
      return 1
  else:
      # Recursive case: Fibonacci number is the sum of the two preceding numbers.
      return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
# Initialize variables to keep track of the current run length and the maximum found so far.
  max_run = 0
  current_run = 0

  for value in mylist:
    if value == key:
        # If the current value matches the key, increment the current run length.
        current_run += 1
        # Update the max run length if the current run is longer.
        max_run = max(max_run, current_run)
    else:
        # If the current value does not match the key, reset the current run length.
        current_run = 0

  return max_run


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
  # Base case: If the list is empty, return a Result object with all sizes set to 0.
  if not mylist:
      return Result(0, 0, 0, False)

  # Base case: If the list has one element, check if it's the key.
  if len(mylist) == 1:
      if mylist[0] == key:
          return Result(1, 1, 1, True)
      else:
          return Result(0, 0, 0, False)

  # Recursive case: Split the list into two halves.
  mid = len(mylist) // 2
  left_half = mylist[:mid]
  right_half = mylist[mid:]

  # Recursively find the longest run in each half.
  left_result = longest_run_recursive(left_half, key)
  right_result = longest_run_recursive(right_half, key)

  # Combine the results.
  # If the entire left half is a run of the key, and the right half starts with the key,
  # we can extend the left run into the right half.
  left_size = left_result.left_size
  if left_result.is_entire_range and len(right_half) > 0 and right_half[0] == key:
      left_size += right_result.left_size

  # Similarly, if the entire right half is a run of the key, and the left half ends with the key,
  # we can extend the right run into the left half.
  right_size = right_result.right_size
  if right_result.is_entire_range and len(left_half) > 0 and left_half[-1] == key:
      right_size += left_result.right_size

  # The longest run might be entirely within one half, or it might span the boundary.
  # If it spans the boundary, we add the right run size of the left half to the left run size of the right half.
  longest_size = max(left_result.longest_size, right_result.longest_size, left_result.right_size + right_result.left_size)

  # Determine if the entire range is a continuous run of the key.
  is_entire_range = left_result.is_entire_range and right_result.is_entire_range

  return Result(left_size, right_size, longest_size, is_entire_range)


