from .default import default_router

from aiogram import Router


routers: list[Router] = [default_router]


def register_handlers(main_router: Router) -> None:
    for router in routers:
        main_router.include_router(router)
