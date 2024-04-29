const mineflayer = require('mineflayer')


class bot{
    constructor(botName){
        this.username = botName
        this.joinServer()
    }
    startBotActions(){
        this.bot.once("login",() =>{
            this.bot.setControlState('forward',true)
            this.bot.setControlState('sprint',true)
            this.bot.setControlState('jump',true)
        })
    }
    joinServer(){
        this.bot = mineflayer.createBot({
            "username":this.username
        });
        this.startBotActions()
    }
}

let bots = []

for(let i = 0; i < 50; i++){
    bots.push(new bot("TestBot" + i))
}


