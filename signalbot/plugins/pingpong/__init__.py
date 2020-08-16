from signalbot.plugins import PluginChat


class PingPongChat(PluginChat):

    def triagemessage(self, message):
        if message.text != '/bot ping':
            return

        self.reply(f'{message.sender}: pong')


__plugin_chat__ = PingPongChat
