


from asus.factory import AsusFactory
from msi.factory import MsiFactory


if __name__ == "__main__":
    msi = MsiFactory()
    msiGpu = msi.createGpu()
    msiGpu.assemble()
    msiMonitor = msi.createMonitor()
    msiMonitor.assemble()

    asus = AsusFactory()
    asusGpu = asus.createGpu()
    asusGpu.assemble()
    asusMonitor = asus.createMonitor()
    asusMonitor.assemble()