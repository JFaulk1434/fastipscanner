#define MyAppName "Nettools"
#define MyAppVersion "1.0.0"
#define MyAppExeName "Nettools.exe"

[Setup]
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=Output
OutputBaseFilename={#MyAppName}_setup_{#MyAppVersion}

[Files]
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"
Source: "dist\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: postinstall nowait skipifsilent