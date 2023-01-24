import os
from colored import fg, bg, attr

reset = attr(0)
darkorange = fg(209)
orange = fg(208)
red = fg(9)
green = fg(46)
os.system('clear')
print(f'''{orange}
 __  __    __    ___  ___   ___    __    _  _ 
(  \/  )  /__\  / __)/ __) / __)  /__\  ( \( )
 )    (  /(__)\ \__ \\\\__  \( (__  /(__)\  )  ( 
(_/\/\_)(__)(__)(___/(___/ \___)(__)(__)(_)\_) 2.0
			made by github/lucadado''')
if os.path.exists('masscanchecker.jar'):
    pass
else:
    print(f'{red}masscanchecker.jar doesn\'t exist!')
    print(f'{green}Downloading masscanchecker.jar')
    os.system('wget https://github.com/lucadado/masscanchecker/raw/main/masscanchecker.jar')
if os.path.exists('r-checker.jar'):
    pass
else:
    print(f'{red}r-checker.jar doesn\'t exist!')
    print(f'{green}Downloading r-checker.jar')
    os.system('wget https://github.com/lucadado/r-checker/raw/main/r-checker.jar')
if os.path.exists('outputs/'):
    pass
else:
    os.mkdir('outputs')  
ip = input(f'{orange}Insert the range: {darkorange}')
if ip.find('*.*'):
	ip = ip.replace('*.*', '0.0/16')
if ip.find('*'):
    ip = ip.replace('*', '0/24')
print(f'{orange}Range: {darkorange}{ip}')
paper = '1-9,12-17,100-110,200-205,212,300-305,400-405,500-505,600-605,666,700-705,777,800-805,900-905,1000-1005,2000-2025,3000-3005,4000-4005,5000-5005,6666,7000-7005,7777,8000-8015,9000-9010,9571,10000-10300,11000-11010,11111,11783,12000-12010,12345,12346,13000-13010,13370,13377,13338,14000-14010,15000-15010,15535,16000-16010,17000-17010,18000-18010,19000-19010,20000-20050,21000-21020,21152,21243,22000-22020,22222,23000-23005,23456,23467,23647,24000-24005,25000-26020,26666,27000-27020,27565,27765,27489,27777,28000-28005,28888,29000-29005,29999,30000-30020,33333,34567,35000,35565,40000-40020,44444,44829,50000-50020,55555,60000-60020,65535'
spooky = '40100-40500,20000-20100,26584,25999,29999,25000-25900,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2500,2800,5500,6000,6500,7001,7100,7200,5200,5252,9000,9100,16700,16800,16900,17000,17100,17200,16566,1516,69,96,18000-18025,999,5,1,2,3,4,6,7,8,9,10,8000-8025,65534,1515,1678,15915,1696,1506,1514,406,700-705,1500-1550,501-525,60000-60005,500,25599,25500,25600,25500,36000-36010,25555,25670,45000-45025,5000-5005,50000-50005,15000-15015,1000-1025,1-20,26-28,88,1234,123,234,30000-30020,16000-16010,14711,14000-14005,800-900,900-905,32000-32020,35000-35010,20000-20020,25000-25015,45000-45200,10000-10050,6666,777,888,7777,40000-40050,20000,20001,20002,20003,20004,20005,20100,20200,20300,20400,20500,20600,20700,20800,20900,21000,21001,21002,21003,21004,21005,21100,21200,21300,21400,21500,21600,21700,21800,21900,22100,22200,22300,22400,22500,22600,22700,22800,22900,23000,23100,23200,23300,23400,23500,23600,23700,23800,23900,24000,24100,24200,24300,24400,24500,24600,24700,24800,24900,27100,27200,27300,27400,27500,27600,27700,27800,27900,28100,28200,28300,28400,28500,28600,28700,28800,28900,29100,29200,29300,29400,29500,29600,29700,29800,29900,60000,60001,60002,60003,60004,60005,10100,10200,10300,10400,10500,10600,10700,10800,10900,11100,11200,11300,11400,11500,11600,11700,11800,11900,12100,12200,12300,12400,12500,12600,12700,12800,12900,13000,13100,13200,13300,13400,13500,13600,13700,13800,13900,14000,14100,14200,14300,14400,14500,14600,14700,14800,14900,15000,15100,15200,15300,15400,15500,15600,15700,15800,15900,16100,16200,16300,16400,16500,16600,16700,16800,16900,17100,17200,17300,17400,17600,17800,17900,18100,18200,18300,18400,18500,18600,18700,18800,18900,19100,19200,19300,19400,19500,19600,19700,19800,19900,30000,30001,30002,30003,30004,30005,25555,25000,25001,25002,25003,25004,25005,25100,25200,25300,25400,25600,25700,25800,25900,26000,26001,26002,26003,26004,26005,40000-40005,10000-10005,50000-50005'
lpr = '1-9,12-17,81-110,200-205,300-305,400-405,500-505,600-605,666,700-705,777,800-805,900-905,1000-1005,2000-2020,3000-3005,4000-4005,5000-5005,6666,7000-7005,7777,8000-8010,10000-10020,12345,12346,13338,20000-20020,21000-21020,22000-22020,23000-23005,24000-24005,25000-25020,25500-25630,26000-26020,26666,27000-27020,27777,28000-28005,28888,29000-29005,29999,10000-10020,20000-20020,30000-30020,40000-40020,50000-50020,60000-60020'
zephix = '1-9,12-17,100-120,200-220,300-320,400-420,500-520,600-620,700-720,800-820,900-920,1000-1020,2000-2020,3000-3020,4000-4020,5000-5020,6000-6020,7000-7020,8000-8020,8100-8120,9000-9020,10000-10100,11000-11100,12000-12100,13000-13100,14000-14100,15000-15100,16000-16100,17000-17100,18000-18100,19000-19100,20000-20300,21000-21100,22000-22100,23000-23100,24000-24100,25000-30000,31000-31100,32000-32100,33000-33100,34000-34100,35000-35100,36000-36100,37000-37100,38000-38100,39000-39100,40000-40500,41000-41100,42000-42100,43000-43100,44000-44100,45000-45100,46000-46100,47000-47100,48000-48100,49000-49300,50000-50400,51000-51100,52000-52100,53000-53100,54000-54100,55000-55100,56000-56100,57000-57100,58000-58100,59000-59100,60000-60300,61000-61100,62000-62100,63000-63100,64000-64100,65000-65535'

