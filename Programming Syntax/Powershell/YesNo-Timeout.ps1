function YesNo-TimeOut {
    #Gives a y/n prompt with a timeout, returns 'y','n',$null
    Param(
           [int]$seconds = 5,
        [string]$prompt = 'Hit a key'
    )

    $startTime = Get-Date
    $timeOut = New-TimeSpan -Seconds $seconds

    while((Get-Date) -lt ($startTime + $timeOut)){
        if ([console]::KeyAvailable) {
            $response = [System.Console]::ReadKey("NoEcho, IncludeKeyDown")
            #echo $response.Key
            if ($response.Key -contains 'y'){
                Write-Host $null #prints a new line
                return 'y'
            }
            if ($response.Key -contains 'n'){
                Write-Host $null #prints a new line
                return 'n'
            }
        }
        # there are 10000000 Ticks in a second
        $remainingTime = ([math]::Round((50000000 + ($startTime.Ticks - (Get-Date).Ticks))/10000000))
        $text = "[" + $prompt + " " + $remainingTime + " (Y/N)]" 
        Write-Host -NoNewline $text ("`r"*($text.Length))
        [Threading.Thread]::Sleep( 100 )
    }
    Write-Host $null #prints a new line
    return $null
}

echo (YesNo-TimeOut)
