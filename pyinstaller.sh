pyinstaller --noconfirm --log-level=WARN \
    --onefile --windowed --console \
    --add-data="README:." \
    --add-data="icon.png:img" \
    --upx-dir=/usr/local/share/ \
    mt-cc-firewall-test.spec