# NAO Interactive Behavior (Choregraphe + Python SDK)

This project implements interactive behaviours using Choregraphe and NAOqi Python SDK.  
It includes both the original graphical behavior (`behavior.xar`), the choregraphe file, the exported crg file in export/ and a modular Python version that performs the same speech-triggered gestures.

---

## Features

- Works with the NAO virtual robot (simulated test) or a real NAO robot (live speech recognition)

---

##  Getting Started

### 1️⃣ Clone the Repository

---

### 2️⃣ Set Up Python 2.7 Environment (recommended: pyenv)

```bash
pyenv install 2.7.18
pyenv virtualenv 2.7.18 nao_env
pyenv activate nao_env
```

---

### 3️⃣ Install NAOqi Python SDK

#### Download

Go to [SoftBank Robotics Community Downloads](https://community.aldebaran.com/en/resources/software)  
Download: `pynaoqi-python2.7-2.8.6.23-linux64.tar.gz`

#### Extract and Configure

```bash
tar -xzf pynaoqi-python2.7-2.8.6.23-linux64.tar.gz
export PYTHONPATH=$PYTHONPATH:/full/path/to/pynaoqi-python2.7-2.8.6.23-linux64/lib
```

To make it permanent:
```bash
echo 'export PYTHONPATH=$PYTHONPATH:/path/to/naoqi-sdk/lib' >> ~/.bashrc
source ~/.bashrc
```

---

## How to Run

### For Testing (No Real Robot Needed)

```bash
python2 main.py
```

---

### 🗣️ For Live Speech Recognition (Real NAO Robot Required)

```bash
python2 main.py
```

> Make sure your NAO is powered on and connected to the same network.  
> Update the `ROBOT_IP` variable in `main.py` to match your NAO's IP address.

---

## Author

**Bakel Bakel**  
*Marine Autonomy | Robotics | NAO Developer*

