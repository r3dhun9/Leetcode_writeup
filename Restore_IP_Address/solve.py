class Solution:
    valid_array = []
    
    def restoreIpAddresses(self, s):
        if len(s) < 4 or len(s) > 12:
            return
        curr = ""
        self.valid_array = []
        self.dfs(s, 0, curr)
        return self.valid_array
        
    def dfs(self, s, segment, cur):
        if segment == 3:
            if len(s) > 0:
                if self.isValid(s):
                    self.valid_array.append(cur + s)
                    return
        for i in range(1,4):
            if i > len(s):
                return
            tmp = s[:i]
            if self.isValid(tmp):
                self.dfs(s[i:], segment+1, cur+tmp+'.')
        
    def isValid(self, s):
        if s[0] == '0':
            if s == '0':
                return True
            else:
                return False
        if int(s) > 255 or int(s) < 0:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "0000"
    l = sol.restoreIpAddresses(s)
    print(l)