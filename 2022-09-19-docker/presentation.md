---
marp: true
class: lead
paginate: true
math: katex
theme: uncover
style: |
  section {

  background-color: #ccc;
  letter-spacing: 1px;
  text-align: left;

  }
  h1 {

  font-size: 1.3em;
  text-align: center;

  }
  h2 {

  font-size: 1.5em;
  text-align: left;

  }
  h3 {

  font-size: 1em;

  text-align: center;
  font-weight: normal;
  letter-spacing: 1px;

  }
  h6 {

  text-align: center;
  font-weight: normal;
  letter-spacing: 1px;

  }
  p{

  text-align: left;
  font-size: 0.75em;
  letter-spacing: 0px;

  }
  img[src$="centerme"] {
  font-size: 0.8em; 
  display:block; 
  margin: 0 auto; 
  }
  footer{

  color: black;
  text-align: left;

  }
  ul {

  padding: 10;
  margin: 0;

  }
  ul li {

  color: black;
  margin: 5px;
  font-size: 30px;

  }
  /* Code */
  pre, code, tt {

  font-size: 0.98em;
  font-size: 25px;
  font-family: Consolas, Courier, Monospace;
  color: white;

  }
  code , tt{

  margin: 0px;
  padding: 2px;
  white-space: nowrap;
  border: 1px solid #eaeaea;
  border-radius: 3px;
  color: white;
  background: black;

  }

  pre {

  background-color: #f8f8f8;
  overflow: auto;
  padding: 6px 10px;
  border-radius: 3px;
  background-color: black;
  }

  pre code, pre tt {

  background-color: transparent;
  border: none;
  margin: 0;
  padding: 0;
  white-space: pre;
  border: none;
  background: transparent;
  }
---

# An introduction to Docker

### Jørgen S. Dokken


###### dokken@simula.no

---
# Docker creates a virtual operating system
<style scoped>ul { padding: 10; list-style: -; }</style>
<style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

[Docker Desktop](https://docs.docker.com/desktop/)
[Docker Client](https://docs.docker.com/engine/reference/commandline/cli)
[Docker Hub](https://hub.docker.com/)

![width:800 center](setup.svg)

<span style="font-size:80%">Figure from: https://docs.docker.com/get-started/overview/</span>

---
# Docker consists of different abstractions

Docker images (Custom filesystem with all preinstalled dependencies)

Docker container (Runnable instance of an image on any OS)


```docker
docker pull ubuntu:22.04
docker run -i -t ubuntu:22.04
```

---

# Important command line arguments (1)
`--name=my-awesome-container` : Give the container a name to easily restart it

```docker
docker run -ti --name=dolfinx_v051 dolfinx/dolfinx:v0.5.1 
docker container start -i dolfinx_v051
```
---

# Important command line arguments (2)
`--rm` : Remove container when exiting

```docker
docker run -ti --name=dolfinx_v051 dolfinx/dolfinx:v0.5.1 
docker container start -i dolfinx_v051
```

---
# Important command line arguments (3)

`-d` : Detach the container from the terminal and run it in the background

```docker
docker run -ti  -d --name="test_env" dolfinx/dolfinx:v0.5.1
docker attach test_env
docker exec -ti test_env sh -c "pip3 install pandas"
``` 

---
# Important command line arguments (4)

`-p 8888:8888` : Map port `8888` on your system to port 8888 in the container

```docker
docker run -ti --rm -p 8888:8888 dolfinx/lab:v0.5.1
```
---

# Important command line arguments (5)
 `-v location_on_host:location_in_container` share a folder with the container 
 
 `-w location_in_container` Working directory (default starting location when starting the container)

 ```docker
docker run -ti --rm -v $(pwd):/root/shared -w /root/shared \
           dolfinx/dolfinx:nightly
```

---
<style scoped>ul { padding: 10; list-style: -; }</style>

# When/why use docker?
- Many environments with different version requirements
- Dependency on "heavy packages" (e.g. PETSc) that takes a long time to install
- Consistent test/end user environments

---
# Building a docker image (1)
requirements.txt
```text
pandas

matplotlib

seaborn

--no-binary=h5py
h5py
```

```bash
pip3 install -r requirements.txt --upgrade
```
---

# Building a docker image (2)

Dockerfile
```docker
FROM dolfinx/lab:v0.5.1
WORKDIR /tmp/
ADD requirements.txt /tmp/requirements.txt
ENV HDF5_MPI="ON" HDF5_DIR="/usr/local/"

RUN CC=mpicc pip3 install -r requirements.txt --upgrade &&\
    pip3 cache purge
ENTRYPOINT ["jupyter", "lab", "--ip", "0.0.0.0", "--no-browser", "--allow-root"]
```

```docker
docker build -t test_image .
```

---
# Where to store a docker image?

- DockerHub (https://hub.docker.com/)
- Quay.io (https://quay.io/)
- Github Packages (https://github.com/features/packages)


---
# Examples of GitHub integration

- Github Packages integration (https://github.com/jorgensd/dolfinx_mpc)
- Advanced build image (https://github.com/FEniCS/dolfinx/blob/main/docker/Dockerfile)
- Binder (https://github.com/jorgensd/dolfinx-tutorial)

---

# Other container systems:
- Buildah (https://buildah.io/)
- Podman (https://podman.io/)
- Containerd (https://containerd.io/)
- ...and many more!