tshark -r dump.pcap -T fields -e ip.src -e dns.qry.name -2R 'dns.flags.response eq 0' | awk -F" " '{ print $2 }' | rev | cut -d . -f -2 | rev | sort -u > ./db/domain.txt



