# Quick utility to check recently uploaded Google Drive files
param(
    [int]$Max = 10
)

Write-Host "🔍 Checking Google Drive recent files (limit: $Max)..." -ForegroundColor Cyan
gdrive readonly recent --max $Max
