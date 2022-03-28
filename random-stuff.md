 # Unpin Microsoft Store # 
Replace "Mail" with
- Microsoft Store
- Spotify
```
$appname = "Mail"
 ((New-Object -Com Shell.Application).NameSpace('shell:::{4234d49b-0245-4df3-b780-3893943456e1}').Items() | ?{$_.Name -eq $appname}).Verbs() | ?{$_.Name.replace('&','') -match 'Unpin from taskbar'} | %{$_.DoIt(); $exec = $true}
 ```
 # Removing Windows apps # 
Additional package names
https://www.majorgeeks.com/content/page/remove_windows_10_apps_using_powershell.html
```
Get-AppxPackage *Microsoft.3dbuilder* | Remove-AppxPackage
Get-AppxPackage *AdobeSystemsIncorporated.AdobePhotoshopExpress* | Remove-AppxPackage
Get-AppxPackage *Microsoft.WindowsAlarms* | Remove-AppxPackage
Get-AppxPackage *Microsoft.Asphalt8Airborne* | Remove-AppxPackage
Get-AppxPackage *microsoft.windowscommunicationsapps* | Remove-AppxPackage
Get-AppxPackage *Microsoft.WindowsCamera* | Remove-AppxPackage
Get-AppxPackage *king.com.CandyCrushSodaSaga* | Remove-AppxPackage
Get-AppxPackage *Microsoft.DrawboardPDF* | Remove-AppxPackage
Get-AppxPackage *Facebook* | Remove-AppxPackage
Get-AppxPackage *BethesdaSoftworks.FalloutShelter* | Remove-AppxPackage
Get-AppxPackage *FarmVille2CountryEscape* | Remove-AppxPackage
Get-AppxPackage *Microsoft.WindowsFeedbackHub* | Remove-AppxPackage
Get-AppxPackage *Microsoft.GetHelp* | Remove-AppxPackage
Get-AppxPackage *Microsoft.Getstarted* | Remove-AppxPackage
Get-AppxPackage *Microsoft.ZuneMusic* | Remove-AppxPackage
Get-AppxPackage *Microsoft.WindowsMaps* | Remove-AppxPackage
Get-AppxPackage *Microsoft.Messaging* | Remove-AppxPackage
Get-AppxPackage *Microsoft.Wallet* | Remove-AppxPackage
Get-AppxPackage *Microsoft.MicrosoftSolitaireCollection* | Remove-AppxPackage
Get-AppxPackage *Todos* | Remove-AppxPackage
Get-AppxPackage *ConnectivityStore* | Remove-AppxPackage
Get-AppxPackage *MinecraftUWP* | Remove-AppxPackage
Get-AppxPackage *Microsoft.OneConnect* | Remove-AppxPackage
Get-AppxPackage *Microsoft.BingFinance* | Remove-AppxPackage
Get-AppxPackage *Microsoft.ZuneVideo* | Remove-AppxPackage
Get-AppxPackage *Microsoft.BingNews* | Remove-AppxPackage
Get-AppxPackage *Microsoft.MicrosoftOfficeHub* | Remove-AppxPackage
Get-AppxPackage *Netflix* | Remove-AppxPackage
Get-AppxPackage *OneNote* | Remove-AppxPackage
Get-AppxPackage *Microsoft.MSPaint* | Remove-AppxPackage
Get-AppxPackage *PandoraMediaInc* | Remove-AppxPackage
Get-AppxPackage *Microsoft.People* | Remove-AppxPackage
Get-AppxPackage *CommsPhone* | Remove-AppxPackage
Get-AppxPackage *windowsphone* | Remove-AppxPackage
Get-AppxPackage *Microsoft.Print3D* | Remove-AppxPackage
Get-AppxPackage *flaregamesGmbH.RoyalRevolt2* | Remove-AppxPackage
Get-AppxPackage *WindowsScan* | Remove-AppxPackage
Get-AppxPackage *AutodeskSketchBook* | Remove-AppxPackage
Get-AppxPackage *Microsoft.SkypeApp* | Remove-AppxPackage
Get-AppxPackage *bingsports* | Remove-AppxPackage
Get-AppxPackage *Office.Sway* | Remove-AppxPackage
Get-AppxPackage *Microsoft.Getstarted* | Remove-AppxPackage
Get-AppxPackage *Twitter* | Remove-AppxPackage
Get-AppxPackage *Microsoft3DViewer* | Remove-AppxPackage
Get-AppxPackage *Microsoft.WindowsSoundRecorder* | Remove-AppxPackage
Get-AppxPackage *Microsoft.BingWeather* | Remove-AppxPackage
Get-AppxPackage *Microsoft.XboxApp* | Remove-AppxPackage
Get-AppxPackage *XboxOneSmartGlass* | Remove-AppxPackage
Get-AppxPackage *Microsoft.XboxSpeechToTextOverlay* | Remove-AppxPackage
Get-AppxPackage *Microsoft.XboxIdentityProvider* | Remove-AppxPackage
Get-AppxPackage *Microsoft.XboxGameOverlay* | Remove-AppxPackage
```
Use an array for each loop
```
$AppList = @(
 "*Skype*"
 "*Spotify*"
 "*Disney*"
 "*Microsoft.ZuneVideo*"
	"*officehub*"
	"*windowsphone*"
	"*windowsmaps*"
	"*windowscommunicationsapps*"
	"*Microsoft.Messaging*"
	"*bingweather*"
	"*solitairecollection*"
	"*bingnews*"
)

foreach ($App in $AppList) {
    Get-AppxPackage -Name $App | Remove-AppxPackage -ErrorAction SilentlyContinue
}
```
 # Pull list of apps to TXT: # 
