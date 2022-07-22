import subprocess
import time
import asyncio
import vars
from simple_term_menu import TerminalMenu
from tqdm import tqdm
from time import sleep
import psutil
import signal

class Gms(object):

    @staticmethod
    def getCmd(name, ctg):
        cmd = vars.cmds[name][ctg]
        if ctg == 'cmd':
            return cmd.split()
        else:
            #return description
            return cmd

    @staticmethod
    def runGetOutput(cmd):
        return subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout.read()

    @staticmethod
    def print_bold(text):
        print(vars.colors['BOLD'] + text + vars.colors['ENDC'])

    @staticmethod
    def print_green(text):
        print(vars.colors['GREEN'] + text + vars.colors['ENDC'])


    def __init__(self):
        # check for existence 
        if self.checkExists():
            self.initMenu()
        else:
            self.autoExecuteCmds('installServer')

    def checkExists(self):
        if len(Gms.runGetOutput(Gms.getCmd('checkUser', 'cmd'))) > 5:
            return 1
        else:
            return 0

    def initMenu(self):
        options = ["Server panel", "Show status", "Check update and fix", "Exit"]
        terminal_menu = TerminalMenu(options, title="GMS Panel " + vars.GMS['version'])
        menu_entry_index = terminal_menu.show()
        option = options[menu_entry_index]

        if option == 'Server panel':
            pass
        elif option == 'Show status':
            def initMenu(signum, frame): 
                signal.signal(signal.SIGINT, exit)
                self.initMenu()
            signal.signal(signal.SIGINT, initMenu)

            Gms.print_bold('Press Ctrl + C for exit.')
            with tqdm(total=100, desc='CPU (%)', position=1) as cpubar, tqdm(total=100, desc='RAM (%)', position=0) as rambar:
                while True:
                    rambar.n=psutil.virtual_memory().percent
                    cpubar.n=psutil.cpu_percent()
                    rambar.refresh()
                    cpubar.refresh()
                    sleep(0.1)
        elif option == 'Check update and fix':
            pass

    def autoExecuteCmds(self, name):
        cmdsBox = vars.cmdsBox[name]

        for i in range(0, len(cmdsBox)):
            if Gms.getCmd(cmdsBox[i], 'desc') != '':
                Gms.print_bold(vars.cmds[cmdsBox[i]]['desc'])
            subprocess.call(Gms.getCmd(cmdsBox[i], 'cmd'))