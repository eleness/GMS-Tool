
# DONT TOUCH THIS PROPERTIES, IF YOU DONT KNOW WHAT IS IT

colors = {
    'BLACK' : '\033[98m',
    'HEADER' : '\033[95m',
    'OKBLUE' : '\033[94m',
    'OKCYAN' : '\033[96m',
    'OKGREEN' : '\033[32m',
    'WARNING' : '\033[93m',
    'FAIL' : '\033[91m',
    'ENDC' : '\033[0m',
    'BOLD' : '\033[1m',
    'UNDERLINE' : '\033[4m',
}

cfg = {
    'username':'gmodito'
}

cmds = {
    'checkUser' : { 
        'cmd' : 'getent passwd | grep ' + cfg['username'],
        'desc' : 'Checking exists user..' 
    },
    'addUser' : { 
        'cmd':'sudo adduser ' + cfg['username'],
        'desc': 'Adding new user for server.. (Set new password)'
    },
    'loginUser' : { 
        'cmd' : 'su ' + cfg['username'],
        'desc' : 'Login to a new user.. (Enter your password)'
    },

    'createNewDirectory' : { 
        'cmd' : 'mkdir content server Steam content/css',
        'desc' : 'Creating new directory..'
    },
    'cdSteam' : {
        'cmd':'sudo cd Steam',
        'desc':''
    },
    'installSteamCmd' : {
        'cmd':'wget http://media.steampowered.com/client/steamcmd_linux.tar.gz',
        'desc':'Installing SteamCmd...'
    },
    'unzipSteamCmd': {
        'cmd':'tar -xvzf steamcmd_linux.tar.gz',
        'desc':''
    },
    'installServer': {
        'cmd':'sudo ./steamcmd.sh +login anonymous +app_update 4020 validate +quit',
        'desc':'Installing server..'
    },
    'installRequiredLibs': {
        'cmd':'sudo apt-get install libstdc++6 lib32gcc1',
        'desc':'Installing required libs..'
    }
}

cmdsBox = {
    'installServer' : ['installRequiredLibs','createNewDirectory', 'cdSteam', 'installSteamCmd', 'unzipSteamCmd', 'installServer']
}

GMS = {
    'version':'1.0 beta'
}