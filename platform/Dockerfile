FROM platform_base_img

RUN mkdir /platform
RUN mkdir /platform/logs/

RUN ln -fs /usr/share/zoneinfo/Europe/Bucharest /etc/localtime

COPY init/wait-for /platform
RUN chmod 700 /platform/wait-for
COPY src /platform/src
COPY init/init.sh /platform/init.sh

RUN touch /platform/logs/error.log
RUN touch /platform/logs/access.log

RUN chown www-data:www-data /platform/logs/*

COPY requirements.txt /platform
RUN pip install -r /platform/requirements.txt

COPY init/platform.conf /etc/apache2/sites-available/platform.conf

RUN a2enmod rewrite
RUN a2enmod headers
RUN a2dissite 000-default.conf
RUN a2ensite platform.conf

EXPOSE 443
EXPOSE 80