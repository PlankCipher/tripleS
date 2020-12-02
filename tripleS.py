import os
import pyxhook
import random
import argparse

continuous = False
last_key = None

parser = argparse.ArgumentParser(
    description='Keyboard switches sound simulator.')
parser.add_argument('-v', '--volume', type=float, default=1,
                    help='Volume of switch sound (float)')


args = parser.parse_args()


def KeyDownHandle(event):
    global continuous, last_key

    sound = 'sounds/modelm/'

    if event.Key == 'space':
        sound += 'space.wav'
    else:
        sound += f'{random.randint(1, 11)}.wav'

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
