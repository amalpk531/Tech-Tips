# Tech-Tips
How To Remove Ads/Bloatware/Glance Screen from Realme Devices : No root | Uninstall System App

steps...............

1.download platform tools 
2.open terminal from "platform tools folder"
3.enable usb debugging in phone from ->developer options
4.connect data cable :phone -> pc
5.type following commands in cmd

#---------------for finding connected device--------------- 
	

		adb devices





#---------------------------for deleting system apps-----------

	adb shell pm uninstall --user 0 

[after this command type the package name of the app you want to delete


[eg: 	

	adb shell pm uninstall --user 0 com.netflix.mediaclient

and hit enter]

[[note: deleting core system apps will stuck your phone to bootloop]]



#-----------------------package names of apps that can be easily removed (realme) -------#

 App market➡️ com.heytap.market
 
▫️ Browser ➡️ com.heytap.browser

▫️ Music ➡️ com.oppo.music

▫️ Video ➡️ com.coloros.video

▫️ Calculator ➡️ com.coloros.calculator

▫️ File Manager ➡️ com.coloros.filemanager

▫️ Heytap Account ➡️ com.heytap.usercenter

▫️ Heytap Cloud ➡️ com.heytap.cloud

▫️ Game space ➡️ com.coloros.gamespaceui

▫️ Theme store ➡️ com.heytap.themestore

▫️ Search box ➡️ com.oppo.quicksearchbox

▫️ Clone phone ➡️ com.coloros.backuprestore

▫️ Smart screen ➡️ com.coloros.assistantscreen

▫️ Oroaming ➡️ com.redteamobile.roaming

▫️ Compass ➡️ com.coloros.compass2

▫️ Weather Service ➡️ com.coloros.weather.service

▫️ Weather ➡️ com.coloros.weather2

#---------------------google apps-------------------------------------------------#


▫️ Chrome ➡️ com.android.chrome

▫️ Keep notes ➡️ com.google.android.keep

▫️ Gmail ➡️ com.google.android.gm

▫️ Google duo ➡️ com.google.android.apps.tachyon

▫️ Google calendar ➡️ com.google.android.calendar

▫️ Google play movies ➡️ com.google.android.videos

▫️ Google photos ➡️ com.google.android.apps.photos

▫️ Map ➡️ com.google.android.apps.maps

▫️ Wellbeing ➡️ com.google.android.apps.wellbeing

▫️ YouTube ➡️ com.google.android.youtube

▫️ YouTube Music ➡️ com.google.android.apps.youtube.music




