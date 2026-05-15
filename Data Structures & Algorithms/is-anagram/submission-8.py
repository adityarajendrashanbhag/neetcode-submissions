"""
Dictionary lookup:
When you do s_dict['a'], Python has to:

Take the key 'a'
Run it through a hash function to convert it to a number
Go to that location in memory

That hashing step takes extra work every single time.
Array lookup:
When you do arr[0], Python just:

Go directly to index 0 in memory

No extra steps, no hashing — just direct access.
Think of it like this:

Dictionary → You give a name, security converts it to a number, then finds your seat
Array → You already have a seat number, go directly

Same end result, but array skips the middle step. That's why arrays are faster in practice even though both are technically O(1).

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for i in s:
            if i in s_dict:
                s_dict[i] = s_dict.get(i) + 1
            else:
                s_dict[i] = 1

        for i in t:
            if i in t_dict:
                t_dict[i] = t_dict.get(i) + 1
            else:
                t_dict[i] = 1
            
        return s_dict == t_dict



        