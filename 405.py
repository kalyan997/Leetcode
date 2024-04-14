class Solution:
    def toHex(self, num: int) -> str:
        
        hex_map = {0:"0", 1:"1",2:"2",3:"3",4:"4",5:"5",
                  6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",
                  12:"c",13:"d",14:"e",15:"f"}
        if num == 0:
            return "0"
        res = ""
        #curr_pos = 0
        if num < 0:
            num &= 0xFFFFFFFF
            
        print(num)
        while num>0:
            curr_bit = num%16
            num = num//16
            
            res = hex_map[curr_bit] + res
            
        return res