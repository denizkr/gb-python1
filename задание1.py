duration = int(input("Промежуток времени в секундах:"))
if duration < 60:
    dur_sec = duration
    print(dur_sec, "сек")
elif duration >= 60 and duration < 3600:
    dur_sec = duration % 60
    dur_min = duration // 60
    print(dur_min, "мин", dur_sec, "сек")
elif duration > 3600 and duration < 86400:
    dur_sec = duration % 60
    dur_min = duration % 3600 // 60
    dur_hour = duration // 3600
    print(duration // 3600, "час", duration % 3600 // 60, "мин", duration % 60, "сек")
elif duration > 86400:
    dur_sec = duration % 86400 % 3600 % 60
    dur_min = duration % 86400 % 3600 // 60
    dur_hour = duration % 86400 // 3600
    dur_day = duration // 86400
    print(dur_day, "дн", dur_hour, "час", dur_min, "мин", dur_sec, "сек")