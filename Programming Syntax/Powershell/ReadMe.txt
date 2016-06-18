Power shell is a CUI, and has many similar properties to various shells
Unlike many shells, instead of passing information as text between various programs, it passes objects between programs
Powershell is a scripting language
Shares a lot of aliases with bash (in linux) and the cmd (in windows)
pipping stuff through "Get-Member" command will be your new best friend when you get started

Note:

Compiling/running
	Powershell by default restricts running powershell scripts. to set it to run local scrips, run
		Set-Executionpolicy remotesigned
	powershell is an interpriter, no compiling required
