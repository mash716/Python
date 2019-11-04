import os

PROJECT_DIR = 'C:¥python-izm'
SETTINGS_FILE = 'settings.ini'

print(os.path.join(PROJECT_DIR,SETTINGS_FILE))
print(os.path.join(PROJECT_DIR,'setting_dir',SETTINGS_FILE))

