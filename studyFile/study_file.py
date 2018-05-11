#coding:utf-8
#获取文件内容
import os
print os.listdir('.')
f = file('studyFile/form.text')

tasks = f.readlines()

print ('tasks')
print (tasks)

f.close()

results = []
for task in tasks:
    data = task.split()

    for data_item in data:
        print data_item
        results.append (data_item)
    pass
pass
output = file('studyFile/result.txt', 'w')
output.writelines(results)
output.close()