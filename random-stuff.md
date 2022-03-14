**Unpin Microsoft Store**
Replace "Mail" with
- Microsoft Store
- Spotify
```
$appname = "Mail"
 ((New-Object -Com Shell.Application).NameSpace('shell:::{4234d49b-0245-4df3-b780-3893943456e1}').Items() | ?{$_.Name -eq $appname}).Verbs() | ?{$_.Name.replace('&','') -match 'Unpin from taskbar'} | %{$_.DoIt(); $exec = $true}
 ```
 
**CHOCO Software Installs**

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

**Dell Command utility updates (recommended)**
```
."C:\Program Files\Dell\CommandUpdate\dcu-cli.exe" /applyUpdates -updateSeverity=recommended -outputLog=C:\Temp\dell_command.log
```
