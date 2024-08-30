# -*- coding: utf-8 -*-

import requests

server_loaders = ['paper', 'spigot', 'bukkit', 'folia', 'purpur', 'sponge']
client_loaders = ['fabric', 'forge', 'neoforge', 'quilt', 'liteloader']

def find_loader(loader, mode):
    if mode == 'server':
        for loaders in server_loaders:
            if loaders == loader:
                return True
        else:
            return False
    elif mode == 'client':
        for loaders in client_loaders:
            if loaders == loader:
                return True
        else:
            return False

def find_mod(mod, version, loader):
    if loader in server_loaders or loader in client_loaders:
        r = requests.get(f'https://api.modrinth.com/v2/project/{mod}/version?game_versions={version}&loader={loader}')
        if r.status_code == 200:
            for i in range(0, len(r.json())):
                selected_part = r.json()[i]
                if version in selected_part["game_versions"] and loader in selected_part["loaders"]:
                    return selected_part["files"][0]["url"]
            else:
                return False # This is a sign that no such mod has been found.
        elif r.status_code == 404:
            return False
    elif loader not in server_loaders:
        if loader not in client_loaders:
            return False