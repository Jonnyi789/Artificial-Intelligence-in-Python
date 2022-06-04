import common
import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def check_result(title, map1, map2):
	result=True
	print(title)
	for y in range(0,common.constants.MAP_HEIGHT):
		v=""
		for x in range(0,common.constants.MAP_WIDTH):
			if (map1[y][x]==map2[y][x]):
				v+=bcolors.GREEN+str(map1[y][x])+bcolors.NORMAL
			else:
				result = False
				v+=bcolors.RED+str(map1[y][x])+bcolors.NORMAL
		print(v)
	if (result):
		print("Test Result: " + bcolors.GREEN+"Passed"+bcolors.NORMAL)
	else:
		print("Test Result: " + bcolors.RED+"Failed"+bcolors.NORMAL)
	return result
	
# data1 = ("21111111111"
# "01111111111"
# "01111111111"
# "00000000000"
# "01111111110"
# "01000000000"
# "01111111111"
# "00000000000"
# "01111011111"
# "01111011110"
# "01100011013"
# "01111111110")

# gold_df1 = ("41111111111"
# "41111111111"
# "41111111111"
# "44444444444"
# "41111111114"
# "41444444444"
# "41111111111"
# "44444444444"
# "41111411111"
# "41111411110"
# "41144411013"
# "41111111110")

# gold_bf1 = ("41111111111"
# "41111111111"
# "41111111111"
# "44444444444"
# "41111111114"
# "41444444444"
# "41111111111"
# "44444444444"
# "41111411111"
# "41111411110"
# "41144411013"
# "41111111110")

# data2 = ("00000000000"
# "00000000000"
# "11111111110"
# "00001000000"
# "01111111110"
# "00000000000"
# "11111101111"
# "00000320000"
# "11111101110"
# "00000100100"
# "01111110110"
# "00000000100")

# gold_df2 = ("00000000000"
# "00000000000"
# "11111111110"
# "00001000000"
# "01111111110"
# "00000000000"
# "11111101111"
# "00000554444"
# "11111141114"
# "44444144144"
# "41111114114"
# "44444444144")

# gold_bf2 = ("00000000000"
# "00000000000"
# "11111111110"
# "00001000000"
# "01111111110"
# "00000000000"
# "11111101111"
# "00000554000"
# "11111141110"
# "00000100100"
# "01111110110"
# "00000000100")

data3 = ("00000111110"
"01010100000"
"01010111110"
"01010100000"
"01010111110"
"01013100000"
"01111111110"
"00000000000"
"11111111110"
"00001000000"
"01111111110"
"20000000000")

gold_df3 = ("55555111110"
"51015100000"
"51015111110"
"51015100000"
"51015111110"
"51015100000"
"51111111110"
"55555555555"
"11111111115"
"00001444445"
"01111111115"
"55555555555")

gold_bf3 = ("55555111114"
"51415144444"
"51415111114"
"51415144444"
"51415111114"
"51415144444"
"51111111114"
"55555555555"
"11111111115"
"44441444445"
"41111111115"
"55555555555")

data1 = ("21000000000"
"01011111110"
"01000000010"
"01111111010"
"01000001010"
"01011101010"
"01013101010"
"01010001010"
"01011111010"
"01000000010"
"01111111110"
"00000000000")

gold_df1 = ("51555555555"
"51511111115"
"51555555515"
"51111111515"
"51555551515"
"51511151515"
"51515151515"
"51515551515"
"51511111515"
"51555555515"
"51111111115"
"55555555555")

gold_bf1 = ("51555555555"
"51511111115"
"51555555515"
"51111111515"
"51555551515"
"51511151515"
"51515151515"
"51515551515"
"51511111515"
"51555555515"
"51111111115"
"55555555555")

data2 = ("20000000001"
"01011111111"
"01000000001"
"01011111111"
"01010000011"
"01010101101"
"01010100001"
"01000111101"
"00111111101"
"10111111101"
"10111111111"
"10000000031")

gold_df2 = ("54444444441"
"51411111111"
"51444444441"
"51411111111"
"51414444411"
"51414141141"
"51414144441"
"51444111141"
"55111111141"
"15111111141"
"15111111111"
"15555555551")

gold_bf2 = ("54444444441"
"51411111111"
"51444444441"
"51411111111"
"51414444411"
"51414141101"
"51414144401"
"51444111101"
"55111111101"
"15111111101"
"15111111111"
"15555555551")

# data1 = ("2000000000"
# "0101111111"
# "0100000000"
# "0101111111"
# "0101000001"
# "0101010110"
# "0101010000"
# "0100011110"
# "0011111110"
# "1011111110"
# "1011111111"
# "1000000003")
			  
# gold_df1 = ("5444444444"
#   "5141111111"
#   "5144444444"
#   "5141111111"
#   "5141444441"
#   "5141414114"
#   "5141414444"
#   "5144411114"
#   "5511111114"
#   "1511111114"
#   "1511111111"
#   "1555555555")
					 
# gold_bf1 = ("5444444444"
#   "5141111111"
#   "5144444444"
#   "5141111111"
#   "5141444441"
#   "5141414110"
#   "5141414440"
#   "5144411110"
#   "5511111110"
#   "1511111110"
#   "1511111111"
#   "1555555555")
					 

