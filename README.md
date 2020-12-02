# tripleS

> Wise man once said: No software can give you the feeling of the switches, just the sound.

tripleS is a keyboard switches sound simulator for Linux and MacOS written in Python.

## Dependencies

### Packages

* `sox` => to play sounds
* `python-xlib` => required by `pyxhook`

### Python Libraries

* `pyxhook` => to listen to keyboard events

## Usage

```
usage: tripleS.py [-h] [-v VOLUME] -s SOUNDS

Keyboard switches sound simulator.

optional arguments:
  -h, --help            show this help message and exit
  -v VOLUME, --volume VOLUME
                        Volume of switch sound (float)
  -s SOUNDS, --sounds SOUNDS
                        Path to directory cotaining switches sounds. Have a look at https://github.com/PlankCipher/tripleS#sounds for more info

Examples:
  python tripleS.py -s sounds/modelm/
  python tripleS.py -s sounds/hhkb2_pro_topre -v 1.7
```

## Sounds

Currently, the supported file types are `wav` and `mp3`. The directory containing keyboard switches sounds you want to play can and must be specified via the `-s`/`--sounds` option.

The directory must contain the following so that the program accepts using it:
* A file called `enter.wav` or `enter.mp3` for the enter key sound.
* A file called `space.wav` or `space.mp3` for the space key sound.
* At least one file for the sound of the rest of the keys. The file can be called anything as long as it ends with `.wav` or `.mp3`. The more files you have for this, the more variety of sounds you get.

## Contributions

Contributions are highly appreciated, specially with sound files.

## Credits

The credit for `Model M` and `Happy Hacking Keyboard Professional 2` sounds goes to [millerjs](https://github.com/millerjs)