cls
@ECHO OFF

title  MPS - Multipurpose Software 

if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK
if NOT EXIST Groove goto MDGroove
:CONFIRM
goto LOCK


goto CONFIRM
:LOCK
ren Groove "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
echo AEL
goto End
:UNLOCK
attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Groove
echo AEL
goto End
:FAIL
echo Invalid password
goto end
:MDGroove
md Groove
echo Groove created successfully
goto End
:End
