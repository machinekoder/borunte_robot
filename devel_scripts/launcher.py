# -*- coding: utf-8 -*-
import os
import shlex
import sys
import time

TIMEOUT = 1.0

processes = []  # type: List[sh.RunningCommand]


class ProgramTerminated(Exception):
    pass


def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def start_process(command, line):
    """

    :type command: sh.Command
    """
    processes.append(
        command(shlex.split(line), _out=sys.stdout, _err=sys.stderr, _bg=True)
    )
    time.sleep(TIMEOUT)


def terminate_processes():
    for process in processes:
        if process is None:
            continue
        try:
            process.terminate()
        except OSError:
            pass
        process.wait()


def check_processes():
    for process in processes:
        if process is None:
            continue
        if not check_pid(process.pid):
            raise ProgramTerminated()


def wait_loop():
    try:
        while True:
            check_processes()
            time.sleep(TIMEOUT)
    except KeyboardInterrupt:
        pass
    except ProgramTerminated:
        print('A program terminated, stopping other processes.')
