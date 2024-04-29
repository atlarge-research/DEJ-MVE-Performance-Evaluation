const mineflayer = require('mineflayer')

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

for(let i = 0; i < 10; i++){
    const bot = mineflayer.createBot({
        username: 'Player'
      })
    
    
    bot.setControlState('forward', true)
      
    bot.on('kicked', console.log)

    await sleep(10000)
}

