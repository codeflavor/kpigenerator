# -*- coding: utf-8 -*-
import datetime
import random
import time
import psutil

charlist = 'AbCDeFgHijklmnopQrStuVwxyZ231_654987-'
multiplier = 10 # use the multiplier to increase/decrease the kpi value
hashno = 10 # number of KPIs a time series event should have
time_event = {} #the hash itself
sleep_timer = 1 * 5  # generate every 60 * n


kpi_types = {
    1: 'int',
    2: 'string',
    3: 'boolean',
    4: 'float',
}

def gen_name():
    """ Generate a random kpi name with the specified length
    add the random kpi to the hash
    """
    kpi_name = ''
    for i in range(random.randrange(4,10)):
        kpi_name = kpi_name + charlist[random.randrange(len(charlist))]
    return kpi_name

def gen_value(valtype=0, update=False):
    """ If we are updating the hash, only generate new values,
    nothing else
    """
    if not update:
        valtype = random.randrange(1,5)

    if kpi_types[valtype] == 'string':
        service_stat = ['running','faulted', 'offline']
        value_type = service_stat[random.randrange(1,3)]
    elif kpi_types[valtype] == 'int':
        value_type = random.randrange(0,100)
    elif kpi_types[valtype]  == 'boolean':
        bool_stat = ['False','True']
        value_type = bool_stat[random.randrange(2)]
    elif kpi_types[valtype] == 'float':
        value_type = random.randrange(1,100) / 2.5
    else:
        return
    return value_type, kpi_types[valtype]

def gen_def():
    """ Generate a kpi definition """
    timenow = str(datetime.datetime.utcnow())
    time_tag = {}
    print time_tag
    time_tag.setdefault('event',timenow)
    for i in range(hashno):
        value_type, kpi_gender = gen_value()
        kpi_name = gen_name()
        time_tag = inject_kpi(kpi_name, kpi_gender, value_type, timenow)
    print time_tag
    return time_tag

def inject_kpi(kpi_name, kpi_gender, value_type, timenow):
    time_event.setdefault(kpi_name, value_type)
    return time_event

def get_pc_metrics():
    cputime = psutil.cpu_times_percent(interval=1, percpu=False)
    return cputime

def main():
    while True:
        gen_def()
        print get_pc_metrics()
        time.sleep(sleep_timer)

if __name__ == '__main__':
    main()
