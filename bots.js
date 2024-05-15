const mineflayer = require('mineflayer')
const directions = ["forward","back","left", "right"]

class bot{
    constructor(botName){
        this.username = botName
        this.host = "localhost"  //needs to be replaced with the server ib_ip
        this.direction = directions[(Math.random() * directions.length) | 0]
        this.joinServer()
    }
    startBotActions(){
        this.bot.once("login",() =>{
            this.bot.setControlState(this.direction,true)
            this.bot.setControlState('sprint',true)
            // this.bot.setControlState('jump',true) removed this since its ruining the sprint
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
const random = Math.floor((Math.random() * 100000))
const randomFactor = Math.floor((Math.random() * 200))

const randomNum = random * randomFactor


for(let i = 1; i <= 100; i++){
    num =   i + randomNum
    bots.push(new bot("Bot" + num))
}