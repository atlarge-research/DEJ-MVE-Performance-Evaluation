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

const startnum = process.argv[2]
const bots = []

function addFiftyBots(i,bots){
    for(let j = i;j < (i + 50); j++){
        bots.push(new bot("TestBot" + j))
    } 
}
addFiftyBots(startnum,bots)