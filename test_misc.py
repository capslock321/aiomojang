import pytest
import aiomojang


@pytest.mark.asyncio
async def test_blocked():
    blocked = await aiomojang.BlockedServers.get_blocked_servers()
    assert type(blocked) == list


@pytest.mark.asyncio
async def test_mojang():
    stat = await aiomojang.Status().mojang
    assert type(stat) == str


@pytest.mark.asyncio
async def test_sell():
    data = await aiomojang.Statistics().get_sales_today("item_sold_minecraft")
    assert data is not None
    assert type(data) == int or float
