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
if (Test-Path -LiteralPath "C:\Users\user\AppData\Local\Microsoft\OneDrive\OneDrive.exe") 
{
   write-host "Installed - Onedrive"
   exit 1
}
else
{
    write-host "NOT installed - Onedrive"
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
    $exitCode = $?
    Write-Output "Uninstall OneDrive Exit code: $exitCode"
    if ($exitCode -eq $true) {
        Write-Output "OneDrive uninstalled successfully."
        exit 0
    } else {
        Write-Output "Error uninstalling OneDrive. Exit code: $exitCode"
        exit 1
    }
}
```
# App Uninstall (Intune Detection Script) #
```
#Detect built-in applications not needed for organisation devices

try
{
    # List of Applications to Remove
    $AppPackages  = @()
	$AppPackages += "*facebook*"
	$AppPackages += "Microsoft.Xbox.TCUI"
	$AppPackages += "Microsoft.XboxApp"
	$AppPackages += "Microsoft.XboxGamingOverlay"
	$AppPackages += "Microsoft.XboxIdentityProvider"
	$AppPackages += "Microsoft.XboxSpeechToTextOverlay"
	$AppPackages += "Microsoft.GamingApp"
	$AppPackages += "Microsoft.SkypeApp"
	$AppPackages += "MicrosoftTeams"
	$AppPackages += "Microsoft.ZuneMusic"
	$AppPackages += "Microsoft.ZuneVideo"
	$AppPackages += "Microsoft.WindowsFeedbackHub"
	$AppPackages += "Microsoft.BingNews"
	$AppPackages += "Microsoft.BingWeather"
	$AppPackages += "Microsoft.MicrosoftSolitaireCollection"
	$AppPackages += "Microsoft.WindowsMaps"
	$AppPackages += "Microsoft.GetStarted"
	$AppPackages += "Microsoft.People"
	$AppPackages += "Microsoft.windowscommunicationsapps"
	$AppPackages += "Microsoft.Messaging"
	$AppPackages += "Microsoft.MixedReality.Portal"
	$AppPackages += "Microsoft.YourPhone"
	$AppPackages += "Microsoft.Wallet"
	$AppPackages += "Microsoft.GetHelp"
	$AppPackages += "Microsoft.BingFinance"
	$AppPackages += "Dell.Optimizer"
	$AppPackages += "DellInc.DellDigitalDelivery"
	$AppPackages += "Microsoft.RemoteDesktop"
	$AppPackages += "*Skype*"
	$AppPackages += "*Spotify*"
	$AppPackages += "*Disney*"
	$AppPackages += "*Microsoft.Bing*"
	$AppPackages += "*Microsoft.ZuneVideo*"
	$AppPackages += "*officehub*"
	$AppPackages += "*windowsphone*"
	$AppPackages += "*windowsmaps*"
	$AppPackages += "*windowscommunicationsapps*"
	$AppPackages += "*Microsoft.Messaging*"
	$AppPackages += "*bingweather*"
	$AppPackages += "*solitairecollection*"
	$AppPackages += "*Microsoft.Asphalt8Airborne*"
	$AppPackages += "*king.com.CandyCrushSodaSaga*"
	$AppPackages += "*Microsoft.BingFinance*"
	$AppPackages += "*Netflix*"
	$AppPackages += "*Twitter*"
	$AppPackages += "*Candy*"
	$AppPackages += "*LinkedIn*"
	$AppPackages += "*Dell.Optimizer*"
	$AppPackages += "*DellInc.DellOptimizer*"
	$AppPackages += "*DellInc.DellDigitalDelivery*"
	$AppPackages += "*Promo*"
	$AppPackages += "*OneNote*"
	
    $Error.Clear()
    $found = $false
    foreach ($App In $AppPackages) 
    {
        $Package = Get-AppxPackage -allusers | Where-Object {$_.Name -like $App}
        $ProvisionedPackage = Get-AppxProvisionedPackage -Online | Where-Object {$_.DisplayName -like $App}
        If ($null -ne $Package) {
            Write-Host "App Found: $($Package.Name). Start remediation script."
            $found = $true
        } Else {
            Write-Host "Package $App not found."
        }
        If ($null -ne $ProvisionedPackage) {
            Write-Host "Provisioned App Found: $($ProvisionedPackage.DisplayName). Start remediation script."
            $found = $true
        } Else {
            Write-Host "Provisioned Package $App not found."
        }
    }
	
    If ($found) 
    {
        exit 1
    }
	Else {
		exit 0
	}
} 
catch
{
    $errMsg = $_.Exception.Message
    Write-Error $errMsg
    exit 1
}
```
# App Uninstall (Intune Remediation Script) #
```
#Uninstalls built-in applications not needed for organisation devices

