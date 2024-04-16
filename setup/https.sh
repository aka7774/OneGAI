#!/usr/bin/bash

sudo apt -y install certbot python3-certbot-nginx

if [ ! -e /etc/nginx/conf.d/ssl.conf ]; then
  sudo mkdir /ai/www
  sudo cat <<'__END__' > /etc/nginx/conf.d/ssl.conf
server {
    server_name $1;
    location / {
        root /ai/www;
        index index.html;
    }
}
__END__
fi

sudo service nginx restart

sudo certbot --nginx -d $1
