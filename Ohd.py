from pymem import *
from pymem.process import *
def main():
    try:
        mem = pymem.Pymem("HarshDoorstop-Win64-Shipping.exe")
        module = module_from_name(mem.process_handle, "HarshDoorstop-Win64-Shipping.exe").lpBaseOfDll
        offsets1 = [0x10, 0x110, 0x610, 0x758, 0x228, 0xA0, 0x3B0]

        def GetPointer(base, offsets):
            addr = mem.read_int(base)
            for i in offsets:
                if i != offsets[-1]:
                    addr = mem.read_int(addr + i)
            return addr + offsets[-1]

        def ammo_value():
            ammo = mem.read_int(GetPointer(module + 0x042A0D38, offsets1))
            return ammo

        while True:
            mem.write_int(GetPointer(module + 0x042A0D38, offsets1), 1000)
            print(str(ammo_value()))
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()