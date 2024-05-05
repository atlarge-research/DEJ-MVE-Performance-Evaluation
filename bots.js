const mineflayer = require('mineflayer')
const directions = ["forward","back","left", "right"]

class bot{
    constructor(botName){
        this.username = botName
        this.direction = directions[(Math.random() * directions.length) | 0]
        this.joinServer()
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
const random = (Math.random() * 100000)



for(let i = 1; i <= 50; i++){
    num = Math.floor(i + random)
    bots.push(new bot("TestBot" + random))
}