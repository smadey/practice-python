import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = [r'C:\Users\C5193916\Desktop\python\module', r'C:\Users\C5193916\Desktop\python\data_structure']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = r'C:\Users\C5193916\Desktop\python\backup'

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory
today_dir = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = input('Enter a comment --> ')
if len(comment) == 0:
    target = today_dir + os.sep + now + '.zip'
else:
    target = today_dir + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today_dir):
    os.mkdir(today_dir)
    print('Successful created directory', today_dir)

# 5. Use the zip command (in Unix/Linux) or rar command (in Windows) to put the files in a zip archive
zip_command = r'rar a -r "%s" %s' % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to ', target)
else:
    print('Backup FAILED')