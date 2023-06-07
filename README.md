# rhinosystem

Upgrade and system info tool for Rhino Linux

# Building
Following dependencies are required
- python3-gi
- gir1.2-adw-1
- gir1.2-gtk-4.0
- gir1.2-vte-3.91
- libadwaita-1-0
- libvte-2.91-gtk4-0
- py-cpuinfo
- gettext
- desktop-file-utils
- meson

To build and install rhino-system simply run
```
sudo apt install python3-gi gir1.2-adw-1 gir1.2-gtk-4.0 gir1.2-vte-3.91 libadwaita-1-0 libvte-2.91-gtk4-0 py-cpuinfo gettext desktop-file-utils meson
cd rhino-system/
meson setup _build
sudo ninja -C _build install
sudo chmod +x /usr/local/bin/rhinosystem
```

To launch it run `rhinosystem` in your terminal or search for it in your desktop environment.

![a screenshot of the main rhino system page](https://user-images.githubusercontent.com/60044824/239697615-46fc10e0-9307-4665-9263-0053185cf2b2.png)
