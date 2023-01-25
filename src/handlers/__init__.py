from aiogram import Router


routers: list[Router] = []


def register_handlers(main_router: Router) -> None:
    for router in routers:
        main_router.include_router(router)
