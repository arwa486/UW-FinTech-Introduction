# UW FinTech Bootcamp Homework 19 


## Project Setup 

See the *requirements.txt* for the Python libraries needed for the project. 

- Open a terminal window and create a directory `wallet`. 
- `cd` into `wallet`
- Clone the [hd-wallet-derive][1] with the following code: 
```
git clone https://github.com/dan-da/hd-wallet-derive
cd hd-wallet-derive
curl https://getcomposer.org/installer -o installer.php
php installer.php
php composer.phar install 
```

- Create a symbolic link to the `hd-wallet-derive/hd-wallet-derive.php`:
`ln -s hd-wallet-derive/hd-wallet-derive.php derive`


## Setup the Python files

- Create a file `wallet.py`

- Create a file `constants.py` with the following constants: 
``` 
BTC = 'btc'
ETH = 'eth' 
BTCTEST = 'btc-test'
```








[1]: https://github.com/dan-da/hd-wallet-derive