from solcx import compile_standard
import json
from web3 import web3
import os

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
w3 = web3(web3.HTTPProvider("http:/0.0.0.0:8545"))
chain_id = 13379
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
#3.Send a transaction

#1.Build a transaction as follows
tranaction= SimpleStorage.constructor().buildTrnsaction({"chainId":chain_id,"from":my_address,"nonce":nonce})
# print(transaction) to check for execution with command "python deploy.py"-result will be display in binary code format

#create new file for python environment (.env)






