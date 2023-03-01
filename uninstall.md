# Uninstall Thunderbird #
```
# Moo-ve on over and let's moo-ve this thunderbird outta here!
# Specify the file path to the helper.exe file
$helperExe = 'C:\Program Files\Mozilla Thunderbird\uninstall\helper.exe'; if (Test-Path $helperExe) {
    # If the helper.exe file exists, it's time to say moo-bye to Thunderbird!
    Start-Process -FilePath $helperExe -ArgumentList '/S' -Wait
    Write-Output "Thunderbird has been successfully uninstalled. Moo-ve on to better email clients!"
} else {
    # If the helper.exe file does not exist, display a message
    Write-Output "The file '$helperExe' was not found. Looks like Thunderbird isn't moo-ving anywhere."
}
```
# Uninstall Thunderbird for BATCH (single like) #
```
IF EXIST "C:\Program Files\Mozilla Thunderbird\uninstall\helper.exe" (START "" "C:\Program Files\Mozilla Thunderbird\uninstall\helper.exe" /S) ELSE (ECHO Thunderbird is not Installed)
```
# Thunderbird Detection Script intune #
```
try{
    $helperExe = 'C:\Program Files\Mozilla Thunderbird\uninstall\helper.exe'
    if (Test-Path $helperExe) {
        Write-Output "Thunderbird is installed. Exit code 1"
        exit 1
    } else {
        Write-Output "Thunderbird is not installed. Exit code 0"
        exit 0
    }
}
catch{
    $errMsg = $_.Exception.Message
    write-host $errMsg
    exit 2
}
```
# Thunderbird Remediation Script intune #
```
try{
    $helperExe = 'C:\Program Files\Mozilla Thunderbird\uninstall\helper.exe'
    Start-Process -FilePath $helperExe -ArgumentList '/S' -Wait
    exit 0
}
catch{
    $errMsg = $_.Exception.Message
    write-host $errMsg
    exit 1
}
```
# OneDrive Uninstall (Intune Detection Script) #
```
$OneDrivePath = "$env:SYSTEMROOT\SysWOW64\OneDriveSetup.exe"
if (Test-Path $OneDrivePath) {
    Write-Output "OneDrive is installed."
    exit 1
} else {
    Write-Output "OneDrive is not installed."
    exit 0
}
```

# OneDrive Uninstall (Intune Remediation Script) #
```
# Kill OneDrive process
Stop-Process -Name OneDrive -Force -ErrorAction SilentlyContinue

# Uninstall OneDrive
$OneDriveSetup = "$env:SYSTEMROOT\SysWOW64\OneDriveSetup.exe"
if (Test-Path $OneDriveSetup) {
    Start-Process $OneDriveSetup -ArgumentList "/uninstall" -NoNewWindow -Wait
    if ($LASTEXITCODE -eq 0) {
        Write-Output "OneDrive uninstalled successfully."
        exit 0
    } else {
        Write-Output "Error uninstalling OneDrive. Exit code: $LASTEXITCODE"
        exit $LASTEXITCODE
    }
} else {
    Write-Output "OneDrive is not installed."
    exit 1
}
```
