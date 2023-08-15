if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Royal-Luku/Shinchan_V2_Shortner.git /Shinchan_V2_Shortner 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Shinchan_V2_Shortner 
fi
cd /Shinchan_V2_Shortner 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
