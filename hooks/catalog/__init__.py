from .hook import CatalogHook

hook = CatalogHook(name=__name__)

def __getattr__(name):
    return hook.plugin_events[name]

__all__ = tuple(hook.plugin_events.keys())
