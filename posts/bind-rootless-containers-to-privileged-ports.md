---
📅 created: 06.04.2025 21:20
aliases:
  - nerdctl bin rootless ports
tags:
  - nerdctl
  - containerd
  - ports
  - container
  - rootless
author: Martin
---


# [[Bind rootless containers to privileged ports]]

To bind a port from [[rootless]] containers to [[privileged ports]] in Linux you can:
- Allow one binary to use unprivileged ports, setting `CAP_NET_BIND_SERVICE`to rootlesskit binary
- Lower the systems unpribileged port range

## Set the cap_net_bind_service to rootless kit
To keep the system-wide post limit at 1024 but allow specific rootless tool to bypass it:
Set the `CAP_NET_BIND_SERVICE` capability for the rootless kit, where you installed [[nerdctl]], in rootless usually `/usr/local/bin/rootlesskit`. Alternative `$(which rootlesskit)`:

```SHELL
sudo setcap cap_net_bind_service=ep $(which rootlesskit)
```

THen restart `containerd` or restart your session
```SHELL
systemctl restart --user containerd.service
```

To remove the capability:
```SHELL
sudo setcap -r $(which rootlesskit)
# Then restart session or containerd
```


## System-wide: Modifying the range of unprivileged ports
Override the unprivileged port start to starting at 80:
```SHELL
echo net.ipv4.ip_unprivileged_port_start = 80 | sudo tee /etc/sysctl.d/90-unprivileged_port_start.conf
```

Apply the changes:
```SHELL
sudo sysctl --system
```

Check the current range with:
```SHELL
cat /proc/sys/net/ipv4/ip_unprivileged_port_start
```


🔗 URL :: https://linuxconfig.org/how-to-bind-a-rootless-container-to-a-privileged-port-on-linux


 🔮 Origin:: [[06.04.2025]]