# List of Applications to Remove
$AppPackages  = @()
	$AppPackages += "*facebook*"
	$AppPackages += "Microsoft.Xbox.TCUI"
	$AppPackages += "Microsoft.XboxApp"
	$AppPackages += "Microsoft.XboxGamingOverlay"
	$AppPackages += "Microsoft.XboxIdentityProvider"
	$AppPackages += "Microsoft.XboxSpeechToTextOverlay"
	$AppPackages += "Microsoft.GamingApp"
	$AppPackages += "Microsoft.SkypeApp"
	$AppPackages += "MicrosoftTeams"
	$AppPackages += "Microsoft.ZuneMusic"
	$AppPackages += "Microsoft.ZuneVideo"
	$AppPackages += "Microsoft.WindowsFeedbackHub"
	$AppPackages += "Microsoft.BingNews"
	$AppPackages += "Microsoft.BingWeather"
	$AppPackages += "Microsoft.MicrosoftSolitaireCollection"
	$AppPackages += "Microsoft.WindowsMaps"
	$AppPackages += "Microsoft.GetStarted"
	$AppPackages += "Microsoft.People"
	$AppPackages += "Microsoft.windowscommunicationsapps"
	$AppPackages += "Microsoft.Messaging"
	$AppPackages += "Microsoft.MixedReality.Portal"
	$AppPackages += "Microsoft.YourPhone"
	$AppPackages += "Microsoft.Wallet"
	$AppPackages += "Microsoft.GetHelp"
	$AppPackages += "Microsoft.BingFinance"
	$AppPackages += "Dell.Optimizer"
	$AppPackages += "DellInc.DellDigitalDelivery"
	$AppPackages += "Microsoft.RemoteDesktop"
	$AppPackages += "*Skype*"
	$AppPackages += "*Spotify*"
	$AppPackages += "*Disney*"
	$AppPackages += "*Microsoft.Bing*"
	$AppPackages += "*Microsoft.ZuneVideo*"
	$AppPackages += "*officehub*"
	$AppPackages += "*windowsphone*"
	$AppPackages += "*windowsmaps*"
	$AppPackages += "*windowscommunicationsapps*"
	$AppPackages += "*Microsoft.Messaging*"
	$AppPackages += "*bingweather*"
	$AppPackages += "*solitairecollection*"
	$AppPackages += "*Microsoft.Asphalt8Airborne*"
	$AppPackages += "*king.com.CandyCrushSodaSaga*"
	$AppPackages += "*Microsoft.BingFinance*"
	$AppPackages += "*Netflix*"
	$AppPackages += "*Twitter*"
	$AppPackages += "*Candy*"
	$AppPackages += "*LinkedIn*"
	$AppPackages += "*Dell.Optimizer*"
	$AppPackages += "*DellInc.DellOptimizer*"
	$AppPackages += "*DellInc.DellDigitalDelivery*"
	$AppPackages += "*Promo*"
	$AppPackages += "*OneNote*"
$Error.Clear()
foreach ($App In $AppPackages) {

    $Package = Get-AppxPackage -allusers | Where-Object {$_.Name -like $App}
	$ProvisionedPackage = Get-AppxProvisionedPackage -allusers -Online | Where-Object {$_.DisplayName -like $App}
	
    If ($Package -ne $null) {
        Write-Host "Removing Package : $App"
        Remove-AppxPackage -allusers -Package $Package.PackageFullName
    } 
	Else {
		Write-Host "Package $App not found"
	}

	If ($ProvisionedPackage -ne $null) {
		Write-Host "Removing ProvisionedPackage : $App"
		Remove-AppxProvisionedPackage -allusers -online -Packagename $ProvisionedPackage.Packagename
	} 
	Else {
		Write-Host "Provisioned Package $App not found"
	}
}
```

