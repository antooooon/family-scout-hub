from fastapi import APIRouter

from app.services.channels.service import ChannelService


router = APIRouter(prefix="/channels")

channels_service = ChannelService()


@router.get("/")
async def get_channels():
    channels = await channels_service.repository.get_active_channels()

    return channels


@router.get("/id")
async def get_channels(channel_id):
    return f"channel_id is {channel_id}"


@router.post("/{channel_id}")
async def post_channels(channel_id: int):
    return await channels_service.create_channel(channel_id)