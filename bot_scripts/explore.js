const mineflayer = require('mineflayer')
const { pathfinder, Movements, goals: { GoalNear } } = require('mineflayer-pathfinder')
const bot_count = parseInt(process.argv[4])
const Entity = require("prismarine-entity")('1.8.9')

class Bot {
    constructor(botName) {
        this.username = botName + process.argv[3]
        this.host = process.argv[2]
        this.joinServer()
    }

    async startBotActions() {
        this.bot.once("spawn", async () => {
            this.bot.loadPlugin(pathfinder)
            const botMovements = new Movements(this.bot, this.bot.mcData) 
            this.bot.pathfinder.setMovements(botMovements)
            
            var goal_location = this.bot.entity.position.clone() 
            goal_location.x += (Math.random() - 0.5) * 10000
            goal_location.z += (Math.random() - 0.5) * 10000
            const goal = new GoalNear(goal_location.x, goal_location.y, goal_location.z, 100)
            
            try {
                await this.bot.pathfinder.goto(goal)
                console.log(`${this.bot.username} has reached the goal.`)
            } catch (err) {
                console.error(`${this.bot.username} failed to reach the goal:`, err)
            }
        })
    }

    joinServer() {
        this.bot = mineflayer.createBot({
            "username": this.username,
            "host": this.host
        });
        this.bot.once('login', () => {
            const mcData = require('minecraft-data')(this.bot.version)
            this.bot.mcData = mcData
            this.startBotActions()
        })
    }
}

const bots = []
for (let i = 1; i <= bot_count; i++) {
    bots.push(new Bot("Bot" + i))
}
