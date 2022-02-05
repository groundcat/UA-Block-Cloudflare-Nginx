

# Reads the UA list from the file "ua_list.txt"
ua_file = open("ua_list.txt", "r")
lines = ua_file.readlines()
ua_list = []
for line in lines:
    line_cleaned = line.replace("\n","").lower()
    ua_list.append(line_cleaned)
    ua_list.sort()
ua_list = list(dict.fromkeys(ua_list))
ua_list_count = len(ua_list)
print(ua_list)
print("Identified ",ua_list_count," UAs in the file.")
ua_file.close()


# Write the sorted list back to the file "ua_list.txt"
ua_file_sorted = open("ua_list.txt", "w")
for ua in ua_list:
    ua_line = ua + "\n"
    ua_file_sorted.write(ua_line)
ua_file_sorted.close


# Generate Cloudflare configuration in the string "ua_list_cf"
ua_list_cf = ""
i = 0
for ua in ua_list:
    if (i < ua_list_count - 1):
        cf_single_rule = "(http.user_agent contains \"" + ua + "\") or "
    else:
        cf_single_rule = "(http.user_agent contains \"" + ua + "\")"
    ua_list_cf = ua_list_cf + cf_single_rule
    i += 1


# Write Cloudflare configuration to the file "ua_list_cf.txt"
ua_file_cf = open("ua_list_cf.txt", "w")
ua_file_cf.write(ua_list_cf)
ua_file_cf.close
print("Cloudflare firewall rules generated in the file 'ua_list_cf.txt'")


# Generate nginx configuration in the string "ua_list_nginx"
# Using nginx case insensitive matching
ua_list_nginx = "if ($http_user_agent ~* ("
i = 0
for ua in ua_list:
    if (i < ua_list_count - 1):
        nginx_single_rule = ua + "|"
    else:
        nginx_single_rule = ua
    i += 1
    ua_list_nginx = ua_list_nginx + nginx_single_rule
ua_list_nginx = ua_list_nginx + ")) {\n    return 403;\n}"


# Write nginx configuration to the file "ua_list_nginx.conf"
ua_file_nginx = open("ua_list_nginx.conf", "w")
ua_file_nginx.write(ua_list_nginx)
ua_file_nginx.close
print("Nginx file generated in the file 'ua_list_nginx.conf', please insert this into your Nginx configuration within server{} block")
