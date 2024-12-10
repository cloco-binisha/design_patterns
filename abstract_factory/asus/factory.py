from abstract.company import CompanyFactory
from abstract.gpu import Gpu
from abstract.monitor import Monitor
from asus.gpu import AsusGpu
from asus.monitor import AsusMonitor


class AsusFactory (CompanyFactory):
    def createGpu(self) -> Gpu:
        return AsusGpu()

    def createMonitor(self) -> Monitor:
        return AsusMonitor()