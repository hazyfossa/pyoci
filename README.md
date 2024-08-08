# pyoci

[![image](https://img.shields.io/pypi/v/pyoci.svg)](https://pypi.python.org/pypi/pyoci)
[![image](https://img.shields.io/pypi/l/pyoci.svg)](https://pypi.python.org/pypi/pyoci)
[![image](https://img.shields.io/pypi/pyversions/pyoci.svg)](https://pypi.python.org/pypi/pyoci)

**What**: A library to define [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec) compliant container instances.

**When**: When you need to run or modify a container at the lowest level, without containerd or docker/podman.

**Why**: The full OCI runtime spec can be quite large to read and even trickier to implement. This library saves you all the json-wrangling and validation, without abstracting any features away.

**How**: Under the hood, everything here is a msgpack Struct. These structs were generated from the original json-schema with help of [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator) and then manually refactored by me.

#
**Pros**:
- Full control over the container.
- Compatible with many runtimes.
- Very lightweight[^1].

**Cons**:
- Requires low-level knowledge of how a container is constructed.
- Doesn't support dealing with images in any way (for now), you'll need to provide an already existing container root.
- Isn't well tested with runtimes (for now).

#

This is a low-level library. If you want to simply run a container, without configuring all the inner workings, i'd suggest [docker-py](https://github.com/docker/docker-py).

This library is runtime-agnostic, so it doesn't provide a way to actually run the container. You'll need to pass the definition to an appropriate runtime yourself.

Also, I want to say a huge thanks to koxudaxi and other contributors for the awesome code generator!

[^1]: Pyoci should be very fast and memory/resource efficent thanks to use of msgpack. The performance of actually running the container will depend on your provided runtime. However, since using a runtime directly involves much less abstraction than containerd/docker/etc, this approach should be more efficent overall.