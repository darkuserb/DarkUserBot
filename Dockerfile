FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/bossuserb/BossUserBot.git /root/bossuserbot
WORKDIR /root/bossuserbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
