# Apptainer image for 3DSlicer

Build it with:

```
tmpdir=$(pwd)"/tmp"
mkdir -p $tmpdir
export APPTAINER_TMPDIR=$tmpdir
cachedir=$(pwd)"/cache"
mkdir -p $cachedir
export APPTAINER_CACHEDIR=$cachedir
apptainer build slicer.sif slicer.def 2>&1|tee slicer.log
```

Before run it, set up a temporary folder e.g. under your home

```
mkdir -p  ~/.slicer/user
```

And then run it with

```
apptainer run --nv --bind ~/.slicer/user:/var/cache/user  slicer.sif
```

If needed with your X11 settings you might need some extra options:

```
apptainer run --nv --bind /tmp/.X11-unix:/tmp/.X11-unix --bind ~/.slicer/user:/var/cache/user --env DISPLAY=$DISPLAY slicer.sif
```

There are mount points `/l`, `/m`, `/scratch` already created in the container if you want to bind data folders to those locations.


