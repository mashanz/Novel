import os

MECHINES = [['EYE_BUG',['A',10, 0, 5, 0, 7]],
			['LIGHT_BUG',['A',10, 0, 5, 0, 7]],
			['FLASH_BUG',['A',10, 0, 5, 0, 7]],
			['POWER_BANK_BUG',['A',10, 0, 5, 0, 7]],
			['HEXSIGHT',['A',10, 0, 5, 0, 7]],
			['MULTIPOD',['A',10, 0, 5, 0, 7]],
			['GUARDIANPOD',['A',10, 0, 5, 0, 7]],
			['MOTHERPOD',['A',10, 0, 5, 0, 7]],
			['MINIBOT',['A',10, 0, 5, 0, 7]],
			['TREACHER',['A',10, 0, 5, 0, 7]]]
FUEL	 = ['Type', 'Black_LQ', 'Light','Water','Crystoid','Food']
MATERIALS= []
TOOLS    = []

def SEE_MECHINES():
	x = 0
	y = 0
	while x < len(MECHINES):
		print('\n',MECHINES[x][1])
		while y < 6:
			print(' ',FUEL[y],' \t:',MECHINES[x][1][y])
			y+=1
		y=0
		x+=1

if __name__ == "__main__":
    os.system("cls")
    SEE_MECHINES()