[Setup]
AppName=David AI 2B
AppVersion=1.0
DefaultDirName={pf}\DavidAI2B
DefaultGroupName=David AI 2B
OutputDir=dist
OutputBaseFilename=DavidAI2BInstaller
SetupIconFile=static\david.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\run.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "models\*"; DestDir: "{app}\models"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\David AI 2B"; Filename: "{app}\run.exe"; WorkingDir: "{app}"
Name: "{group}\Uninstall David AI 2B"; Filename: "{uninstallexe}"
