#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Program to take the audio files in /source_sounds and create files at correct volume levels in the documents folder
# taken from https://stackoverflow.com/questions/51468895/changing-a-wav-files-volume-using-python with minor modification
import wave
from os import path
import os
from zipfile import ZipFile, ZIP_LZMA
import Create_filter
from random import choice

# 300 is max
volume = {
	"mirror": 200,
	"max": 175,
	"high": 100,
	"normal": 75,
	"medium": 45,
	"low": 20
}

# valid sound strings
volumes = ["mirror", "max", "high", "normal", "medium", "low"]

# folder for filter sounds
sound_root = 'source_sounds'

# each entry needs a list(len 6) of list(and len)
# blank entries will generate no sound
# using the same file in multiple areas will not generate multiple of the same sound
# multiple choices will be chosen from randomly
soundmap = {
	'divination': [['neutral3.wav'],
				   ['expl_2.wav'],
				   ['scroll.wav'],
				   ['scroll.wav'],
				   ['scroll.wav'],
				   ['scroll.wav']],
	'unique': [['neutral3.wav'],
			   ['expl_2.wav'],
			   ['amulet.wav'],
			   ['amulet.wav'],
			   ['amulet.wav'],
			   ['amulet.wav']],
	'map_good': [['neutral3.wav'],
				 ['flippy.wav'],
				 ['flippy.wav'],
				 ['flippy.wav'],
				 ['flippy.wav'],
				 ['flippy.wav']],
	'map_okay': [['neutral3.wav'],
				 ['expl_2.wav'],
				 ['charm.wav'],
				 ['charm.wav'],
				 ['charm.wav'],
				 ['charm.wav']],
	'challenge': [['neutral3.wav'],
				  ['expl_2.wav'],
				  ['death1.wav', 'death2.wav', 'death3.wav', 'death4.wav', 'death5.wav'],
				  ['attack1.wav', 'attack2.wav', 'attack3.wav', 'attack4.wav', 'attack5.wav', 'attack6.wav'],
				  ['gethit1.wav', 'gethit2.wav', 'gethit3.wav', 'gethit4.wav'],
				  ['gethit1.wav', 'gethit2.wav', 'gethit3.wav', 'gethit4.wav']],
	'currency': [['neutral3.wav'],
				 ['expl_2.wav'],
				 ['gold.wav'],
				 ['gold.wav'],
				 ['gold.wav'],
				 ['gold.wav']],
	'show': [['neutral3.wav'],
			 ['expl_2.wav'],
			 ['convert.wav'],
			 ['convert.wav'],
			 ['convert.wav'],
			 ['convert.wav']],
	'gem': [['neutral3.wav'],
			['expl_2.wav'],
			['gem.wav'],
			['gem.wav'],
			['gem.wav'],
			['gem.wav']],
	'base': [['neutral3.wav'],
			 ['expl_2.wav'],
			 ['charge.wav'],
			 ['charge.wav'],
			 ['charge.wav'],
			 ['charge.wav']],
	'5link': [['5link.wav'],
			  ['5link.wav'],
			  ['5link.wav'],
			  ['5link.wav'],
			  ['5link.wav'],
			  ['5link.wav']],

}


# converts a sound reference to the correct wav file.  Allows for random sounds within a tier.
# returns the index, what to replace, and what to replace it with
# returns -1 if nothing to replace
def convert_sound_reference(format_list):
	for idx in range(len(format_list)):
		if format_list[idx].startswith('CustomAlertSound'):
			sound = format_list[idx].split('"')[1]
			slist = sound.split('_', maxsplit=1)
			return idx, sound, f"{sound_root}/{choice(soundmap[slist[1]][volumes.index(slist[0])])}", volume[slist[0]]
	# nothing to change
	return [-1]


# OBSOLETE
def convert_wav(factor, inpath, outpath):
	pathout = "{}_{}".format(factor, inpath)
	factor = factor / 100
	with wave.open('source_sounds/{}'.format(inpath), 'rb') as fin, wave.open(f'{sound_root}/{pathout}', 'wb') as fout, wave.open(path.join(outpath, f'{sound_root}/{pathout}'), "wb") as f:
		fout.setparams(fin.getparams())
		f.setparams(fin.getparams())
		sampwidth = fin.getsampwidth()

		while True:
			frames = bytearray(fin.readframes(1024))
			if not frames:
				break

			for i in range(0, len(frames), sampwidth):
				if sampwidth == 1:
					# 8-bit unsigned
					frames[i] = int(round((sample[0] - 128) * factor + 128))
				else:
					# 16-, 24-, or 32-bit signed
					sample = int.from_bytes(frames[i:i + sampwidth], 'little', signed=True)
					quiet = round(sample * factor)
					try:
						frames[i:i + sampwidth] = int(quiet).to_bytes(sampwidth, 'little', signed=True)
					except OverflowError:
						if quiet < 0:
							frames[i:i + sampwidth] = int(-32768).to_bytes(sampwidth, 'little', signed=True)
						else:
							frames[i:i + sampwidth] = int(32767).to_bytes(sampwidth, 'little', signed=True)
			fout.writeframes(frames)
			f.writeframes(frames)


# OBSOLETE
# generate all sound combinations the filter may use
def package_sounds():
	poeDir = Create_filter.get_poe_path()
	# Delete existing wav files before creating new ones
	for file in os.listdir(sound_root):
		os.remove(os.path.join(sound_root, file))
	if os.path.isfile('soundpack.zip'):
		os.remove('soundpack.zip')
	if not os.path.isdir(path.join(poeDir, sound_root)):
		os.mkdir(path.join(poeDir, sound_root))
	for file in os.listdir(path.join(poeDir, sound_root)):
		if file.endswith('.wav'):
			os.remove(os.path.join(poeDir, f'{sound_root}/{file}'))
	# Create requested sound files
	soundlist = []
	for track in soundmap:
		for vol in range(len(volumes)):
			i = volume[volumes[vol]]
			for sound in soundmap[track][vol]:
				key = f'{i}_{sound}'
				print(key)
				if key not in soundlist:
					convert_wav(i, sound, poeDir)
					soundlist.append(key)
	# Create sound pack
	with ZipFile('soundpack.zip', mode='w', compression=ZIP_LZMA) as zipper:
		for track in soundlist:
			zipper.write(f'{sound_root}/{track}', arcname=f'{track}.wav')


# When this file is ran directly
if __name__ == "__main__":
	pass
#	package_sounds()
