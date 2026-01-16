# version-api

This is a very simple `fast-api` python app that will query the podman socket, and return the version for that container.

It is completly unsecure, and I only use it in an environment with no outside access. Keep that in mind if you want to use it.

This requires a podman socket to access. For a user one, you can enable it with `systemctl --user enable --now podman.socket`

you can run it with:

```
podman run -d \
  --name version-api \
  -p 8080:8080 \
  -v /run/user/$(id -u)/podman/podman.sock:/run/podman/podman.sock \
  --security-opt label=disable \
  --user 0 \
  --restart always \
  ghcr.io/lmagomes/version-api:0.1.0
```

and then make a request to a service you are running

```
curl 127.0.0.1:8888/version/jellyfin
```

When the service is the name of the container.

