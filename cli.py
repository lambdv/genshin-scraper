# app.py
import typer
import wikiscrapper  as wiki
import tclscrapper   as tcl
import os
import time as timer
import json
import manager as m
import utils

app = typer.Typer()

@app.command()
def compile():
    print("Compiling...")
    m.compile_json_files("./genshindata/public/data/artifacts", "./genshindata/public/data/", "artifacts.json")
    m.compile_json_files("./genshindata/public/data/characters", "./genshindata/public/data/", "characters.json")
    m.compile_json_files("./genshindata/public/data/weapons", "./genshindata/public/data/", "weapons.json")
    print("Compiled")

@app.command()
def update():
    print("Updating...")
    wiki.weaponDBSync(overrideData=False, overrideAssets=False)
    wiki.characterDBSync(overrideData=False, overrideAssets=False)
    wiki.artifactDBSync(overrideData=False, overrideAssets=False)
    print("Updated")

if __name__ == "__main__":
    app()
