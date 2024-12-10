from abstract.company import CompanyFactory
from abstract.gpu import Gpu
from abstract.monitor import Monitor
from msi.gpu import MsiGpu
from msi.monitor import MsiMonitor


class MsiFactory (CompanyFactory):
    def createGpu(self) -> Gpu:
        return MsiGpu()

    def createMonitor(self) -> Monitor:
        return MsiMonitor()