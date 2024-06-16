const mineflayer = require('mineflayer')
const bot_count = process.argv[4]


class bot{
    constructor(botName){
        this.username = botName + process.argv[3]
        this.host = process.argv[2]
        this.joinServer()
    }
    startBotActions(){
        this.bot.once("login",() =>{
            this.bot.setControlState('jump',true)
        })
    }
    joinServer(){
        this.bot = mineflayer.createBot({
            "username":this.username,
            "host":this.host
        });
        this.startBotActions()
    }
}
const bots = []
for(let i = 1; i <= bot_count; i++){
    bots.push(new bot("Bot" + i))
}