#!/bin/bash  
tmux kill-session -a
cd ~/Portfolio-Project
git fetch && git reset origin/main --hard 
source python3-virtualenv/bin/activate   
pip install -r requirements.txt                        

tmux new -s newsession                                                 
source python3-virtualenv/bin/activate       
cd ~/Portfolio-Project/app                                           
flask run --host=0.0.0.0                          

#tmux detach     