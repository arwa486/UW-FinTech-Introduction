# Homework 18 


## Initialzing the Proof of Authority (PoA) Blockchain 

Start by creating new addresses in `geth` with separate `datadir` for the blockchain nodes. For ZBank, I initialized `acct` for each of the nodes to simulate customers of the bank. The code to initialize the nodes: 

`./geth --datadir <NODE NAME> account new`

Next running `puppeth` in the terminal (Git Bash on Windows) to initialize the blockchain. Use the *Clique (Proof of Authority)*  algorithm. Save a network name for the blockchain. Copy the addresses of the nodes created to link with the blockchain. Then export the genesis configuration block (output will be a `<NETWORK NAME>.json` file.) 

Next initialize the node with saved `<NETWORK NAME>.json` file: 

`./geth --datadir <NODE NAME> init <NETWORK NAME>.json`

## Setting up with MyCrypto for UI/UX
