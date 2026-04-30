import pygame
import time
import re
import math
from colorama import init

init()

RESET = "\033[0m"
BOLD = "\033[1m"

# ========= NEON GLOW FUNCTION =========
def neon_text(text, step):
    styled = ""
    for i, char in enumerate(text):
        r = int((math.sin(step + i*0.3) + 1) * 127)
        g = int((math.sin(step + i*0.3 + 2) + 1) * 127)
        b = int((math.sin(step + i*0.3 + 4) + 1) * 127)
        styled += f"\033[38;2;{r};{g};{b}m{char}"
    return styled + RESET

# ========= SAFE LRC LOADER =========
def load_lrc(file):
    lyrics = []
    pattern = re.compile(r"\[(\d+):(\d+\.\d+)\](.*)")

    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.match(line)
            if match:
                mins = int(match.group(1))
                secs = float(match.group(2))
                text = match.group(3).strip()
                total = mins * 60 + secs
                lyrics.append((total, text))

    return sorted(lyrics, key=lambda x: x[0])

# ========= MUSIC =========
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")

lyrics = load_lrc("song.lrc")

pygame.mixer.music.play()
start_time = time.time()

current = 0
indent = 0
step = 0

print()  # start at very top

while current < len(lyrics):
    now = time.time() - start_time

    if now >= lyrics[current][0]:

        spacing = " " * indent

        clean_format = f"{spacing}💖 {lyrics[current][1]} 💖"

        # shadow layer
        print(f"\033[38;2;50;50;50m{clean_format}{RESET}")

        # neon layer
        print(f"{BOLD}{spacing}{neon_text('💖 ' + lyrics[current][1] + ' 💖', step)}{RESET}\n")

        indent += 8   # controls diagonal angle
        step += 0.8
        current += 1

    time.sleep(0.01)

pygame.mixer.music.stop()