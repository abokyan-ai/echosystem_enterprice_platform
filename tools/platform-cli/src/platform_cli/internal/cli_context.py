"""Invocation-local command state; no global services or configuration lookup."""
from contextlib import contextmanager
from dataclasses import dataclass
import signal
import threading
from platform_cli.public import CliServices, PlatformRequest


@dataclass
class CliExecutionContext:
    request: PlatformRequest
    services: CliServices
    output: object
    cancellation: threading.Event
    working_directory: object

    @contextmanager
    def signal_scope(self):
        previous = {}
        try:
            if threading.current_thread() is threading.main_thread():
                for sig in (signal.SIGINT, signal.SIGTERM):
                    previous[sig] = signal.getsignal(sig)
                    signal.signal(sig, lambda signum, frame: self.cancellation.set())
            yield
        finally:
            for sig, handler in previous.items():
                signal.signal(sig, handler)
