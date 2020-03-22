# Helper code to install all modules mentioned in requirements.txt

import subprocess
import sys


def install(package):
	subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def main():
	with open("requirements.txt", 'r') as f:
		for line in f:
			install(line.strip())


if __name__ == "__main__":
	main()
