from signalbot.plugins import PluginChat
from random import randint

# For the script
import glob
import os
import csv

class CodStatsPlugin(PluginChat):

    def triagemessage(self, message):
        if message.text not in  ['/cod session']:
            return

        # Open the latest session stats
        out_path = "/var/www/html/cod/"
        files = glob.glob(f"{out_path}summary*")
        files.sort(key=os.path.getmtime)
        latest = files[-1]

        session_date = latest.split('summary-')[1].split('.')[0]
        repl_string = f"Session KPGs for {session_date}:\n"
        with open(latest, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                repl_string += f"{row[0]}: {float(row[1]):.2f}\n"

        self.reply(repl_string)


__plugin_chat__ = CodStatsPlugin
