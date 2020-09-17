from signalbot.plugins import PluginChat
from random import randint


class RandomPlugin(PluginChat):

    name_map = {
        '+14257706791': 'Sammo',
        '+447919078769': 'Tony',
        '+447590439752': 'Bridgo',
        '+447739149940': 'Finno',
        '+447742356201': 'HorseMan',
        '+447546358942': 'PonyGirl',
        '+447751182979': 'Tang',
        '+447709487480': 'Griff'
    }

    def triagemessage(self, message):
        if message.text == '/bot riceroll':
            self.reply('idiot')

        name = message.sender
        if name in self.name_map:
            name = self.name_map[name]

        if message.text.lower() not in ['/bot diceroll', '/bot 🎲']:
            return

        number = randint(1,6)

        self.reply(f'{name} rolled {number}')


__plugin_chat__ = RandomPlugin
