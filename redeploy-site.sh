#!/bin/bash  
cd ~/Portfolio-Project
git fetch && git reset origin/main --hard 
source python3-virtualenv/bin/activate   
pip install -r requirements.txt                        

systemctl start myportfolio
systemctl enable myportfolio 

systemctl daemon-reload 
systemctl restart myportfolio 
