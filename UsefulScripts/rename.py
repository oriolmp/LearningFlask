import shutil
import numpy as np


names = os.listdir("./path")
new_names = []
for i in range(len(names)):
    new_names = np.append(new_names, str(i).zfill(4))

for i, fname in enumerate(names):
    original_name = os.path.join("./path", fname)
    new_name = os.path.join("./path", new_names[i] + '.png')
    os.rename(original_name, new_name)

