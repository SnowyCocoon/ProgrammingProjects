const Discord = require('discord.js');
const bot = new Discord.Client();

bot.on('message', (message) => {
    
        if(message.content == 'ping') {
           // message.reply('pong');
           message.channel.sendMessage('pong');
        }
        });
    
bot.login('MzY5NDg2NTU2ODYxNTYyODg2.DM4ZoQ.i3E4M_S0afpNRXmNvGnjQJx3tlo');