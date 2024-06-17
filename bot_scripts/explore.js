const mineflayer = require('mineflayer')
const { pathfinder, Movements, goals:{ GoalNear} } = require('mineflayer-pathfinder')
const bot_count = process.argv[4]
const Entity = require("prismarine-entity")('1.8.9')



class bot{
    constructor(botName){
        this.username = botName + process.argv[3]
        this.host = process.argv[2]
        this.joinServer()
    }
    async startBotActions(){
        this.bot.once("spawn", async() =>{
            this.bot.loadPlugin(pathfinder)
            const botMovements = new Movements(bot)
            this.bot.pathfinder.setMovements(botMovements)
            var goal_location = this.bot.entity.position
            goal_location.x += (Math.random() - 0.5)*10000
            goal_location.z += (Math.random() - 0.5)*10000
            const goal = new GoalNear(goal_location.x,goal_location.y,goal_location.z,100)
            await this.bot.pathfinder.goto(goal)
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