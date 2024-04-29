const mineflayer = require('mineflayer')

const bot = mineflayer.createBot({
    username: 'Player'
  })

bot.on('kicked', console.log)