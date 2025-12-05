a = 0b101100 # 10進数では44
b = 0b110110 # 10進数では54
c = []

c.append(bin(a & b).count('1')) # 0b101100&0b110110 = 0b100100 = 2
c.append(bin(a | b).count('1')) # 0b101100|0b110110 = 0b111110 = 5
c.append(bin(a ^ b).count('1')) # 0b101100^0b110110 = 0b11010  = 3
c.append(bin(a >> 2).count('1')) # 0b101100>>2      = 0b1011   = 3
print(c)
