async def async_turn_on(self, **kwargs):
    # Call the Bluelinky API to start the vehicle
    await self.client.start_vehicle()
