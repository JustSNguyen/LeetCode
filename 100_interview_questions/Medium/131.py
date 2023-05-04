from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        string_length = len(s)
        partitions = [-1 for _ in range(string_length)]

        def check_palindrome(start_index, end_index):
            length = end_index - start_index + 1 
            for i in range(start_index, start_index + length // 2):
                if s[i] != s[end_index - i + start_index]:
                    return False 
            
            return True 

        def partition_dp(index):
            if index >= string_length:
                return []
            
            if partitions[index] != -1:
                return partitions[index]
            
            partitions[index] = []
            for end_index in range(index, string_length):
                cur_partition = []
                is_palindrome = check_palindrome(index, end_index)
                if not is_palindrome: 
                    continue 
                
                cur_palindrome = s[index: end_index + 1]
                next_partitions = partition_dp(end_index + 1)

                if len(next_partitions) == 0:
                    cur_partition = [cur_palindrome]
                    partitions[index].append(cur_partition)
                    continue 
                
                for next_partition in next_partitions:
                    cur_partition = [cur_palindrome]
                    cur_partition += next_partition
                    partitions[index].append(cur_partition)
            
            return partitions[index]

        return partition_dp(0)
    
if __name__ == '__main__':
    sol = Solution()
    s = "a"
    res = sol.partition(s)
    print(res)