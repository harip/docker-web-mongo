
# Docker compose sample - Python and Mongodb

### Installing
```
Docker compose up
```

This will create two containers. Run the containers in the background using

```
Docker compose up -d
```

Attach to a container

```
docker exec -it CONTAINER bash
```

Connect to Mongodb from host machine

```
mongo 127.0.0.1:27018/test
```