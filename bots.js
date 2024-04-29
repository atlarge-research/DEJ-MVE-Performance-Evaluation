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




function addFiftyBots(i,bots){
    for(let j = i;j < (i + 50); j++){
        bots.push(new bot("TestBot" + j))
    }
    return (i+50)   
}

async function runFile(){
    let i = 0
    let bots = []
    i = addFiftyBots(i,bots)

    await sleep(10000)

    i = addFiftyBots(i,bots)

}

runFile()

