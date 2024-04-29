const mineflayer = require('mineflayer')
const directions = ["forward","back","left", "right"]

const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay))


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


let i = 0

function addFiftyBots(i){
    let bots = []
    for(i; i < i + 50; i++){
        bots.push(new bot("TestBot" + i))
    }
    return i    
}

i = addFiftyBots(i)
sleep(5000)
i = addFiftyBots(i)