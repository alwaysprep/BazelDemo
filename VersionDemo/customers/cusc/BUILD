load("@cusc//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary")


py_binary(
    name="app",
    srcs=["app.py"],
    deps=[
        requirement("libx-alwaysprep"),
        requirement("liby-alwaysprep")
    ]
)
