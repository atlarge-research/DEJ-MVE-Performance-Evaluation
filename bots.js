const mineflayer = require('mineflayer')

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


async function createBots(num){
    for(let i = 0; i < num; i++){
        const bot = mineflayer.createBot({
            username: 'Player'
          })
        
        bot.setControlState('forward', true)
          
        bot.on('kicked', console.log)
    
        await sleep(10000)
    }    
}

createBots(5)