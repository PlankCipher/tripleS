import os
import pyxhook
import random
import argparse
from os import path, listdir
import re

continuous = False
last_key = None

parser = argparse.ArgumentParser(
    description='Keyboard switches sound simulator.')
parser.add_argument('-v', '--volume', type=float, default=1,
                    help='Volume of switch sound (float)')
parser.add_argument('-s', '--sounds', required=True, type=str,
                    help='Path to directory cotaining switches sounds. Have a look at https://github.com/PlankCipher/tripleS/#Sounds for more info')

args = parser.parse_args()

enter_path = ''
space_path = ''
others_paths = []

if not path.isdir(args.sounds):
    print('Couldn\'t parse sounds')
    exit()
else:
    files = listdir(args.sounds)

    if len(files) > 0:
        enter_re = re.compile('^enter\.(mp3|wav)$')
        space_re = re.compile('^space\.(mp3|wav)$')
        other_re = re.compile('^.+\.(mp3|wav)$')

        for file in files:
            if re.match(enter_re, file) != None:
                enter_path = file
            elif re.match(space_re, file) != None:
                space_path = file
            elif re.match(space_re, file) == None and re.match(enter_re, file) == None and re.match(other_re, file) != None:
                others_paths.append(file)
    else:
        print('Couldn\'t parse sounds')
        exit()

    if not enter_path or not space_path or len(others_paths) == 0:
        print('Couldn\'t parse sounds')
        exit()


def KeyDownHandle(event):
    global continuous, last_key

    sound = args.sounds

    if event.Key == 'space':
        sound = path.join(sound, space_path)
    elif event.Key == 'Return':
        sound = path.join(sound, enter_path)
    else:
        rand_index = random.randint(0, len(others_paths) - 1)
        sound = path.join(sound, others_paths[rand_index])

    if not continuous or event.Key != last_key:
        last_key = event.Key
        os.system(f'play -v {args.volume} {sound} 2> /dev/null &')
        continuous = True


def KeyUpHandle(event):
    global continuous
    continuous = False


hook = pyxhook.HookManager()
hook.KeyDown = KeyDownHandle
hook.KeyUp = KeyUpHandle
hook.HookKeyboard()

hook.start()
