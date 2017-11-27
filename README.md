# facebook-remove
Helps remove Facebook cache &amp; cookies!

To run it periodically, use crontab.
1. Open a Terminal and run,
```
crontab -e
```
this should open an Editor. There you can type
2. For every hour:
```
crontab 0 * * * * /path/to/script
```
3. For every minute:
```
crontab * * * * * /path/to/script
```
And to see your crontabs
```
crontab -l
```
