import sys
import logging 
import importlib 
from pathlib import Path 

def load_plug(plug_name): 
   path = Path(f"Fonts/plugins/{plug_name}.py")
   name = "Fonts.plugins.{}".format(plug_name) 
   spec = importlib.util.spec_from_file_location(name, path) 
   load = importlib.util.module_from_spec(spec) 
   load.loader = logging.getLogger(plug_name) 
   spec.loader.exec_module(load) 
   sys.modules["Fonts.plugins." + plug_name] = load 
   print("FONTS loaded" + plug_name)