from solcx import compile_standard
import json
from web3 import web3
import os
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()


compiled_sol = compile_standard(
    {
        "language": "solidity",
        "sources": {"simpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
with open("compiled_code.json", "ww") as file:
    json.dump(compiled_sol, file)
# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
# print(abi)
# install trufflesuite.com/ganache software now to proceed further
# install web3

#for connecting to ganache
#"http:/0.0.0.0:8545" has been taken from ganache webpage(RPC server) after install of ganache
#chain id 1337 address "0x350d0b19bb29d4674531d6f115237e16afce377c" has been taken from ganache webpage after install of ganache
# orivate key "5JYJWrRd7sbqEzL9KR9dYTGrxyLqZEhPtnCtcvhC5t8ZvWgS9iC" .lk/2o00ohas been taken from ganache webpage after install of ganache
w3 = web3(web3.HTTPProvider("https://rinkeby.infura.io/v3/0114b1ee19b340f6b5237751615e33ac"))
chain_id = 4
my_address="0x3505456THKHXS56232536478H90543JHY8"
#private_key="5JYJWrRd7sbqEzL9KR9dYTGrxyLqZEhPtnCtcvhC5t8ZvWgS9iC"
pricate_key= os.getenv("PRIVATE_KEY")


#create the contract in python
SimpleStorage=w3.eth.contract(abi=abi,bytecode=bytecode)
#print(SimpleStorage)
#then execute "python deploy.py" in terminal 

#Get the latest transaction
nonce=w3.eth.getTransactionCount(my_address)
#"print(nonce)" to check for execution with command "python deploy.py"-Result display as'0' because since no tranaction now.
# refer  1.solidity  vedio at 3:59:05


#1.Build a transaction
#2.Sign a transaction
#3.Send this signed transaction

#1.Build a transaction as follows
tranaction= SimpleStorage.constructor().buildTrnsaction({"chainId":chain_id,"from":my_address,"nonce":nonce})
# print(transaction) to check for execution with command "python deploy.py"-result will be display in binary code format

#create new file for python environment (.env)


#2.Sign a transaction now
signed_txn=w3.eth.account.sign_transaction(transaction,private_key-private_key)
print("Deploying contract....")

#3.Send this signed transaction for verification
tx_hash=w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!")
# refer  1.solidity  vedio at 4:08:30

# Working with the contract,you always need
# Contract Address
# Contract ABI
simple_storage=w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)
# Call -> simulate making the call and getting a return value
# Tranact -> Actually make a state change

#Initial value of favuorite number
print("Updating Contract...")
print(simple_storage.functions.retrive().call())
#print(simple_storage.functions.store(15).call())
store_transaction=simple_storage.functions.store(15).buildTransaction({"chainId":chain_id,"from":my_address,"nonce":nonce+1})
signed_store_txn=w3.eth.account.sign_transaction(store_transaction,private_key=private_key)
send_store_tx=w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt=w3.eth.wait_for_transaction_receipt(send_store_tx)
print("Updated!")
# print(simple_storage.functions.retrieve().call()) and then run the python deploy.py in terminal then the result will shows as below
# line1-"Deployed contract..." line2-"Deployed!" line3-"0" line4-"updating contract..."line5-"Updated!"line6-"15"
# refer  1.solidity  vedio at 4:17:30

# Download node & install from web"nodejs.org/en/dpwnload" to proceed further
# then run "npm install --global yarn" in terminal command to proceed further
# then run "yarn global add ganache-cli"in terminal command to proceed further
# then run command "ganache-cli --deterministic" => will get "AVAILABLE ACCOUNTS,PRIVATE KEYS(FOR AVAILABLE ACCOUNTS),LISTENING ON-127.0.0.1:8545,GAS PRICE,GAS LIMIT)
# update line40 as "w3 = web3(web3.HTTPProvider("http:/127.0.0.1:8545))" from LISTENING ON instead of "w3 = web3(web3.HTTPProvider("http:/0.0.0.0:8545"))"
# update line42 as "my_address="0x75WE89THKHXS56232536478H90543JHY8" from AVAILABLE ACCOUNTS instead of "my_address="0x3505456THKHXS56232536478H90543JHY8"
# update private key at .env as "0x859T5JYJWrRd7sbqEzL9KR9dYTGrLqZEhPtnCtcvhC5t8ZEG" from PRIVATE KEYs instead of "5JYJWrRd7sbqEzL9KR9dYTGrxyLqZEhPtnCtcvhC5t8ZvWgS9iC"
# refer  1.solidity  vedio at 4:22:00

# create new account in infura.io for check testnet/mainnet then create a new project"freecodecamp-brownie"
# update line40 https://rinkeby.infura.io/v3/0114b1ee19b340f6b5237751615e33ac from new project"freecodecamp-brownie" 
# update line41 as chain_id = 4 instead of chain_id =1337 from https://chainlist.org/ for rinkeby Testnet
# similaly change private key & public address from metamask wallet  rinkeby test network
# refer  1.solidity  vedio at 4:26:00


















