from crontab import Crontab

with CronTab(user='root') as cron:
    job = cron.new(command='echo hello_world')
    job.minute.every(1)
    
print('cron.write() was just executed')
