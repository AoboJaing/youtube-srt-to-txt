# coding : utf-8

import linecache

file_srt = open('Servos - working principle and homemade types.srt', 'r')
file_txt = open('newfile.txt', 'w')

cout=1
for (num, value) in enumerate(file_srt):
    if cout == 5:
        cout = 1
    if cout == 3:
        file_txt.write(linecache.getline('en-Servos - working principle and homemade types.srt', num+1))
        file_txt.write(value)
    cout += 1

file_srt.close()
file_txt.close()

