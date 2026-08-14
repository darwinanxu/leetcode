"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network 
and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

    String encode(List<String> strs) {
        // ... your code
        return encoded_string;
    }

Machine 2 (receiver) has the function:

    List<String> decode(String encoded_string) {
        // ... your code
        return decoded_strs;
    }

So Machine 1 does:

    String encoded_string = encode(strs);
    
and Machine 2 does:

    List<String> decoded_strs = decode(encoded_string);    

decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

Example 1:
Input: strs = ["Hello","World"]
Output: ["Hello","World"]

Example 2:
Input: strs = [""]
Output: [""]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
"""

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j+1 : j+1+length]
            result.append(word)

            i = j+1+length 

        return result

# Using list.append() and "".join() is more space-efficient 
# than repeatedly concatenating strings with +
class Solution2:  
    def encode(self, strs: List[str]) -> str:
        encode_list = []

        for s in strs:
            encode_list.append(str(len(s)))
            encode_list.append("#")
            encode_list.append(s)

        return "".join(encode_list)


    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            str_len = int(s[i:j])
            str_start = j + 1
            str_end = str_start + str_len -1
            string = s[str_start : str_end + 1]

            decode_list.append(string)
            i = str_end + 1

        return decode_list
