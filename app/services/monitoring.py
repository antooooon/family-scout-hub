from app.db.repositories.monitoring import MonitoringRepository


class MonitoringService:
    """
    1. есть telegram_id
    2. надо для каждого канала, доступного по этому telegram_id достать конфиг
    3. конфиг: /канал: к.слово1, к.слово2, к.слово3/
    """

    def __init__(
            self,
            repository: MonitoringRepository
    ):
        self.repository = repository

    async def get_monitoring_config(
            self,
            channels_ids: list
    ) -> dict:
        result_map = await self.repository.get_monitoring_data(channels_ids=channels_ids)

        channels_map = {}

        for row in result_map:
            channel_id = row["telegram_id"]
            settings_id = row["settings_id"]
            settings_name = row["settings_name"]
            keyword = row["word"]

            channels_map.setdefault(channel_id, {})
            channels_map[channel_id].setdefault(
                settings_id,
                {
                    "settings_name": settings_name,
                    "keywords": [],
                }
            )
            channels_map[channel_id][settings_id]["keywords"].append(keyword)

        return channels_map
