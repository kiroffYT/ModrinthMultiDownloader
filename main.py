from rich.console import Console
from maxgradient import Gradient
import sys
import lliisstt
import os
from datetime import date

console = Console() # Initialize a console

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    console.print(
        "Использование: main.py -mode [client/server] -loader [название загрузчика/ядра (в зависимости от режима)]\n",
        "-version [версия Minecraft] -modlist [путь к списку модов]\n",
        "\n",
        "-modlist - путь к текстовому фалу, который содержит все моды, которые\n",
        "           нужно установить. Временно только в папке с кодом.\n",
        "\n",
        "-mode - указание на то, для чего загружаются указанные моды - для клиенсткой\n",
        "        версии Minecraft или для его серверного ядра.\n",
        "\n",
        "-version - версия игры, для которой загружаются моды.\n",
        "\n",
        "Синтаксис файла со списком модов:\n",
        "\n",
        "(названия модов, каждый с новой строки)",
        "\n",
        "\n",
        "[#ff44444]ПРЕДУПРЕЖДЕНИЕ: [/]В связи с тем, что данная программа находится\n",
        "в стадии разработки, могут загружаться не те моды, либо не загружаться вовсе.\n"
    )
elif sys.argv[1] == "-mode" and sys.argv[2] == "client":
    if sys.argv[3] == "-loader":
        if sys.argv[4] in lliisstt.server_loaders or sys.argv[4] in lliisstt.client_loaders:
            if sys.argv[5] == "-version":
                if len(sys.argv) > 6:
                    console.clear()
                    console.print(
                        Gradient("     _____        _____                                                    \n", justify="center", colors=["green","cyan","blue"]),
                        Gradient(" ___|    _|__  __|___  |__  _____  ____    ______  __  __  ______  _____   \n", justify="center", colors=["green","cyan","blue"]),
                        Gradient("|    \  /  | ||   ___|    ||     ||    \  |   ___||  |/ / |   ___||     |  \n", justify="center", colors=["green","cyan","blue"]),
                        Gradient("|     \/   | ||   |__     ||    _||     \ |   |__ |     \ |   ___||     \  \n", justify="center", colors=["green","cyan","blue"]),
                        Gradient("|__/\__/|__|_||______|  __||___|  |__|\__\|______||__|\__\|______||__|\__\ \n", justify="center", colors=["green","cyan","blue"]),
                        Gradient("    |_____|      |_____|                                                   \n", justify="center", colors=["green","cyan","blue"]),
                        Gradient("                                                                           \n", justify="center", colors=["green","cyan","blue"]),
                        Gradient("     C   R   E   A   T   E   D       B   Y      K   I   R   O   F   F      \n", justify="center", colors=["green","cyan","blue"]),
                        "\n",
                        "\n",
                        "Пожалуйста, подождите...",
                        "\n"
                    )
                    if sys.argv[7] == '-modlist' and len(sys.argv) > 8:
                        try:
                            mod_list = open(sys.argv[8], 'r+', encoding='utf-8')
                            raw_mod_list = [line.strip() for line in mod_list.readlines()]
                            not_founded_mods = []
                            for mod in raw_mod_list:
                                mod_url = lliisstt.find_mod(mod, sys.argv[6], sys.argv[4])
                                if mod_url != False:
                                    console.print(f'Загружаю мод {mod}...\n')
                                    os.system(f'curl -f -# -O {mod_url}')
                                elif mod_url == False:
                                    print(f'Не найден мод: {mod}')
                                    not_founded_mods.append(mod)
                            if len(not_founded_mods) == 0:
                                console.print('[#00aa00]Успешно загружены все моды.[/]\n')
                            elif len(not_founded_mods) > 0:
                                console.print('[#aaaa00]Не найденные моды:[/]\n')
                                for not_founded_mod in not_founded_mods:
                                    console.print(f'• {not_founded_mod}\n')
                            os.mkdir(f'{date.today()}')
                            os.system(f'move *.jar {date.today()} > nul')
                        except FileNotFoundError:
                            console.print(
                                "[#ff0000]Ошибка[/]\n",
                                "\n",
                                f"[#ff0000]Файл с именем {sys.argv[2]} не найден.[/]"
                            )
if len(sys.argv) <= 2:
    console.print('[#ff4444]Ошибка: не указаны аргументы для корректной работы программы.[/]\n')
    console.print('Помощь: main.py -h')