from os import path
from os import getcwd

ROOT = path.join(getcwd(), '..')
QUEUE = path.join(ROOT, 'DownloadQueue.txt')
TEMP = path.join(__file__, 'temp')
FINAL_FILES = path.join(ROOT, 'downloads')
