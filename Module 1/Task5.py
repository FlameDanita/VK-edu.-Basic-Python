a = int(input())
b = float(input())
c = int(input())

print(f"{a:+010d}")
print(f"{b:#>10.2f}")
# print(f"{c:0>16b}")

res_current = (f"{c:0>16b}")
result = str(res_current)
result = (result[::-1])
print('_'.join(result[i:i+4] for i in range(0, len(result), 4))[::-1])


#  +000000102\n######3.14\n100_0110_0111
# "-000001024\n######3.14\n100_0110_0111"
# "+000000563\n###-123.46\n110_1111"