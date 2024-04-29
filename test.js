const mineflayer = require('mineflayer')
const bot = mineflayer.createBot()


bot.once("login", () => {
    bot.setControlState('jump', true)
  });