#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import shutil


source = r"C:\Users\PALLAVI\OneDrive\Desktop\Codealpha projects\task2_automation_scripts\source_folder"
destination = r"C:\Users\PALLAVI\OneDrive\Desktop\Codealpha projects\task2_automation_scripts\jpg_files"

if not os.path.exists(source):
    print("Source folder not found.")
    exit()

if not os.path.exists(destination):
    os.makedirs(destination)


for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), os.path.join(destination, file))
        print(f"Moved: {file}")


print("Done.")

