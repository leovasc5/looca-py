from re import sub
from platform import system
from subprocess import getoutput
from psutil import cpu_percent
class Processor:
    def __init__(self):
        self.cpu = {}
    
        if(system() == 'Linux'):
            output = getoutput("awk '!$0{exit}1' /proc/cpuinfo")

            for i in output.splitlines():
                try:
                    self.cpu[sub('\t', '', i.split(': ')[0])] =  i.split(': ')[1]
                except:
                    pass

    def getInfo(self, info):
        try:
            return self.cpu[info]
        except NameError:
            return f"Can't return CPU vendor id\nError found: {NameError}"

    def getMinFrequency(self):
        try:
            output = getoutput("lscpu | grep MHz")
            x = sub('\n', '', output.split(':')[2])
            return sub(' ', '', x)
        except:
            return f"Can't return min frequency\nError found: {NameError}"

    def getMaxFrequency(self):
        try:
            output = getoutput("lscpu | grep MHz")
            x = sub('\n', '', output.split(':')[1])
            return sub(' ', '', x).split('C')[0]
        except:
            return f"Can't return max frequency\nError found: {NameError}"

    def getUsagePercent(self, percpu):
        try:
            return cpu_percent(percpu=percpu)
        except:
            return f"Can't return cpu usage\nError found: {NameError}"

    def getAll(self):
        try:
            # Include new methods
            return self.cpu
        except:
            return f"Can't return data\nError found: {NameError}"
    
    def help(self):
        print(f'Welcome to Looca!\n\nYou have access to this data on getInfo method:')

        for key in self.cpu.keys() :
            print(key)

        print('\n\nTo access the value of this data, just call the instance.Processor.getInfo(\'data name\') method. The method  will return a string with the corresponding value.')
        print('\nYou can also access the minimum and maximum CPU frequency by the respective methods: getMinFrequency() and getMaxFrequency.')
        print('\nIt is possible to get the estimated CPU usage (in percentage) by the getUsagePercent(Boolean) method. It is necessary to specify whether you need the general or individual value of each core.')
        print('\nGood luck!')

#Zona de Testes
Processor().help()