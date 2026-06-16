**Step 1:** Make sure the system has everything installed.

```
sudo apt update && sudo apt install -y git python3 python3-pip python3-venv python-is-python3
```

**Step 2:** Set up the dev environment.

```
git clone https://github.com/1BH23CS024/BCSL606.git --depth=1 && cd BCSL606 && python3 -m venv .venv && source .venv/bin/activate && pip install upgrade -r requirements.txt
```

This should setup everything and install all the required packages. You will be able to use it comfortably if you're not retarded, otherwise we'd have bigger things to worry about.

Thank you.

**Update:** With @daddys-dispatch help, the code has been posted as Python files as well. Most of them can't be executed on the terminal directly because they were written for Jupyter notebooks. The goal was to provide files for easy accessibility via the terminal using `cat`, which works flawlessly. As usual, love you babe! 😘
