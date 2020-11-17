class World:
    """
    Representation of the cooperative environment
    """

    def __init__(self):
        self._agents = []
        self._entities = self.load_entities()

    def load_entities(self):
        """
        Load the entities.
        """
        # TODO: Use a JSON file!
        pass

    def add_agent(self, agent):
        """
        Add new agent to the virtual environment.
        :param agent: an agent object
        :return: None
        """
        self._agents.append(agent)

    def draw(self):
        """
        Draw the virtual environment.
        """
        for agent in self._agents:
            agent.draw()

