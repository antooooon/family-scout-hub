
class UserNotFoundError(Exception):
    """User with the specified telegram_id was not found"""

    def __init__(self, telegram_id: int) -> None:
        self.telegram_id = telegram_id

        super().__init__(
            f"User with telegram_id={telegram_id} not found"
        )

