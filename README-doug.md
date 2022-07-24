I had to make 2 changes to get this to work.

1. I was getting date parsing errors.  The code had date workaround for tv shows, but not for movies. I did the same workaround for movies. But I hard coded the date format to my format.

```
time = datetime.datetime.strptime(watchedTime + " 20:15", config.CSV_DATETIME_FORMAT + " %H:%M")
```

```
try:
        time = datetime.datetime.strptime(watchedTime + " 20:15", config.CSV_DATETIME_FORMAT + " %H:%M")
except ValueError:
    # try the date with a dot (also for backwards compatbility)
    # watchedTime = re.sub("[^0-9]", ".", watchedTime)
    time = datetime.datetime.strptime(watchedTime + " 20:15", "%m.%d.%y" + " %H:%M")
```

2.  I was getting timeouts and my file was so big, I decided to break it down to smaller files.  I used split to do this.

```
split -l 500 NetflixViewingHistory.csv NetflixViewingHistory
```

Then fixed the naming to look like: NetflixViewingHistory1.csv, NetflixViewingHistory2.csv,....