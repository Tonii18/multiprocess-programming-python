def messages_analysis(fragment):
    messages_map = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for line in fragment:
        parts = line.strip().split(';')
        level = parts[2].strip().upper()
        if level in messages_map:
            messages_map[level] += 1
        else:
            messages_map[level] = 1

    return messages_map


def ips_analysis(fragment):
    ip_counts = {}
    for line in fragment:
        parts = line.split(';')
        ip = parts[3].strip()
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

    return ip_counts


def errors_by_hours_analysis(fragment):
    hour_counts = {}
    unknown_key = 'unknown'
    message_type = 'ERROR' # We can change it to the kind message we want

    for line in fragment:
        parts = line.split(';')
        event = parts[2].strip().upper()

        if event != message_type:
            continue

        time_field = parts[1].strip() if len(parts) > 1 else ""
        if not time_field:
            hour_counts[unknown_key] = hour_counts.get(unknown_key, 0) + 1
            continue

        try:
            hour_str = time_field.split(':')[0]
            hour = int(hour_str)
            if 0 <= hour <= 23:
                hour_key = f"{hour:02d}"
                hour_counts[hour_key] = hour_counts.get(hour_key, 0) + 1
            else:
                hour_counts[unknown_key] = hour_counts.get(unknown_key, 0) + 1
        except Exception:
            hour_counts[unknown_key] = hour_counts.get(unknown_key, 0) + 1

    return hour_counts
