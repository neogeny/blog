# -*- coding: utf-8 -*-

import os
import shutil
import sys

from invoke.tasks import task
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

CONFIG = {
    "deploy_path": "build/html",
    "production": "root@localhost:22",
    "dest_path": "/var/www",
    "port": 8000,
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def build(c):
    """Build local version of site"""
    c.run("pelican -s pelicanconf.py")


@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run("pelican -d -s pelicanconf.py")


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run("pelican -r -s pelicanconf.py")


@task
def serve(c):
    """Serve site at http://localhost:8000/"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"], ("", CONFIG["port"]), ComplexHTTPRequestHandler
    )

    sys.stderr.write("Serving on port {port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    c.run("pelican -s publishconf.py")


@task
def publish(c):
    """Build and publish with production settings (rsync)"""
    c.run("pelican -s publishconf.py")
    c.run(
        'rsync --delete --exclude ".DS_Store" -pthrvz -c '
        "{} {production}:{dest_path}".format(
            CONFIG["deploy_path"].rstrip("/") + "/", **CONFIG
        )
    )


@task
def ghp(c):
    """Publish build/html to GitHub Pages via ghp-import"""
    c.run("pelican -s publishconf.py")
    c.run("ghp-import -n -p -f build/html")
