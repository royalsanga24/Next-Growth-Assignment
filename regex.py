import re

string = """
{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
"""

def find_ids(string):
    """
        string: The input string/response
    """
    pattern = r'"id":(\d+)' #  `"id":` matches the string "id": in string and (\d+) matches one or more digits preceding `"id":` value
    return re.findall(pattern, string) # matches the pattern in input string and returns a list of all matches
    
print(find_ids(string))
