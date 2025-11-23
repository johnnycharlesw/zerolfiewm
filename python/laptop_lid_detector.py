from evdev import InputDevice, list_devices, ecodes
class LidFinder:
    def find_lid_device():
        for path in list_devices():
            dev = InputDevice(path)
            # Check capabilities for SW_LID only
            capabilities = dev.capabilities().get(ecodes.EV_SW, [])
            if ecodes.SW_LID in capabilities:
                return dev
        return None

    def __init__(self):
        lid_device = self.find_lid_device()

        if lid_device:
            print(f"Found lid device: {lid_device.path} ({lid_device.name})")
        else:
            print("No lid device found.")

        self.lid_device=lid_device
