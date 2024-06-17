const mineflayer = require('mineflayer')
const bot_count = parseInt(process.argv[4])
const Entity = require("prismarine-entity")('1.8.9')
const directions = ["forward","back","left", "right"]


class Bot {
    constructor(botName) {
        this.username = botName + process.argv[3]
        this.host = process.argv[2]
        this.direction = directions[(Math.random() * directions.length) | 0]
        this.joinServer()
    }

    async startBotActions() {
        this.bot.once("spawn", async () => {            
            var goal_location = this.bot.entity.position.clone() 
            goal_location.y += 60
            await this.bot.creative.flyTo(goal_location)
            this.bot.setControlState(this.direction,true)
        })
    }

    joinServer() {
        this.bot = mineflayer.createBot({
            "username": this.username,
            "host": this.host
        });
        this.bot.once('login', () => {
            this.startBotActions()
        })
    }
}

const bots = []
for (let i = 1; i <= bot_count; i++) {
    bots.push(new Bot("Bot" + i))
}