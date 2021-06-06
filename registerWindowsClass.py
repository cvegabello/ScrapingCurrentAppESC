import winreg

class WinRegistry:

    def readRegistry(self, nameAppStr, indexInt):
        with winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER) as hkey:
            with winreg.OpenKey(hkey, "Software",0, winreg.KEY_ALL_ACCESS) as sub_key:
                with winreg.OpenKey(sub_key, "IGT",0, winreg.KEY_ALL_ACCESS) as sub_key2:
                    with winreg.OpenKey(sub_key2, nameAppStr,0, winreg.KEY_ALL_ACCESS) as sub_key3:
                        pathStr = winreg.EnumValue(sub_key3,indexInt)
                        return pathStr[1]