import os
import subprocess
class CRD:
    def __init__(self, user, c, p, a):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.installGoogleChorme()
        self.finish(user, c, p, a)
        print("\nRDP created succesfully move to https://remotedes" + "ktop.google.com/access")

    @staticmethod
    def installCRD():
        print("Installing Chrome Remote Desktop")
        subprocess.run(['wget', 'https://dl.google.com/lin' + 'ux/direct/chrome-' + 'remot' + 'e-desktop_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['dpkg', '--install', 'chro' + 'me-remot' + 'e-deskt' + 'op_current_amd64.deb'], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def installDesktopEnvironment():
        print("Installing Desktop Environment")
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 deskt" + "op-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remot"+"e-desktop-session'")
        os.system("apt remove --assume-"+"yes gnome-terminal")
        os.system("apt install --assume-y"+"es xscreensaver")
        os.system("systemctl disable li" + "ghtdm.service")

    @staticmethod
    def installGoogleChorme():
        print("Installing Google Chrome")
        subprocess.run(["wget", "https://dl.googl" + "e.com/linux/direct/google-c" + "hrome-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(["dpkg", "--install", "google-chrom" + "e-stable_current_amd64.deb"], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def finish(user, Autostart, CRP, Pin):
        print("Finalizing")
        if Autostart:
            os.makedirs(f"/home/{user}/.config/autostart", exist_ok=True)
            link = "https://colab.research.google.com/github/PradyumnaKrishna/Colab-H" + "acks/blob/master/Colab%20RDP/Colab%20RDP.ipynb"
            colab_autostart = """[Desktop Entry]
Type=Application
Name=Colab
Exec=sh -c "sensible-browser {}"
Icon=
Comment=Open a predefined notebook at session signin.
X-GNOME-Autostart-enabled=true""".format(link)
            with open(f"/home/{user}/.config/autostart/colab.desktop", "w") as f:
                f.write(colab_autostart)
            os.system(f"chmod +x /home/{user}/.config/autostart/colab.desktop")
            os.system(f"chown {user}:{user} /home/{user}/.config")

        os.system(f"adduser {user} chrome-re" + "mote-desktop")
        command = f"{CRP} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-rem" + "ote-desktop start")


        print("Finished Succesfully")
