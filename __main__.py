import glob 
from pathlib import Path 
from downloaded_rom.Utils import load_plug 
import logging
from . import bot 


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING) 

path = "Fonts/plugins/*.py"
files = glob.glob(path) 
 
for name in files: 
    with open(name) as a: 
      pxt = Path(a.name)
      plugs = pxt.stem
      load_plug(plugs.replace(".py", "")) 
     
print("FONTS BOT STARTED & LOADED ALL PLUGINS")
 
if name == "main":
  bot.run_until_disconnected()