const SHA256 = require('crypto-js/sha256');

class Transaction{
    constructor(fromAdress, toAdress, amount){
        this.fromAdress = fromAdress;
        this.toAdress = toAdress;
        this.amount = amount;
    }
}

class Block{
    constructor(timestamp, transactions, previousHash = ''){
        this.timestamp = timestamp;
        this.transactions = transactions;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
        this.nonce = 0;
    }

    calculateHash(){
        return SHA256(this.previousHash + this.timestamp + JSON.stringify(this.transactions) + this.nonce).toString();
    }

    mineBlock(difficulty){
        while(this.hash.substring(0, difficulty) !== Array(difficulty+1).join("0")){
            this.nonce++;
            this.hash = this.calculateHash();
        }

        console.log("Block Mined: " + this.hash);
    }
}



class Blockchain{
    constructor(){
        this.chain = [this.createGenesisBlock()];
        this.difficulty = 3;
        this.pendingTransactions = [];
        this.miningReward = 100;
    }

    createGenesisBlock(){
        return new Block("01/01/2019", "Genesis block", "0");
    }

    getLatestBlock(){
        return this.chain[this.chain.length - 1];
    }
    //miners must choose the transactions they want to include in BTC and which not (block can only hold 1mb)
    minePendingTransactions(miningRewardAdress){
        let block = new Block(Date.now(), this.pendingTransactions);
        block.mineBlock(this.difficulty);

        console.log('block sucessfully mined!')
        this.chain.push(block);

        this.pendingTransactions = [
            new Transaction(null, miningRewardAdress, this.miningReward)
        ];
    }

    createTransaction(transaction){
        this.pendingTransactions.push(transaction);
    }

    getBalanceOfAdress(address){
        let balance = 0;

        for(const block of this.chain){
            for(const trans of block.transactions){
                if(trans.fromAdress === address){
                    balance -= trans.amount;
                }

                if(trans.toAdress === address){
                    balance += trans.amount;
                }
            }
        }

        return balance;
    }

    isChainValid(){
        for(let i=1; i < this.chain.length; i++)
        {
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i-1];

            if(currentBlock.hash !== currentBlock.calculateHash()){
                return false;
            }

            if(currentBlock.previousHash !== previousBlock.hash){
                return false;
            }


        }
        return true;
    }
}   




let CoCoin = new Blockchain();
CoCoin.createTransaction(new Transaction('address1', 'address2', 100));
CoCoin.createTransaction(new Transaction('address2', 'address1', 50));

console.log('\n Starting the miner...');
CoCoin.minePendingTransactions('CoCo-Address')

console.log('\nBalance of CoCo is', CoCoin.getBalanceOfAdress('CoCo-Address'));

console.log('\n Starting the miner...');
CoCoin.minePendingTransactions('CoCo-Address')

console.log('\nBalance of CoCo is', CoCoin.getBalanceOfAdress('CoCo-Address'));