import pytest
import aiomojang

@pytest.mark.asyncio
async def test_players():
    player = await aiomojang.Players().get_uuids("capslock321", "Hypermnesia")
    assert type(player) == list


@pytest.mark.asyncio
async def test_player():
    player = await aiomojang.Player("capslock321").uuid
    assert player is not None
    assert type(player) == str
