if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TechnicalDwip/2024 /2024
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /2024 
fi
cd /2024 
pip3 install -U -r requirements.txt
echo "Trying To Running By Royal's Speed 😜☠️"
python3 bot.py
