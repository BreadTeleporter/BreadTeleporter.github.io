import ctypes, sys, os
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # Code of your program here
    print("Welcome to msfampatcher")
    print("This program will remove Microsoft Family Safety from your system")
    print("Please make sure you have a backup of your system before you continue")
    print("This program will remove the following files:")
    print("WpcMon.exe")
    print("WpcTok.exe")
    print("Press enter to continue and accept that the creator is not responsible for any damage done to your pc")
    print("Please note that you should not run this script on the account you want to disable Family Safety on")
    print("Please make a new LOCAL account to run this script on as Family Saftey will not start on a LOCAL account.")
    print("Press ctrl+c to cancel")
    input()
    print("Removing WpcMon.exe")
    #Kill WpcMon.exe and WpcTok.exe
    try:
        ctypes.windll.kernel32.DeleteFileW(r'C:\Windows\System32\WpcMon.exe')
    except:
        print("Error removing WpcMon.exe")
    print("Removing WpcTok.exe")
    try:
        ctypes.windll.kernel32.DeleteFileW(r'C:\Windows\System32\WpcTok.exe')
    except:
        print("Error removing WpcTok.exe")
    print("Done")
    print("Please restart your computer")
    print("Press enter to exit")
    input()
    sys.exit()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
