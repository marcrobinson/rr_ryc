### Enable logging ###
StartDetailedLoging()
StartUserLog()

### Wait for the lights ###
print "HHIIIIIII"
print "\n\n\n\ "+str(Globals.running)+"\n\n\n"

AimForLane(0)

Speed(100)

#WaitForGo()



print "HHIIIIIII2"

### Racing until terminated ###
while Globals.running:
	# Wait until we reach the first corner
	WaitForWaypoint(2)
	# Wait until we reach the start / finish line
	WaitForWaypoint(1)

### Wait for a few seconds ###
#WaitForSeconds(4)

### Disable logging ###
EndDetailedLog()
EndUserLog()

### End of the race ###
FinishRace()
