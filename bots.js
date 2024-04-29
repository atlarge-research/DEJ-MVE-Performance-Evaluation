const mineflayer = require('mineflayer')


class bot{
    constructor(botName){
        this.username = botName
        this.joinServer()
    }

    joinServer(){
        this.bot = mineflayer.createBot({
            "username":this.username
        });
        bot.startBotActions()
    }

    startBotActions(){
        bot.once("login",() =>{
            bot.setControlState('forward',true)
        })
    }



}

let bots = []

for(let i = 0; i < 50; i++){
    bots.push(new bot("TestBot" + i))
}