rate = input(f'{orange}Insert the max-rate (default 5000): {darkorange}')
if rate == '':
	rate = '5000'
else:
	pass
print(f'Max-rate: {rate}')
outputscan = input(f'{orange}Insert the output of masscan scan (ms_scan default): {darkorange}')
if outputscan == '':
	outputscan = 'ms_scan'
else:
	pass
print(f'Outputscan: {outputscan}')
outputchecker = input(f'{orange}Insert the output of the checker (ms_checked default): {darkorange}')
if outputchecker == '':
	outputchecker = 'ms_checked'
else:
	pass
print(f'Outputchecker: {outputchecker}')
check = input(f'{orange}Do you want automatically check the servers? (y/n): {darkorange}')
ports = input(f'''{orange}
Available Range:
» Spooky 
» paper
» lpr (Low Port Range)
» zephix

Insert port range: ''')
if ports == 'Spooky':
	print(f'{orange}Port Range: {darkorange}Spooky')
	command = f'masscan -p{spooky} {ip} --max-rate {rate} -oL outputs/{outputscan}'
	os.system(command)
elif ports == 'paper':
	print(f'{orange}Port Range: {darkorange}paper')
	command = f'masscan -p{paper} {ip} --max-rate {rate} -oL outputs/{outputscan}'
	os.system(command)
elif ports == 'lpr':
	print(f'{orange}Port Range: {darkorange}lpr')
	command = f'masscan -p{lpr} {ip} --max-rate {rate} -oL outputs/{outputscan}'
	os.system(command)
elif ports == 'zephix':
	print(f'{orange}Port Range: {darkorange}zephix')
	command = f'masscan -p{zephix} {ip} --max-rate {rate} -oL outputs/{outputscan}'
	os.system(command)
else:
	print(f'{orange}Port Range: {darkorange}{ports}')
	command = f'masscan -p{ports} {ip} --max-rate {rate} -oL outputs/{outputscan}'
	os.system(command)
os.system(f'java -jar masscanchecker.jar {outputscan} 10 | tee outputs/{outputchecker}')
num_lines = sum(1 for line in open(f'outputs/{outputchecker}'))
print(f'{orange}Server found: {darkorange}{num_lines}')
print(f'{red}Deleted \'{outputscan}\'{reset}')
os.system(f'rm -rf outputs/{outputscan}')
if check.lower() == 'y' or check.lower() == 'yes':
    print(f'{green}Checking...{reset}')
    os.system(f'java -jar r-checker.jar outputs/{outputchecker} | outputs/{outputchecker}-checked')
else:
    pass