```
Get-AppxPackage > C:\temp\apps.txt
```

 # Pull specific apps in window: # 
```
get-appxpackage | findstr Microsof
```

 # CHOCO Software Installs # 

Template - https://gist.github.com/ferventcoder/1fd9a9a005079e20875d

String items together sample: 
```
choco install greenshot -y --force; choco install foxitreader -y --force; choco install libreoffice-fresh -y --force; choco install 7zip -y --force; choco install;choco install googlechrome -y --force; choco install vlc -y --force
```
```
choco install greenshot -y --force
choco install foxitreader -y --force
choco install libreoffice-fresh -y --force
choco install 7zip -y --force
choco install googlechrome -y --force
choco install vlc -y --force

choco install thunderbird -y --force
choco install office365business -y --force
choco install microsoft-teams.install -y --force
choco install adobereader -y --force
```

 # Dell Command utility updates (recommended) # 
```
."C:\Program Files\Dell\CommandUpdate\dcu-cli.exe" /applyUpdates -updateSeverity=recommended -outputLog=C:\Temp\dell_command.log
```

 # Disable News & Interts # 
```
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Feeds" /v EnableFeeds /t REG_DWORD /d 00000000 /f
```
 # Remove Search bar # 
```
reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search /v SearchboxTaskbarMode /t REG_DWORD /d 00000000 /f
```
 # Re-name workstation w/ prompt # 
```
$newpc = Read-Host -Prompt 'Input new PC-NAME LOC#-DT/LT-ROLE/USER';Rename-Computer -NewName "$newpc" -Force
```

 # Copy file & Set background image win10 #
```
# In order to get this  working, set the  execution policy
## Set-ExecutionPolicy RemoteSigned 
#setup items
New-Item -path "c:\scripts\deploy\" -ItemType "directory" -force

#copy files
$source_dir =  "\\1.3.3.7\public\deploy\background.jpg"
$dest_dir = "c:\scripts\deploy\"
$filepath = "c:\scripts\deploy\background.jpg"
Copy-Item -Path $source_dir -Destination $dest_dir -Force

#SETTING THE WALLPAPER
$setwallpapersrc = @"
using System.Runtime.InteropServices;

public class Wallpaper
{
  public const int SetDesktopWallpaper = 20;
  public const int UpdateIniFile = 0x01;
  public const int SendWinIniChange = 0x02;
  [DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
  private static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
  public static void SetWallpaper(string path)
  {
    SystemParametersInfo(SetDesktopWallpaper, 0, path, UpdateIniFile | SendWinIniChange);
  }
}
"@
Add-Type -TypeDefinition $setwallpapersrc

[Wallpaper]::SetWallpaper("$filepath")
```
