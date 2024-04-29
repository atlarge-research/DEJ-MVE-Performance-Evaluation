const mineflayer = require('mineflayer')


class bot{
    constructor(botName){
        this.username = botName
        this.joinServer();
    }

    initBot(){
        this.bot = mineflayer.createBot({
            "username":this.username
        });
    }



}

let bots = []

for(let i = 0; i < 10; i++){
    bots.push(new bot("TestBot" + i))
}


