const {Blockchain, Transaction} = require('./blockchain');

const EC = require('elliptic').ec;
const ec = new EC('secp256k1');

const myKey = ec.keyFromPrivate('41a84219c108252a219d967c3f46438da49fdd9c327dcc7d05e0a4483985c411');
const myWalletAddress = myKey.getPublic('hex');



let CoCoin = new Blockchain();

const tx1 = new Transaction(myWalletAddress, 'public key goes here', 10);
tx1.signTransaction(myKey);
CoCoin.addTransaction(tx1);

console.log('\n Starting the miner...');
CoCoin.minePendingTransactions(myWalletAddress)

console.log('\nBalance of CoCo is', CoCoin.getBalanceOfAdress(myWalletAddress));

console.log('\n Starting the miner...');
CoCoin.minePendingTransactions(myWalletAddress)

console.log('\nBalance of CoCo is', CoCoin.getBalanceOfAdress(myWalletAddress));