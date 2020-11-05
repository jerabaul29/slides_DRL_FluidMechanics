from tensorforce.environments import Environment

class MyEnvironment(Environment):
    def states(self):
        """Returns the state space specification.
        """

    def actions(self):
        """Returns the action space specification.
        """

    def reset(self):
        """Resets the environment to start a new episode.
        Returns: dict[state]: Dictionary containing initial state(s) and auxiliary information.
        """

    def execute(self, actions):
        """Executes the given action(s) and advances the environment by one step.
        Args: actions (dict[action]): Dictionary containing action(s) to be executed
        Returns:
            ((dict[state], bool | 0 | 1 | 2, float)): Dictionary containing next state(s),
            terminal information, and observed reward.
        """
