import pytest
import aiomojang
import datetime


@pytest.mark.asyncio
async def test_skin_url():
    skin = aiomojang.Skin("capslock321")
    assert type(await skin.url()) == str


@pytest.mark.asyncio
async def test_timestamp():
    time = aiomojang.Render("capslock321")
    assert isinstance(await time.timestamp(), str)


@pytest.mark.asyncio
async def test_json():
    data = await aiomojang.Render("capslock321").raw()
    assert type(data) == dict
