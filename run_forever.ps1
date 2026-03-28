Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

Set-Location -Path $PSScriptRoot

while ($true) {
    try {
        python main.py
    } catch {
        Write-Host "Bot crashed. Restarting in 5 seconds..."
    }
    Start-Sleep -Seconds 5
}
