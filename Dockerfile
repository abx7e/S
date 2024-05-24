FROM abs7e/abs7e:slim-buster

#clonning repo 
RUN git clone https://github.com/abs7e/root/S
#working directory 
WORKDIR /root/BlackThonUB

# Install requirements
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/BlackThonUB/bin:$PATH"

CMD ["python3","-m","BlackThon"]
