const mineflayer = require('mineflayer')

class Bot{
    constructor(Name){
        this.username=Name 
        this.joinServer()
    }
    joinServer(){
        this.bot = mineflayer.createBot({"username":this.username})
    }
    lifecycle(){
        this.bot.on('end',()=> {setTimeout(() => this.joinServer, 5000)})
    }

}

let bots = [];

for(var i = 0; i < 6; i++){
    bots.push(new Bot('bot number #{i}'))
}



