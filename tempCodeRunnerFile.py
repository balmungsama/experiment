import string, random
class Trial_stim:
    def __init__(self, block_count, trial_count, speed):
        self.block_count = block_count
        self.trial_count = trial_count
        self.speed = speed
        self.stimuli = list(string.ascii_uppercase)
    def stim_order(self,num_stim): # num_stim can be 1 or 2, determines the number of 
        self.num_stim = num_stim
        try:
            if self.num_stim not in [1,2]:
                raise ValueError("The number of numerical stimuli displayed must be either 1 or 2.")
        except (IndexError):
            exit('could not complete request')
        self.stim_count = random.choice(range(15,20)) - num_stim
        self.stimuli = [random.choice(self.stimuli) for stim in range(self.stim_count)]
        self.stimuli.extend([random.choice(range(10)) for ii in range(num_stim)])
        self.stimuli = random.sample(self.stimuli, len(self.stimuli))

        if num_stim == 1 and random.choice(range(1,6)) == 1:
            self.stimuli[random.choice(range(len(self.stimuli)))] = ' '

        print(len(self.stimuli))
        print(self.stimuli)


test_class = Trial_stim(
    block_count = 1, 
    trial_count = 1, 
    speed = 'slow'
)
test_class.stim_order(
    num_stim = 3
)
