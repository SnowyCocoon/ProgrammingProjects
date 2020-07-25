bot.on('message', (message) => {
    
        if(message.content == 'ping') {
           // message.reply('pong');
           message.channel.sendMessage('pong');
        }
    
    })

    // Do wysyłania wiadomości discord.js










const commando = require('discord.js-commando');
const bot = new commando.Client();

bot.registry.registerGroup('random', 'Random');
bot.registry.registerDefaults();
bot.registry.registerCommandsIn(__dirname + "/commands");

bot.login('MzY5NDg2NTU2ODYxNTYyODg2.DM4ZoQ.i3E4M_S0afpNRXmNvGnjQJx3tlo');

//kod do commando









