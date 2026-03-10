---
title: Docker Networking 101 - Bridges, Hosts, and Why Your Container Can't See the Internet
date: 2025-03-01
tags: [docker, networking, linux, containers]
description: A mental model for Docker's network modes. Explains bridge, host, none, and macvlan with actual use cases.
---

# Docker Networking 101 — Bridges, Hosts, and Why Your Container Can't See the Internet

Docker networking trips up almost everyone the first time. You run a container, try to hit it from the host, nothing. Or the container can't reach the internet. Let's fix the mental model.

## Second level heading

What does this render too?

### Third level heading

What does THIS render to? Curiours to find out.

#### And tourth level

Let's see how this renders!

##### Fifth

Just for good measure.

###### Six

can we even go this far?

## The Default: Bridge Mode

When you `docker run` without specifying `--network`, you get a **bridge network**. Docker creates a virtual switch (`docker0`) and gives each container a private IP in `172.17.0.0/16`.

```
Host (192.168.1.10)
  └── docker0 (172.17.0.1)
        ├── container A (172.17.0.2)
        └── container B (172.17.0.3)
```

Containers can talk to each other and reach the internet via NAT. The host cannot reach them directly by IP — you need to **publish ports**:

```bash
docker run -p 8080:80 nginx
# host:8080 → container:80
```

### Named Bridge Networks (Do This Instead)

Default bridge has one big problem: containers can't resolve each other by name. Create a named network and they can:

```bash
docker network create myapp
docker run --network myapp --name db postgres
docker run --network myapp --name web nginx
# 'web' can now reach 'db' by hostname
```

This is what `docker-compose` does automatically under the hood.

## Host Mode

```bash
docker run --network host nginx
```

The container shares the host's network namespace. No NAT, no port mapping — it binds directly to the host's interfaces. Port 80 in the container **is** port 80 on the host.

Use this when you need maximum network performance or the app does something weird with raw sockets. Downside: zero network isolation, Linux only (not Mac/Windows Docker Desktop).

## None Mode

```bash
docker run --network none alpine
```

No network interface except loopback. Container is completely isolated. Good for batch jobs processing local files that have no business touching a network.

## Macvlan — Giving Containers a Real LAN IP

This is the power move. Macvlan assigns each container a MAC address and a real IP on your physical network. From the rest of your LAN, the container looks like a real machine:

```bash
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 \
  mylan

docker run --network mylan --ip 192.168.1.50 nginx
```

Now `192.168.1.50` is directly reachable from any device on your network. No port forwarding. Great for homelab services you want on your LAN (Plex, Jellyfin, Home Assistant).

**Gotcha**: the host cannot talk to macvlan containers by default (kernel limitation). You need a macvlan interface on the host side too — see [the macvlan workaround](/post.html?slug=macvlan-host-access).

## Debugging Checklist

When a container can't reach something:

```bash
# What network is it on?
docker inspect <container> | jq '.[].NetworkSettings.Networks'

# Can it reach the gateway?
docker exec <container> ping 172.17.0.1

# DNS working?
docker exec <container> nslookup google.com

# iptables not eating your traffic?
iptables -L DOCKER -n -v
```

## Related Articles

- [Docker Compose for a Self-Hosted Stack](/post.html?slug=docker-compose-selfhost)
- [Macvlan Host Access Workaround](/post.html?slug=macvlan-host-access)

---

_Last updated: March 2025_
