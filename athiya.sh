sudo yum update -y
sudo yum groupinstall -y "Server with GUI"
sudo systemctl set-default graphical.target
sudo systemctl isolate graphical.target
sudo yum install -y epel-release
sudo yum install -y xrdp
sudo systemctl start xrdp
sudo systemctl enable xrdp
sudo firewall-cmd --permanent --add-port=3389/tcp sudo firewall-cmd –reload
