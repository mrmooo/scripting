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
# OneDrive Uninstall (save as ps1) #
```
# Terminate any OneDrive processes
taskkill /f /im OneDrive.exe

# Uninstall OneDrive
if ([Environment]::Is64BitOperatingSystem) {
    %SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall
} else {
    %SystemRoot%\System32\OneDriveSetup.exe /uninstall
}

# Moo-ve on with your day
Write-Output "OneDrive has been un-herd from this device. Time to moo-ve on to better things!"
```
