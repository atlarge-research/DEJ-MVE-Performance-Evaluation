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

let aBot = new bot("TestBot")