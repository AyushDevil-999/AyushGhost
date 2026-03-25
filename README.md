# AyushGhost v6.1 (Ghost control andoid)

AyushGhost ek powerful PHP-based tool hai jo automated payload generation aur tunneling (Cloudflare) provide karta hai. Iska use ethical hacking aur security testing ke liye kiya jata hai.
🛠️ Installation & Setup

Pehle terminal open karein aur niche diye gaye commands ko ek-ek karke paste karein:
Bash


🚀 How to Use
    # Repository clone karein:

    git clone https://github.com/azadproduction212-cyber/AyushGhost.git

# Directory mein jayein:

     cd AyushGhost

# Permissions allow karein:

    chmod +x *

# Tool run karein:

    php AyushGhost.php


# Tool start hone ke baad
[1] Deploy option select karein.

Cloudflare link generate hone tak wait karein.

 Apna LHOST (Ngrok TCP link ya Local IP) aur LPORT enter karein.

Payload pub/ folder mein System_Update.apk naam se save ho jayega.

 Victim ko link bhejein, download hote hi listener start karein.

# ⚠️ Common Errors & Fixes

Agar tool chalne mein koi dikat aaye, toh ye try karein:

Cloudflared Not Found: Agar link generate nahi ho raha, toh check karein ki cloudflared install hai ya nahi.

# Fix:(kali)
    sudo dpkg -i cloudflared.deb 
 # Fix (termux)
    pkg install cloudflared 

 MSFVenom Error: Agar APK build nahi ho rahi.

Fix: Check karein ki Metasploit installed hai. msfvenom -v type karke check karein.

 Permission Denied: Agar "Permission Denied" aaye.

       chmod +x AyushGhost.php

 Port 8080 Busy: Agar server start nahi ho raha karke purane process band karein.

         pkill -f php
        


# ⚠️Disclaimer:
Yeh tool sirf educational purposes ke liye hai. Kisi bhi illegal activity ke liye author zimmedar nahi hoga.
