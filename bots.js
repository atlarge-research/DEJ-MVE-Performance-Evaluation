const mineflayer = require('mineflayer')
const directions = ["forward","back","left", "right"]

class bot{
    constructor(botName){
        this.username = botName
        this.host = process.argv[2]
        this.direction = directions[(Math.random() * directions.length) | 0]
        this.joinServer()
    }
    startBotActions(){
        this.bot.once("login",() =>{
            // this.bot.setControlState(this.direction,true)
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
for(let i = 1; i <= 80; i++){
    bots.push(new bot("Bot" + i))
}