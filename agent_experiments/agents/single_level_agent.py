from agents.base_agent import Agent


class SingleLevelAgent(Agent):
    """An agent that uses DialogModel as an AI."""
    def __init__(self, model, rpf, cpf, name='AI'):
        super(SingleLevelAgent, self).__init__()
        self.model = model
        self.rpf = rpf  # "Response prompt function"
        self.cpf = cpf  # "Choice prompt function"
        self.name = name
        self.human = False

    def feed_context(self, ctx):
        # Reset/track dialogue contents
        self.dialogue = []

        self.ctx = ctx

    def write(self):
        # generate a new utterance
        response_prompt = self.rpf({
            'ctx': self.ctx,
            'dialogue': self.dialogue
        })
        response = self.model.get_model_outputs([response_prompt])[0]
        response_sp = response.split()

        if response_sp[0] != 'YOU:':
            # first add the special 'YOU:' token if necessary
            self.dialogue.append('YOU:')
        else:
            # Remove you token from response string if necessary
            response = response.lstrip('YOU:').lstrip()
        # then append the utterance
        self.dialogue.extend(response_sp)

        return response

    def read(self, inpt):
        inpt_sp = inpt.split()

        # first add the special 'YOU:' token if necessary
        self.dialogue.append('THEM:')
        # then append the utterance
        self.dialogue.extend(inpt_sp)

    def choose(self):
        # generate a new utterance
        choice_prompt = self.cpf({
            'ctx': self.ctx,
            'dialogue': self.dialogue
        })
        choice = self.model.get_model_outputs([response_prompt])[0]

        try:
            choice = [int(c) for c in choice.split()]
        except:
            print('Choice values could not be parsed from model response')
            return ['<no_agreement>' for _ in range(3)]

        return choice
