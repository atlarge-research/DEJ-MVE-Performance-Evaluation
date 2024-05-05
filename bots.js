const mineflayer = require('mineflayer')
const directions = ["forward","back","left", "right"]

class bot{
    constructor(botName){
        this.username = botName
        this.joinServer()
        this.direction = directions[(Math.random() * directions.length) | 0]
    }
    startBotActions(){
        this.bot.once("login",() =>{
            this.bot.setControlState(this.direction,true)
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
const bots = []
const random = (Math.random() * 1000)



for(let i = 0; i < 50; i++){
    num = i + random
    bots.push(new bot("TestBot" + random))
}