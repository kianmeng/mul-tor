".\.env\Scripts\activate" && pyinstaller --onedir --icon "icon.ico" --console --name "Mul-Tor" --upx-dir "Z:\Projects\Python\### UPX ###" --add-data="./.env/Lib/site-packages/grapheme/data/*;grapheme/data/" --hidden-import "plyer.platforms.win.filechooser" main.py && rmdir /s /q .\build && rmdir /s /q .\__pycache__ && del ".\Mul-Tor.spec" && pyinstaller --onefile --icon "icon.ico" --console --name "Mul-Tor" --upx-dir "Z:\Projects\Python\### UPX ###" --add-data="./.env/Lib/site-packages/grapheme/data/*;grapheme/data/" --hidden-import "plyer.platforms.win.filechooser" main.py && rmdir /s /q .\build && rmdir /s /q .\__pycache__ && del ".\Mul-Tor.spec"