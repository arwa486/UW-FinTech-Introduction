import subprocess
import json 
from constants import *
import os


#!pip install python-dotenv
#from dotenv import load_dotenv 
#load_dotenv()

#Use python-dotenv library to find the mnemonic stored in the .env file
mnemonic = os.getenv('MNEMONIC', 'virtual pretty time number wedding siren private narrow sign provide require black')

#Function derive the wallet addresses 
coins = [BTC, ETH, BTCTEST]

#command = './derive -g --mnemonic="virtual pretty time number wedding siren private narrow sign provide require black" --coin=BTC  --numderive=3 --cols=path,address,privkey,pubkey --format=json'

#p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
#output, err = p.communicate()
#p_status = p.wait()

#keys = json.loads(output)
#print(keys)


def derive_wallets(arg)):
    #Loop through the constants
    for a in arg:
        command = f'./derive -g --mnemonic={mnemonic} --coin={coin} --numderive=3 --cols=path,address,privkey,pubkey --format=json'
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        p_status = p.wait()

        keys = json.loads(output)
        print(keys)

