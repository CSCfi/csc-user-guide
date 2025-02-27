from .hook import SoftwareCatalogHook

hook = SoftwareCatalogHook()

on_config = hook.on_config
on_page_markdown = hook.on_page_markdown
on_page_context = hook.on_page_context
on_post_build = hook.on_post_build
on_serve = hook.on_serve

__all__ = [name for name in locals().keys() if name.startswith("on_")]
