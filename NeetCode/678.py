# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         stack = []
#
#         for char in s:
#             if char != ")":
#                 stack.append(char)
#
#             while stack and