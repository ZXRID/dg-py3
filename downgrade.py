# Made by ZXRID from XiuzCode & BlackCoderCrush
# XiuzCode : https://github.com/XiuzCode
# BlackCoderCrush : https://github.com/blackcodercrush
# Reference : https://www.yvtix.xyz/2020/10/termux-downgrade-py3.9-to-py3.8.html

from subprocess import check_output as out
import os
import sys
if '3.9.0' not in sys.version:
    exit('[*] Your python version already downgraded.')
for module in ['bs4','requests']:
    try:
        exec(f'import {module}')
    except:
        os.system(f'python3 -m pip install {module}')
        exec(f'import {module}')
soup = bs4.BeautifulSoup

class DownGrade_PY:
    def __init__(self):
        print ('<[ DOWNGRADE PYTHON 3.9.X TO PYTHON 3.8.6 ]>')
        self.url = 'https://mirrors.dgut.edu.cn/termux/termux-packages-24/'
        self.arch = out(['dpkg','--print-architecture']).strip().decode()
        print (f'[*] Your architecture: {self.arch}')
        self.run()

    def run(self):
        data = requests.get(self.url).text
        if self.arch not in data:
            exit('[!] Your architecture not supported')
        link = f'{self.arch}/'
        data_1 = requests.get(self.url + link).text
        data_1 = soup(data_1,'html.parser')
        data_1 = data_1.find('a', string=lambda _: _ and 'python_3.8.6' in _)['href']
        print ('[*] Python package found')
        print ('[+] Downloading... (don\'t close before download are completed.)')
        with open('python_3.8.6.deb','wb') as download:
            download.write(requests.get(self.url + link + data_1).content)
        print ('[*] Download complete, installing...')
        os.system('pkg install ./python_3.8.6.deb --allow-downgrades -y')
        exit ('[*] Downgrade success!')

DownGrade_PY()
