[Setup]
AppName=Nettools
AppVersion=1.0.0
DefaultDirName={pf}\Nettools
DefaultGroupName=Nettools
OutputDir=Output
OutputBaseFilename=nettools_setup

[Files]
Source: "dist\Nettools.exe"; DestDir: "{app}"
Source: "dist\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Nettools"; Filename: "{app}\Nettools.exe"
Name: "{commondesktop}\Nettools"; Filename: "{app}\Nettools.exe"

[Run]
Filename: "{app}\Nettools.exe"; Description: "Launch Nettools"; Flags: postinstall nowait skipifsilent