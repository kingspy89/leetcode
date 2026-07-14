class Solution(object):
  def convert(self, s, numRows):
    
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    index = 0   
    step = 1    

    for char in s:
        rows[index] += char
        index += step

        # If we hit bottom or top, reverse direction
        if index == 0 or index == numRows - 1:
            step *= -1

    # Combine all rows into one string
    return ''.join(rows)
