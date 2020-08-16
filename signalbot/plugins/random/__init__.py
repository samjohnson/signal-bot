from signalbot.plugins import PluginChat
from random import randint


class RandomPlugin(PluginChat):

    name_map = {}

    def triagemessage(self, message):

        if message.text not in  ['/bot diceroll', '/bot 🎲']:
            return

        name = message.sender
        if name in self.name_map:
            name = self.name_map[name]

        number = randint(1,6)

        self.reply(f'{name} rolled {number}')


__plugin_chat__ = RandomPlugin
