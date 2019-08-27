# http://blogs.msdn.com/b/powershell/archive/2011/04/04/scaling-and-queuing-powershell-background-jobs.aspx

$jobs = @() #an array to keep track of started jobs
for ($i=0; $i -lt 10; $i++){
    $jobs = $jobs + (Start-job -ScriptBlock {"func0 running - job ?"}) #runs the job in the 'scriptblock' 
    #start job returns in job ID
}
$jobs | Get-job #returns the status of all jobs (or in this case) specified jobs
$jobs | wait-job | out-null #waits until the specified jobs are complete before continueing
$jobs | Receive-Job #get's the results of each job that ran, note: jobs won't return output is they are still running

#since Start-job starts an independent script, everything outside the call isn't in the scope of the job being run UNLESS EXPLICIDLY IMPORTED
$functions = { #some functions for use in the job
    function func1($t1){
        "func1 running - job $t1"
    }
}
$jobs = @()
for ($i=0; $i -lt 10; $i++){
    $jobs = $jobs + (Start-job -InitializationScript $functions -ScriptBlock { #uses the '-InitializationScript' to 'import' said functions
        param($t1) #used to handle arguments
        func1($t1)
    } -ArgumentList $i) #feeding arguments into the job, which is feed into the function
}
$jobs | wait-job | out-null
$jobs | foreach {$_ | Receive-Job}
