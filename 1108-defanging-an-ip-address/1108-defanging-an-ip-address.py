class Solution(object):
    def defangIPaddr(self, address):
        new = ""

        for ch in address:
            if ch == ".":
                new = new +"[.]"
            else:
                new =new + ch

        return new