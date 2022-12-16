import psutil, platform, cpuinfo

class Processor:
    def __init__(self) -> None:
        pass

    def getName(self):
        return cpuinfo.get_cpu_info()['brand_raw']

    def getCPUvAmount(self):
        return cpuinfo.get_cpu_info()['count']


#Zona de Testes
print(Processor().getCPUvAmount())