#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
;lets automate my mobilepass python script
!q::
if WinExist(%mobilepass%) {
MsgBox "mobilepass running"
WinKill %mobilepass%
}
RunWait, C:/Users/lwalters/AppData/Local/Programs/Python/Python310/pythonw.exe c:/Users/lwalters/github/lawrencewalters/autohotkey/mobilepassahk.py, c:/Users/lwalters/github.com/lawrencewalters/autohotkey/
return