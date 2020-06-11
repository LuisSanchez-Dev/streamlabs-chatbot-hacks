import clr
import System
clr.AddReference(
  [asm for asm in System.AppDomain.CurrentDomain.GetAssemblies() if "AnkhBotR2" in str(asm)][0]
)
import AnkhBotR2

clr.AddReference("System.Windows.Forms")
from System.Windows.Forms.MessageBox import Show
msgbox = lambda obj: Show(str(obj))

Creator = "LuisSanchezDev"
Description = "Programatically get the users' currency and hours"
ScriptName = "ExportUsersData"
Version = "1.0.0"
Website = "https://youtube.com/c/luissanchezdev"

def Init():
  data = GetUsersCurrencyData()
  msgbox(data)

def Execute(data):
  pass

def Tick():
  pass

def GetUsersCurrencyData():
  global_manager = AnkhBotR2.Managers.GlobalManager.Instance
  vm_locator = global_manager.VMLocator
  currency_view = vm_locator.CurrencyView
  users = currency_view.Users
  output = ""
  for entry in users:
    output += "{0},{1},{2},{3},{4}\n".format(
    entry.UserId,
    entry.User.Name,
    entry.Rank,
    entry.TimeWatched,
    entry.Points
  )
  return output