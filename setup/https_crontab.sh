#!/bin/sh

cron_job_line="0 4 1 * * /usr/bin/certbot renew"
cron_file="/var/spool/cron/root"

[ -f ${cron_file} ] && touch ${cron_file}

cron_job_line_for_grep="${cron_job_line//\\/\\\\}"
if [ `grep "${cron_job_line_for_grep}" "${cron_file}" | wc -l` -eq 0 ] ; then
  echo "not registered yet. begin registering..."
  echo "${cron_job_line}" >> "${cron_file}"
else
  echo "already registered."
fi

# cron再起動
/etc/init.d/crond restart
