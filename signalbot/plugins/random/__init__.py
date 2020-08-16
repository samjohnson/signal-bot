from signalbot.plugins import PluginChat
from random import randint


class RandomPlugin(PluginChat):

    name_map = {}

    def triagemessage(self, message):

        name = message.sender
        if name in self.name_map:
            name = self.name_map[name]

        if message.text.lower() not in ['/bot diceroll', '/bot 🎲']:
            self.reply(name + ' is chatting shit: ' + message.text)
            return

        number = randint(1,6)

        self.reply(f'{name} rolled {number}')


__plugin_chat__ = RandomPlugin
