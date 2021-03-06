from adapters import PullRequestAdapter
from adapters import PushAdapter

from listeners.push import CLAPushListener
from listeners.pulls import AutomaticPR

def route_and_handle(headers, body):
    hooktype = headers.get('X-Github-Event')
    if hooktype == "pull_request":
        pr = PullRequestAdapter()
        pr.add_listener(AutomaticPR())
        pr.handle(body)
    elif hooktype == "push":
        pu = PushAdapter()
        pu.handle(body)
