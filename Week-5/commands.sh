grep 'GET /telugu/' s-anand.net-May-2024 | awk '$9 >= 200 && $9 < 300' | grep 'May/2024' | grep -E 'Sat' | awk '{split($4, time, ":"); if (time[2] >= 11 && time[2] < 15) print}' | wc -l

grep 'GET /telugu/' s-anand.net-May-2024| awk '$9 >= 200 && $9 < 300' | grep 'May/2024' | awk '{print $4}' | sed 's/\[//' | while read datetime; do date -d "$(echo $datetime | sed 's/\// /g' | sed 's/:/ /' | awk '{print $2,$1,$3,$4":"$5":"$6}')" '+%u %H' ; done | awk '$1 == 6 && $2 >= 11 && $2 < 15' | wc -l


grep 'GET /telugu/' s-anand.net-May-2024 | awk '$9 >= 200 && $9 < 300' | grep -E ':(11|12|13|14):' | wc -l


zcat s-anand.net-May-2024.gz | awk -F'"' '$4 ~ /^GET \/telugu\// && $6 >= 200 && $6 < 300 {gsub(/\[|\]/,"",$3); cmd="date -d\""substr($3,1,11)"\" +%u"; cmd | getline dow; close(cmd); split($3,t,":"); if(dow==6 && t[1]>=11 && t[1]<15) count++} END{print count}'

zcat s-anand.net-May-2024.gz | awk '
{
    # Extract time and status code
    match($0, /\[([0-9]+)\/May\/2024:([0-9]{2}):[0-9]{2}:[0-9]{2} \+0000\]/, time);
    match($0, /"(GET [^"]+)"/, request);
    match($0, /" ([0-9]{3}) /, status);

    # Extract day of the week using date command (adjust file name as needed)
    cmd = "date -d \"2024-05-" time[1] "\" +\"%A\"";
    cmd | getline day;
    close(cmd);

    # Apply filtering conditions
    if (day == "Saturday" && time[2] >= 11 && time[2] < 15 && status[1] >= 200 && status[1] < 300 && request[1] ~ /^GET \/telugu\//) {
        count++;
    }
}
END { print count }
'

