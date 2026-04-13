---
📅 created: 09.04.2026 17:57
aliases:
tags:
  - April 2026
  - chrony
  - linux
author: Martin
---


# [[Chrony Configuration Check - Multiple bindcmdaddress Directives]]

Chrony listens to the last entry it finds. While it officially supports only one `bindcmdaddress` per address family (IPv4/IPv6).[1]

Result Failure test:
- [[chronyd]] does not exit with an error if multiple `bindcmdaddresses` are defined.
* "Last one wins": Final entyr in the config file became active
* `chronyd -n -p -f /etc/chrony.conf` does NOT treat logic errors!

------------------------------
## 1. Syntax Check
RUN:
```SHELL
sudo chronyd -n -p -f /etc/chrony/chrony.conf
```
CHECK RESULTS:
```SHELL
echo $?
```

0 is fine. others errors.

------------------------------
## 2. Test Scenario: Multiple Entries
Add 3 `bindcmdaddress` to `/etc/chrony/chrony.conf`:
```CFG
bindcmdaddress 127.0.0.1
bindcmdaddress 192.168.1.10
bindcmdaddress 127.0.0.2
```

Execution:
   1. Save the configuration.
   2. Restart the service: `sudo systemctl restart chronyd`
   3. Verify status: `systemctl status chronyd` 

------------------------------
## 3. Runtime Check (Socket Analysis)
Check on which addresses [[chrony]] listens
heck the open UDP sockets (Port 323).

RUN:
```SHELL
sudo ss -lupn | grep chronyd
```

OUTPUT:
```SHELL
UNCONN 0      0                  127.0.0.2:323       0.0.0.0:*    users:(("chronyd",pid=11927,fd=5))        
UNCONN 0      0                      [::1]:323          [::]:*    users:(("chronyd",pid=11927,fd=6))        
```

Chrony listens on `127.0.0.2`. 
> previous IPs are ignored.

------------------------------

## 📚 Sources
[1] chrony.conf(5) Manual Page: https://chrony-project.org/doc/3.4/chrony.conf.html#bindcmdaddress



 🔮 Origin:: [[08.04.2026]]
