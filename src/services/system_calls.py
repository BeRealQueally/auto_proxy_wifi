from subprocess import DEVNULL, STDOUT, STARTF_USESHOWWINDOW, STARTUPINFO, check_call, check_output, run, \
    CalledProcessError
from typing import Any
from locale import getpreferredencoding

startupinfo = STARTUPINFO()
startupinfo.dwFlags |= STARTF_USESHOWWINDOW


def exec_code(cmd: Any, verbose: bool = False) -> int:
    """
    Utility function to execute a command in bash and return the exit code.

    PARAMETERS
    ----------
    cmd : Any
        The command to execute.
    verbose : bool
        Whether to print the command and output.

    RETURNS
    -------
    int
        The exit code of the command.
    """
    try:
        return check_call(
            cmd,
            stdout=None if verbose else DEVNULL,
            stderr=STDOUT,
            shell=True,
            startupinfo=startupinfo,
        )
    except CalledProcessError as e:
        if verbose: print(e)


def exec_output(cmd: Any, utf8: bool = False, verbose: bool = False) -> str:
    """
    Utility function to execute a command in bash and return the STDOUT output.

    PARAMETERS
    ----------
    cmd : Any
        The command to execute.
    verbose : bool
        Whether to print the command and output.

    RETURNS
    -------
    str
        The output of the command.
    """
    try:
        return check_output(
            cmd,
            stderr=STDOUT,
            startupinfo=startupinfo,
        ).decode("utf8" if utf8 else getpreferredencoding())
    except CalledProcessError as e:
        if verbose:
            print(e)


def powershell_exec_output(cmd: Any, utf8: bool = False,) -> str:
    """
    Utility function to execute a powershell command and return the STDOUT output.

    PARAMETERS
    ----------
    cmd : Any
        The command to execute.

    RETURNS
    -------
    str
        The output of the command.
    """
    completed = run(
        ["powershell", "-Command", "-WindowStyle Hidden", cmd], capture_output=True, startupinfo=startupinfo,
    )
    return completed.stdout.decode("utf8" if utf8 else getpreferredencoding())