# data2 = ("0000000000"
# "1111110101"
# "0300010101"
# "1111010101"
# "0001010101"
# "0100010101"
# "1111010101"
# "0000000101"
# "0111111100"
# "0000000101"
# "0111111120"
# "0000000010")
			  
# gold_df2 = ("0000005554"
#   "1111115151"
#   "0555515151"
#   "1111515151"
#   "4441515151"
#   "4144515151"
#   "1111515151"
#   "4444555151"
#   "4111111154"
#   "4444444151"
#   "4111111154"
#   "4444444414")
					 
# gold_bf2 = ("4444445554"
#   "1111115151"
#   "0555515151"
#   "1111515151"
#   "4441515151"
#   "4144515151"
#   "1111515151"
#   "4444555151"
#   "4111111154"
#   "4440000151"
#   "4111111154"
#   "4000000014")

# data3 = ("0000000000"
# "0010111111"
# "0210100000"
# "1110101110"
# "0000101010"
# "0010101010"
# "0010001010"
# "0011111010"
# "0000000010"
# "0011111110"
# "0010001031"
# "1000101001")
			  
# gold_df3 = ("4444444444"
#   "4414111111"
#   "4414144444"
#   "1114141114"
#   "4444141414"
#   "4414141414"
#   "4414441414"
#   "4411111414"
#   "4444444414"
#   "4411111114"
#   "4414441031"
#   "1444141001")
					 
# gold_bf3 = ("4444444444"
#   "4414111111"
#   "4414144444"
#   "1114141114"
#   "4444141414"
#   "4414141414"
#   "4414441414"
#   "4411111414"
#   "4444444414"
#   "4411111114"
#   "4414441031"
#   "1444141001")

all_passed = True

gold_dfmap1 = common.init_map();
common.set_map(gold_dfmap1, gold_df1)
gold_bfmap1 = common.init_map()
common.set_map(gold_bfmap1, gold_bf1)

dfmap1 = common.init_map()
common.set_map(dfmap1, data1)
df1 = student_code.df_search(dfmap1)
tdf1 = "Simple maze first depth search results:";
cdf1 = check_result(tdf1,dfmap1,gold_dfmap1)

if df1:
	print( bcolors.GREEN+"correct return value"+bcolors.NORMAL)
else:
	print( bcolors.RED+"wrong return value"+bcolors.NORMAL)
print("\n\r")

bfmap1 = common.init_map()
common.set_map(bfmap1, data1)
bf1 = student_code.bf_search(bfmap1)
tbf1 = "Simple maze first breadth search results:"
cbf1 = check_result(tbf1,bfmap1,gold_bfmap1)
if bf1:
	print( bcolors.GREEN+"correct return value"+bcolors.NORMAL)
else:
	print( bcolors.RED+"wrong return value"+bcolors.NORMAL)
print("\n\r")

all_passed = all_passed and cdf1 and cbf1 and df1 and bf1 

gold_dfmap2 = common.init_map();
common.set_map(gold_dfmap2, gold_df2)
gold_bfmap2 = common.init_map()
common.set_map(gold_bfmap2, gold_bf2)

dfmap2 = common.init_map()
common.set_map(dfmap2, data2)
df2 = student_code.df_search(dfmap2)
tdf2 = "Empty map first depth search results:";
cdf2 = check_result(tdf2,dfmap2,gold_dfmap2)
if df2:
	print( bcolors.GREEN+"correct return value"+bcolors.NORMAL)
else:
	print( bcolors.RED+"wrong return value"+bcolors.NORMAL)
print("\n\r")

bfmap2 = common.init_map()
common.set_map(bfmap2, data2)
bf2 = student_code.bf_search(bfmap2)
tbf2 = "Empty map first breadth search results:"
cbf2 = check_result(tbf2,bfmap2,gold_bfmap2)
if bf2:
	print( bcolors.GREEN+"correct return value"+bcolors.NORMAL)
else:
	print( bcolors.RED+"wrong return value"+bcolors.NORMAL)
print("\n\r")

all_passed = all_passed and cdf2 and cbf2 and df2 and bf2 

gold_dfmap3 = common.init_map();
common.set_map(gold_dfmap3, gold_df3)
gold_bfmap3 = common.init_map()
common.set_map(gold_bfmap3, gold_bf3)

dfmap3 = common.init_map()
common.set_map(dfmap3, data3)
df3 = student_code.df_search(dfmap3)
tdf3 = "Empty map first depth search results:";
cdf3 = check_result(tdf3,dfmap3,gold_dfmap3)
if not df3:
	print( bcolors.GREEN+"correct return value"+bcolors.NORMAL)
else:
	print( bcolors.RED+"wrong return value"+bcolors.NORMAL)
print("\n\r")

bfmap3 = common.init_map()
common.set_map(bfmap3, data3)
bf3 = student_code.bf_search(bfmap3)
tbf3 = "Empty map first breadth search results:"
cbf3 = check_result(tbf3,bfmap3,gold_bfmap3)

if not bf3:
	print( bcolors.GREEN+"correct return value"+bcolors.NORMAL)
else:
	print( bcolors.RED+"wrong return value"+bcolors.NORMAL)
print("\n\r")
