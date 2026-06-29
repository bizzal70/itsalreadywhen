# setup_scheduler.ps1
# Creates two Windows Task Scheduler tasks:
#   1. Daily scraper  — runs every day at 6:00 AM
#   2. Weekly digest  — runs every Sunday at 8:00 AM (prompts before pushing)
#
# Run once as Administrator:
#   powershell -ExecutionPolicy Bypass -File setup_scheduler.ps1

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = (Get-Command python).Source

# --- Daily scraper ---
$dailyAction = New-ScheduledTaskAction `
    -Execute $python `
    -Argument "`"$scriptDir\scraper.py`"" `
    -WorkingDirectory $scriptDir

$dailyTrigger = New-ScheduledTaskTrigger -Daily -At "06:00"

$dailySettings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
    -RestartCount 2 `
    -RestartInterval (New-TimeSpan -Minutes 10)

Register-ScheduledTask `
    -TaskName "ItsAlreadyWhen_DailyScrape" `
    -Action $dailyAction `
    -Trigger $dailyTrigger `
    -Settings $dailySettings `
    -Description "Daily cybersecurity RSS scraper for It's Already When." `
    -RunLevel Highest `
    -Force

Write-Host "Daily scraper task created: runs every day at 6:00 AM" -ForegroundColor Green

# --- Weekly digest (Sunday 8 AM) ---
$weeklyAction = New-ScheduledTaskAction `
    -Execute $python `
    -Argument "`"$scriptDir\digest.py`"" `
    -WorkingDirectory $scriptDir

$weeklyTrigger = New-ScheduledTaskTrigger -Weekly -WeeksInterval 1 -DaysOfWeek Sunday -At "08:00"

Register-ScheduledTask `
    -TaskName "ItsAlreadyWhen_WeeklyDigest" `
    -Action $weeklyAction `
    -Trigger $weeklyTrigger `
    -Settings $dailySettings `
    -Description "Weekly digest generator for It's Already When." `
    -RunLevel Highest `
    -Force

Write-Host "Weekly digest task created: runs every Sunday at 8:00 AM" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Set your ANTHROPIC_API_KEY as a system environment variable"
Write-Host "  2. Make sure git is configured with push access to bizzal70/itsalreadywhen"
Write-Host "  3. Run scraper.py manually once to seed the database"
