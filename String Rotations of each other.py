class Solution:
    
    # Function to check if two strings are rotations of each other or not
    def areRotations(self, s1, s2):
        # Step 1: Agar length same nahi hai toh rotation possible hi nahi
        if len(s1) != len(s2):
            return False
        
        # Step 2: s1 ko do baar concatenate karo
        temp = s1 + s1
        
        # Step 3: Check karo kya s2, temp ka substring hai
        return s2 in temp



# ✅ Test the function with a sample input
if __name__ == "__main__":
    obj = Solution()
    s1 = "abcde"
    s2 = "deabc"
    print("Are Rotations:", obj.areRotations(s1, s2))  # Output: True
